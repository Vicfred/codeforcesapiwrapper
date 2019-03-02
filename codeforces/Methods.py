from typing import List, Optional
import requests

from codeforces.BlogEntry import BlogEntry
from codeforces.Comment import Comment
from codeforces.User import User

base_url = "http://codeforces.com/api/"


def blogEntry_comments(blogEntryId: int) -> Optional[List[Comment]]:
    method_route = "blogEntry.comments"
    r = requests.get(base_url + method_route, params={"blogEntryId": blogEntryId})
    if r.status_code != 200:
        return None
    json = r.json()
    if json["status"] != "OK":
        return None
    result = json["result"]
    comments = list()
    for comment in result:
        comments.append(Comment(**comment))
    return comments

def blogEntry_view(blogEntryId: int) -> BlogEntry:
    method_route = "blogEntry.view"
    r = requests.get(base_url + method_route, params={"blogEntryId": blogEntryId})
    if r.status_code != 200:
        return None
    json = r.json()
    if json["status"] != "OK":
        return None
    result = json["result"]
    return BlogEntry(**result)


def user_info(handles: List[str]) -> Optional[List[User]]:
    if len(handles) > 1000:
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
    json = r.json()
    if json["status"] != "OK":
        return None
    result = json["result"]
    users = list()
    for user in result:
        users.append(User(**user))
    return users
