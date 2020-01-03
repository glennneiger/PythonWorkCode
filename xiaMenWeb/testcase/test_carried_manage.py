# -*- coding: utf-8 -*-
# @Time    : 2019/11/6 9:55
# @Author  : chenky
# @ProjectName :xiaMenWeb
# @FileName: test_carried_manage.py
# @Software: PyCharm


import unittest
from selenium import webdriver
import time
from pageObject.carriedManagePage import SystemManagePage


class TestCarriedManage(unittest.TestCase):
    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.driver.quit()

    def tearDown(self):
        super().tearDown()

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = webdriver.Firefox()
        cls.carried_page = SystemManagePage(cls.driver)
        cls.driver.get("http://62.234.35.213:8080/cx/")
        cls.carried_page.login_to_system_manage()

    def setUp(self):
        super().setUp()
        self.driver.get("http://62.234.35.213:8080/cx/")

    def test_01(self):
        """验证能正确添加承运人流程"""
        carried_name = str(round(time.time()))
        self.carried_page.click_system_manage()
        self.carried_page.click_carried_manage()
        self.carried_page.click_add_carried()
        self.carried_page.input_carried_name(carried_name)
        self.carried_page.input_carried_english_name(carried_name)
        self.carried_page.click_sure()

if __name__ == '__main__':
    unittest.main()
