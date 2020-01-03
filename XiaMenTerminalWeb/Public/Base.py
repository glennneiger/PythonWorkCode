# -*- coding: utf-8 -*-
# @Time    : 2019/7/19 13:55
# @Author  : chenky
# @ProjectName :XiaMenTerminalWeb
# @FileName: Base.py
# @Software: PyCharm
import time
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Public import Log


class Base(object):
    """对selenium定位方法进行封装作为基类"""
    __log = Log.Log("Base")

    def __init__(self, driver_a: webdriver.Firefox):
        self.driver = driver_a
        self.timeout = 10
        self.t = 0.5
        super().__init__()

    def find_element(self, loc)->WebElement:
        if not isinstance(loc, tuple):
            self.__log.info("loc传入的参数错误，必须是元祖类型")
        else:
            try:
                self.__log.info("开始进行元素定位：定位方式为--{},定位元素标签为：   {}".format(loc[0], loc[1]))
                ele = WebDriverWait(self.driver, timeout=self.timeout, poll_frequency=self.t).until(
                    lambda t: t.find_element(*loc)
                )
                return ele
            except Exception as e:
                self.__log.error("定位元素时发生错误，{}".format(str(e)))
                return

    def click_element(self, loc):
        try:
            self.find_element(loc).click()
            self.__log.info("点击元素{}".format(loc[1]))
        except Exception as e:
            self.__log.error("点击元素发生错误{}".format(str(e)))

    def send_keys(self, message, loc):
        try:
            self.find_element(loc).send_keys(message)
            self.__log.info("输入{}成功".format(message))
        except Exception as e:
            self.__log.error("发生错误{}".format(str(e)))

    def judge_if_exist_element(self, loc)->bool:
        try:
            self.__log.info("开始判断元素{}是否存在".format(str(loc)))
            result = WebDriverWait(self.driver, timeout=2).until(lambda t: t.find_element(*loc))
            print("元素存在")
            return True
        except Exception as e:
            self.__log.error("{}".format(str(e)))
            print("元素不存在")
            return False

    def is_alert_exist(self):
        """判断alert是不是在"""
        try:
            time.sleep(3)
            alert = self.driver.switch_to.alert
            text = alert.text
            alert.accept()  # 用alert 点alert
            return text
        except:
            return ""

if __name__ == '__main__':
    pass