from codeforces.Methods import *


def test_user_info():
    users = user_info(["Vicfred", "Fefer_Ivan", "tourist", "rng_58"])
    for user in users:
        print(user)


test_user_info()
