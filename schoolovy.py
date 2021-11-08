import yaml
import schoolopy
import sys


def err(msg):
    """
    Prints out error message and exits with error.
    """
    print(f"Error: {msg}")
    exit(1)


def main(limit):
    """
    Likes all the posts & comments
    in your most recent feed (20 posts).

    Args:
        limit: How many posts to like.

    Returns:
        A message of the number of posts & comments that were newly liked.
    """
    with open('config.yaml', 'r') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
    sc = schoolopy.Schoology(schoolopy.Auth(config['key'],
                                            config['secret']))
    post_liked = 0
    comments_liked = 0

    # Set the number of posts to check
    try:
        sc.limit = int(limit)
    except ValueError:
        err("The 'limit' argument must be a number")

    # Get updates
    try:
        updates = sc.get_feed()
    except KeyError:
        err("The key or secret is incorrect")

    print("Liking posts...")

    # Go through all most recent 20 posts
    for update in updates:

        # Check if post is in 'unlike_list'
        if (int(update.id) not
            in config.get('unlike_list').get('posts', []) and
                int(update.uid) not in
                config.get('unlike_list').get('users', [])):
            # Like post
            try:
                sc.like(update.id)
                post_liked += 1
            # KeyError is sometimes thrown randomly
            # for apparently no reason.
            except (schoolopy.NoDifferenceError, KeyError):
                continue

        # Get comments if post is in a group
        if update.realm == "group":
            comments = sc.get_group_update_comments(update.id,
                                                    update.group_id)
        # Else get comments if post is in a course
        elif update.realm == "section":
            comments = sc.get_section_update_comments(update.id,
                                                      update.section_id)
        else:
            continue

        # Go through the comments inside the group
        for comment in comments:
            # Check if comment is in 'unlike_list'
            if (int(comment.id) not in
                config.get('unlike_list').get('comments', []) and
                    int(comment.uid) not in
                    config.get('unlike_list').get('users', [])):
                try:
                    sc.like_comment(update.id, comment.id)
                    comments_liked += 1
                except (schoolopy.NoDifferenceError, KeyError):
                    continue

    return ("---------------\n"
            f"Liked {post_liked} posts and {comments_liked} comments")


if __name__ == "__main__":
    # Too many arguments are specified
    if len(sys.argv) > 2:
        err("Only the 'limit' argument is allowed")
    # Default limit is 20
    limit = 20 if len(sys.argv) == 1 else sys.argv[1]
    print(main(limit))
