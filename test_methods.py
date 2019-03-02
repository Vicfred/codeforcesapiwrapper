from codeforces.Methods import *


def test_blogEntry_comments():
    comments = blogEntry_comments(79)
    for comment in comments:
        print(comment)


def test_blogEntry_view():
    print(blogEntry_view(79))


def test_user_info():
    users = user_info(["Vicfred", "Fefer_Ivan", "tourist", "rng_58"])
    for user in users:
        print(user)
