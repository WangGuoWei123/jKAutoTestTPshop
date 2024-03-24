"""
测试用例
"""
import unittest

from parameterized import parameterized

from api.tp_api import VerifyCodeApi, LoginApi, OrderApi
from tools.utils import *


class LoginTest(unittest.TestCase):
    """登录"""

    session = None

    @classmethod
    def setUpClass(cls):
        cls.session = MakeSession.make_session()

    def setUp(self):
        VerifyCodeApi().get_verify_code()

    @classmethod
    def tearDown(cls):
        # self.verify_code.session.close()
        cls.session.close()

    @parameterized.expand(log_data)
    def test_login(self, username, password, verify_code, msg):

        login = LoginApi(username, password, verify_code)
        response = login.post_login()
        # logging.warning("测试登录")
        try:
            self.assertIn(msg, response.json().get("msg"))
        except AssertionError as e:
            raise e


class OrderTest(unittest.TestCase):
    """订单"""

    def setUp(self):
        self.session = MakeSession.make_session()
        # logging.warning(self.session)

    def tearDown(self):
        self.session.close()

    def test_order(self):
        order = OrderApi()
        self.response = order.my_order()
        try:
            self.assertIn("我的订单", self.response.text)
        except AssertionError as e:
            raise e
