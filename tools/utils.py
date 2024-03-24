"""工具文件"""
import requests


import json

from app import BASE_DIR


class MakeSession(object):
    session = None
    pring("测试下")
    @classmethod
    def make_session(cls):
        if cls.session is None:
            cls.session = requests.Session()
        return cls.session


# print(BASE_DIR)
def log_data():
    login_datas = []
    with open(BASE_DIR + "/data/login_data.json", encoding="utf-8") as f:
        data = json.load(f)

        for k, v in data.items():
            login_datas.append((v.get('username'),
                                v.get('password'),
                                v.get('verify_code'),
                                v.get('msg')))

    return login_datas
