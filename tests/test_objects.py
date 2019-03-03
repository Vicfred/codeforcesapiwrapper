# -*- coding: utf-8 -*-
import requests
from codeforces.User import User
from codeforces.Contest import Contest
from codeforces.Problem import Problem
from codeforces.Submission import Submission


def test_user():
    params = {"handles": "Vicfred"}
    r = requests.get("https://codeforces.com/api/user.info", params=params)
    assert r.status_code == 200
    json = r.json()
    assert json["status"] == "OK"
    result = json["result"]
    assert len(result) >= 1
    vicfred = User(**result[0])
    assert vicfred.handle == "Vicfred"
    print(vicfred)


def test_contest():
    params = {"gym": "false"}
    r = requests.get("https://codeforces.com/api/contest.list", params=params)
    assert r.status_code == 200
    json = r.json()
    assert json["status"] == "OK"
    result = json["result"]
    assert len(result) >= 1
    for contest in result:
        print(Contest(**contest))


def test_problem():
    params = {"tags": "implementation"}
    r = requests.get("https://codeforces.com/api/problemset.problems", params=params)
    assert r.status_code == 200
    json = r.json()
    assert json["status"] == "OK"
    result = json["result"]
    assert len(result) >= 1
    for problem in result["problems"]:
        print(Problem(**problem))


def test_submission():
    params = {"handle": "Vicfred", "from": 1, "count": 10}
    r = requests.get("https://codeforces.com/api/user.status", params=params)
    assert r.status_code == 200
    json = r.json()
    assert json["status"] == "OK"
    result = json["result"]
    assert len(result) >= 1
    for submission in result:
        print(Submission(**submission))
