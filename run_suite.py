import unittest

import time

from case.tp_case import LoginTest, OrderTest
from tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()
# suite.addTest(unittest.makeSuite(VerifyCodeTest))
suite.addTest(unittest.makeSuite(LoginTest))
suite.addTest(unittest.makeSuite(OrderTest))
# unittest.TextTestRunner().run(suite)
with open("./report/" + time.strftime("%Y%m%d %H%M%S") +  ".html","wb") as f:
    # 使用 HTMLTestRunner 要运行测试套件，将结果写入文件流
    runner = HTMLTestRunner(f,title="我的测试报告",description="测试TPShop登录接口")
    runner.run(suite)