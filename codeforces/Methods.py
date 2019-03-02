from typing import List, Optional
from .User import User

import requests

base_url = "http://codeforces.com/api/"


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
