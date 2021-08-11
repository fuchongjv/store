from selenium import webdriver
import unittest
from InitPageData import InitPageData
from LoginPage import LoginPage
from ddt import ddt
from ddt import unpack
from ddt import data


@ddt
class TestLogin(unittest.TestCase):

    @data(*InitPageData.login_data_success)
    def testLoginSuccess(self, testdata):
        username = testdata["username"]
        password = testdata["password"]
        expect = testdata["expect"]

        # 执行登陆逻辑
        login = LoginPage(self.driver)

        login.login(username, password)

        result = login.get_login_success()

        self.assertEqual(result, expect)

    @data(*InitPageData.login_data_password_error)
    def testLoginError(self, testdata):
        username = testdata["username"]
        password = testdata["password"]
        expect = testdata["expect"]

        # 执行登陆逻辑
        login = LoginPage(self.driver)

        login.login(username, password)

        # 获取实际测试结果
        result = login.get_login_pwd_error()

        # 断言
        self.assertEqual(result, expect)

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()
