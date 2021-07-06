import yaml
import schoolopy
import sys


def err(msg):
    """
    Prints out error message and exits with error.
    """
    print(f"Error: {msg}")
    exit(1)


def main():
    """
    Likes all the posts & comments
    in your most recent feed (20 posts).

    Returns:
        Number of posts & comments that were newly liked.
    """
    with open('config.yaml', 'r') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
    sc = schoolopy.Schoology(schoolopy.Auth(config['key'],
                             config['secret']))
    post_liked = 0
    comments_liked = 0

    if len(sys.argv) != 2:
        err("Only the 'limit' argument is allowed")

    # Set the number of posts to check
    try:
        sc.limit = int(sys.argv[1])
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

        # Like post
        try:
            sc.like(update.id)
            post_liked += 1
        except schoolopy.NoDifferenceError:
            pass

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
            # Like each comment
            try:
                sc.like_comment(update.id, comment.id)
                comments_liked += 1
            except schoolopy.NoDifferenceError:
                continue

    return ("---------------\n"
            f"Liked {post_liked} posts and {comments_liked} comments")


if __name__ == "__main__":
    print(main())
