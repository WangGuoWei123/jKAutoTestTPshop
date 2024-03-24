"""
具体接口访问功能
"""

from app import BASE_URL
from tools.utils import MakeSession


class VerifyCodeApi(object):
    def __init__(self):
        """获取session对象"""
        self.session = MakeSession.make_session()
        # print(self.session)
        self.url = "?m=Home&c=User&a=verify"

    def get_verify_code(self):
        """获取响应对象"""
        self.session.get(BASE_URL + self.url)


class LoginApi(object):
    def __init__(self, username, password, verify_code):
        self.session = MakeSession.make_session()
        # print(self.session)
        self.url = "?m=Home&c=User&a=do_login"
        self.myLoginData = {"username": username,
                            "password": password,
                            "verify_code": verify_code}

    def post_login(self):
        return self.session.post(BASE_URL + self.url, data=self.myLoginData)


class OrderApi(object):
    def __init__(self):
        self.session = MakeSession.make_session()
        # print(self.session)
        self.url = "http://127.0.0.1/Home/Order/order_list.html"

    def my_order(self):
        return self.session.get(self.url)
