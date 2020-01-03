# -*- coding: utf-8 -*-
# @Time    : 2019/7/19 13:55
# @Author  : chenky
# @ProjectName :XiaMenTerminalWeb
# @FileName: Base.py
# @Software: PyCharm
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from public.Log import MyLog
_log = MyLog("Base").logger


class Base(object):
    def __init__(self, driver_a: WebDriver):
        self.driver = driver_a
        self.timeout = 20
        self.t = 0.2
        super().__init__()

    def find_element(self, loc: tuple)->WebElement:
        """
        By WebElement and WebDriver to find and click the expected element ,
        if not found ,then return
        else return the Element Object
        :param loc:
        :return:
        """
        time.sleep(1)
        if not isinstance(loc, tuple):
            _log.info("loc input parameter error，must be tuple")
        else:
            try:
                _log.info("starting to located element：by--{}, label is：{}".format(loc[0], loc[1]))
                ele = WebDriverWait(self.driver, timeout=self.timeout, poll_frequency=self.t).until(
                    lambda k: k.find_element(*loc)
                )
                return ele
            except Exception as e:
                _log.error("located element error again，{}".format(str(e)))
                return None

    def click_element(self, loc: tuple):
        """
        By WebElement class to click Element
        if not found, logger error information
        :param loc:
        :return:
        """
        try:
            _log.info("starting to click element: {}".format(loc[1]))
            ele = self.find_element(loc)
            WebDriverWait(self.driver, self.timeout, poll_frequency=self.t).until(
                expected_conditions.element_to_be_clickable(loc)
            )
            current_located_style = loc[0]
            if current_located_style == "css selector":
                self.click_element_by_css_js(loc)
            ele.click()
        except Exception as e:
            _log.error("happened clicking element error:{}".format(str(e)))

    def click_element_by_css_js(self, loc: tuple):
        try:
            js = "document.querySelector('{}').click();".format(loc[1])
            print(js)
            self.driver.execute_script(js)
        except Exception as e:
            _log.error("JS click element error:{}".format(str(e)))

    def click_element_by_action(self, loc):
        try:
            _log.info("starting to click element: {}".format(loc[1]))
            ele = self.find_element(loc)
            WebDriverWait(self.driver, self.timeout, poll_frequency=self.t).until(
                expected_conditions.element_to_be_clickable(loc)
            )
            action = ActionChains(self.driver)
            action.click(ele).perform()
        except Exception as e:
            _log.error("happened action element error:{}".format(str(e)))

    def send_keys(self, message, loc):
        try:
            self.find_element(loc).send_keys(message)
            _log.info("input  '{}'  success".format(message))
        except Exception as e:
            _log.error("input happening error: {}".format(str(e)))

    def judge_if_exist_element(self, loc)->bool:
        try:
            _log.info("starting to judge element if the{} is exist".format(str(loc)))
            result = WebDriverWait(self.driver, timeout=2).until(lambda t: t.find_element(*loc))
            print("the element is exist")
            return True
        except Exception as e:
            _log.error("{}".format(str(e)))
            print("the element is not exist")
            return False

    def is_alert_exist(self):
        try:
            time.sleep(3)
            alert = self.driver.switch_to.alert
            text = alert.text
            alert.accept()  # 用alert 点alert
            return text
        except:
            return ""

if __name__ == '__main__':
    aa = str(round(time.time()*1000))
    print(aa)

    boat_plan = ("css selector", "#westnavtree_7_span")

    Base(webdriver.Firefox()).click_element_by_css_js(boat_plan)
    pass