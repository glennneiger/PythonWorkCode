# -*- coding: utf-8 -*-
# @Time    : 2019/7/19 15:42
# @Author  : chenky
# @ProjectName :XiaMenTerminalWeb
# @FileName: test_Login.py
# @Software: PyCharm
import unittest

import time
from selenium import webdriver

from PageObject.LoginPage import LoginPage


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver.get("http://175.168.0.139:10091")

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.login_page = LoginPage(cls.driver)
        super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def test_01(self):
        """正常登录"""
        self.login_page.input_user("admin")
        self.login_page.input_password("admin123456")
        self.login_page.click_login()
        self.login_page.click_quit_login()
        time.sleep(1)
        self.login_page.alert_or()
        self.login_page.click_quit_login()
        self.login_page.alert_or()
        self.login_page.alert_or()

    def test_02(self):
        """密码错误时"""
        self.login_page.input_user("admin")
        self.login_page.input_password("admin1234567")
        self.login_page.click_login()
        self.login_page.alert_or()

    def test_03(self):
        """用户名错误时"""
        self.login_page.input_user("a")
        self.login_page.input_password("admin123456")
        self.login_page.click_login()
        self.login_page.alert_or()

if __name__ == '__main__':
    unittest.main()
