import yaml
import schoolopy


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
    print("Sharing love...")
    liked = 0
    # Go through all most recent 20 posts
    for update in sc.get_feed():
        # Like post
        try:
            sc.like(update.id)
            liked += 1
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
                liked += 1
            except schoolopy.NoDifferenceError:
                continue
    return liked


if __name__ == "__main__":
    print(f"Liked {main()} new posts")
