import unittest
import os
from HTMLTestRunner import HTMLTestRunner

tests = unittest.defaultTestLoader.discover(os.getcwd(), "Test*.py")

f = open(file="登陆测试.html", mode="w+", encoding="utf-8")

runner = HTMLTestRunner.HTMLTestRunner(
    title="登陆详细报告",
    description="第一轮回归登陆测试",
    verbosity=1,
    stream=f
)

runner.run(tests)
