# -*- coding: utf-8 -*-
# @Time    : 2019/11/6 12:02
# @Author  : chenky
# @ProjectName :xiaMenWeb
# @FileName: test_schedule_manage_boat.py
# @Software: PyCharm


import unittest
from selenium import webdriver
import time
from pageObject.ScheduleManagePage import ScheduleManagePage


class TestScheduleMange(unittest.TestCase):
    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.driver.quit()

    def tearDown(self):
        super().tearDown()
        time.sleep(1)

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.name = str(round(time.time()))
        cls.driver = webdriver.Firefox()
        cls.page = ScheduleManagePage(cls.driver)
        cls.driver.get("http://62.234.35.213:8080/cx/")
        cls.page.login()

    def setUp(self):
        super().setUp()
        self.driver.get("http://62.234.35.213:8080/cx/")
        time.sleep(2)
        self.page.click_schedule_manage()

    def test_01(self):
        """测试能够正常添加泊位"""
        self.page.click_boat_manage()
        self.page.click_add_boat()
        self.page.input_boat_name(self.name)
        self.page.input_boat_weight(100)
        self.page.input_boat_length(100)
        self.page.click_note1()
        self.page.input_note2("test")
        self.page.click_sure()

    def test_02(self):
        """验证能正确添加船舶"""
        self.page.click_ship_manage()
        self.page.click_add_ship()
        self.page.input_ship_name(self.name)
        self.page.input_ship_name_en(self.name)
        self.page.input_ship_imo(self.name)
        self.page.input_ship_call_sign(self.name)
        self.page.input_ship_length(100)
        self.page.input_ship_width(100)
        self.page.input_ship_height(100)
        self.page.input_ship_grt(10)
        self.page.input_ship_nrt(10)
        self.page.input_ship_dwt(10)
        self.page.input_shipExtreMedraft(100)
        self.page.click_choose()
        self.page.choose_Company()
        self.page.click_date()
        self.page.click_right_date()
        self.page.click_outSure()

    def test_03(self):
        """验证能正确添加靠离泊计划"""
        self.page.click_boat_plan()
        self.page.click_add_boat_plan()
        self.page.click_choose_ship()
        self.page.click_choose_base_ship(self.name)
        self.page.click_plan_near_boat_time()
        self.page.click_plan_near_boat_time_inner_sure()
        self.page.click_plan_depart_time()
        self.page.click_plan_depart_time_inner_sure()
        self.page.click_choose_near_boat()
        self.page.click_choose_base_boat(self.name)
        self.page.input_person_number(100)
        self.page.click_outSure_boat_plan()
if __name__ == '__main__':
    unittest.main()

