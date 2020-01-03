# -*- coding: utf-8 -*-
# @Time    : 2019/11/5 17:31
# @Author  : chenky
# @ProjectName :xiaMenWeb
# @FileName: test_login.py
# @Software: PyCharm
import unittest
from selenium import webdriver

from pageObject.loginPage import LoginPage


class TestLogin(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.driver.get("http://62.234.35.213:8080/cx/")

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = webdriver.Firefox()
        cls.login_page = LoginPage(cls.driver)

    def tearDown(self):
        super().tearDown()
        self.driver.delete_all_cookies()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.driver.quit()

    def test_01(self):
        """验证能正确登录"""
        self.login_page.input_user_name("admin")
        self.login_page.input_passwd("Admin")
        self.login_page.click_login()

    def test_02(self):
        """密码错误时不能正确登录"""
        self.login_page.input_user_name("admin")
        self.login_page.input_passwd("dmin")
        self.login_page.click_login()
        self.assertEqual("帐号或密码不正确！", self.login_page.get_error_passwd_info())

if __name__ == '__main__':
    unittest.main()
