from typing import List, Optional
import requests
import json

from codeforces.BlogEntry import BlogEntry
from codeforces.Comment import Comment
from codeforces.Contest import Contest
from codeforces.Hack import Hack
from codeforces.Problem import Problem
from codeforces.ProblemStatistics import ProblemStatistics
from codeforces.RanklistRow import RanklistRow
from codeforces.RatingChange import RatingChange
from codeforces.RecentAction import RecentAction
from codeforces.Submission import Submission
from codeforces.User import User

base_url = "http://codeforces.com/api/"


# noinspection PyPep8Naming
def blogEntry_comments(blog_entry_id: int) -> Optional[List[Comment]]:
    method_route = "blogEntry.comments"
    r = requests.get(base_url + method_route, params={"blogEntryId": blog_entry_id})
    if r.status_code != 200:
        return None
    json_response = r.json()
    if json_response["status"] != "OK":
        return None
    result = json_response["result"]
    comments = list()
    for comment in result:
        comments.append(Comment(**comment))
    return comments


# noinspection PyPep8Naming
def blogEntry_view(blog_entry_id: int) -> BlogEntry:
    method_route = "blogEntry.view"
    r = requests.get(base_url + method_route, params={"blogEntryId": blog_entry_id})
    if r.status_code != 200:
        return None
    json_response = r.json()
    if json_response["status"] != "OK":
        return None
    result = json_response["result"]
    return BlogEntry(**result)


def contest_hacks(contest_id: int) -> List[Hack]:
    method_route = "contest.hacks"
    r = requests.get(base_url + method_route, params={"contestId": contest_id})
    if r.status_code != 200:
        return None
    json_response = r.json()
    if json_response["status"] != "OK":
        return None
    result = json_response["result"]
    hacks = list()
    for hack in result:
        hacks.append(Hack(**hack))
    return hacks


def contest_list(*gym) -> List[Contest]:
    # TODO update to call not anonymously
    method_route = "contest.list"
    r = requests.get(base_url + method_route, params={"gym": gym})
    if r.status_code != 200:
        return None
    json_response = r.json()
    if json_response["status"] != "OK":
        return None
    result = json_response["result"]
    contests = list()
    for contest in result:
        contests.append(Contest(**contest))
    return contests


# noinspection PyPep8Naming
def contest_ratingChanges(contest_id: int) -> List[RatingChange]:
    method_route = "contest.ratingChanges"
    r = requests.get(base_url + method_route, params={"contestId": contest_id})
    if r.status_code != 200:
        return None
    json_response = r.json()
    if json_response["status"] != "OK":
        return None
    result = json_response["result"]
    rating_changes = list()
    for rating_change in result:
        rating_changes.append(RatingChange(**rating_change))
    return rating_changes


def contest_standings(contest_id: int, **kwargs) -> str:
    """
    kwargs should be a dictionary, please pass it as such
    because of the `from` parameter which is also a python
    reserved keyword.

    returns a dictionary with 3 keys
    contest -> a Contest object
    problems -> a list of Problem objects
    rows -> a list of RanklistRow objects
    """
    method_route = "contest.standings"
    params = kwargs
    params["contestId"] = contest_id
    r = requests.get(base_url + method_route, params=params)
    if r.status_code != 200:
        return None
    json_response = r.json()
    if json_response["status"] != "OK":
        return None
    result = json_response["result"]
    response = dict()
    response["contest"] = Contest(**result["contest"])
    response["problems"] = list()
    for problem in result["problems"]:
        response["problems"].append(Problem(**problem))
    response["rows"] = list()
    for row in result["rows"]:
        response["rows"].append(RanklistRow(**row))
    return response


def contest_status(contest_id: int, **kwargs) -> List[Submission]:
    """
    because `from` is a python reserved word and an optional parameter
    for the request you must pass kwargs as a dictionary
    """
    method_route = "contest.status"
    params = kwargs
    params["contestId"] = contest_id
    r = requests.get(base_url + method_route, params=params)
    if r.status_code != 200:
        return None
    json_response = r.json()
    if json_response["status"] != "OK":
        return None
    result = json_response["result"]
    submissions = list()
    for submission in result:
        submissions.append(Submission(**submission))
    return submissions


def problemset_problems(**kwargs):
    """
    returns a dictionary with 2 keys
    problems -> list of Problem objects
    problemStatistics -> list of ProblemStatistics objects
    """
    method_route = "problemset.problems"
    r = requests.get(base_url + method_route, kwargs)
    if r.status_code != 200:
        return None
    json_response = r.json()
    if json_response["status"] != "OK":
        return None
    result = json_response["result"]
    response = dict()
    response["problems"] = list()
    for problem in result["problems"]:
        response["problems"].append(Problem(**problem))
    response["problemStatistics"] = list()
    for statistic in result["problemStatistics"]:
        response["problemStatistics"].append(ProblemStatistics(**statistic))
    return response


# noinspection PyPep8Naming
def problemset_recentStatus(count: int, *problemSetName) -> List[Submission]:
    method_route = "problemset.recentStatus"
    r = requests.get(base_url + method_route, params={"count": count, "problemsetName": problemSetName})
    json_response = r.json()
    if json_response["status"] != "OK":
        return None
    result = json_response["result"]
    submissions = list()
    for submission in result:
        submissions.append(Submission(**submission))
    return submissions


# noinspection PyPep8Naming
def recentActions(maxCount: int) -> List[RecentAction]:
    method_route = "recentActions"
    r = requests.get(base_url + method_route, params={"maxCount": maxCount})
    json_response = r.json()
    if json_response["status"] != "OK":
        return None
    result = json_response["result"]
    recent_actions = list()
    for action in result:
        recent_actions.append(RecentAction(**action))
    return recent_actions


def user_info(handles: List[str]) -> Optional[List[User]]:
    if len(handles) > 10_000:
        return None
    method_route = "user.info"
    params = dict()
    params["handles"] = str()
    for (index, handle) in enumerate(handles):
        if index > 0:
            params["handles"] += ";"
        params["handles"] += handle
    r = requests.get(base_url + method_route, params=params)
    if r.status_code != 200:
        return None
    json_response = r.json()
    if json_response["status"] != "OK":
        return None
    result = json_response["result"]
    users = list()
    for user in result:
        users.append(User(**user))
    return users
