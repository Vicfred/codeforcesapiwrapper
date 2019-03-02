from codeforces.Methods import *


# noinspection PyPep8Naming
def test_blogEntry_comments():
    comments = blogEntry_comments(79)
    for comment in comments:
        print(comment)


# noinspection PyPep8Naming
def test_blogEntry_view():
    print(blogEntry_view(79))


def test_contest_hacks():
    hacks = contest_hacks(566)
    for hack in hacks:
        print(hack)


def test_contest_list():
    contests = contest_list()
    for contest in contests:
        print(contest)


# noinspection PyPep8Naming
def test_contest_ratingChanges():
    rating_changes = contest_ratingChanges(566)
    for rating_change in rating_changes:
        print(rating_change)


def test_contest_standings():
    params = dict()
    params["from"] = 1
    params["count"] = 5
    params["room"] = 28
    resp = contest_standings(566, **params)
    print("=========")
    print("contest:")
    print("=========")
    print(resp["contest"])
    print("=========")
    print("problems:")
    print("=========")
    for problem in resp["problems"]:
        print(problem)
    print("=========")
    print("rows:")
    print("=========")
    for row in resp["rows"]:
        print(row)


def test_contest_status():
    submissions = contest_status(566)
    for submission in submissions:
        print(submission)


def test_user_info():
    users = user_info(["Vicfred", "Fefer_Ivan", "tourist", "rng_58"])
    for user in users:
        print(user)
