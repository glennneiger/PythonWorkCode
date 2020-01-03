# -*- coding: utf-8 -*-
# @Time    : 2019/7/19 15:04
# @Author  : chenky
# @ProjectName :XiaMenTerminalWeb
# @FileName: LoginPage.py
# @Software: PyCharm
import time
from selenium import webdriver

from Public.Base import Base
from Public.Config import ConfigUtils
from Public.Log import PATH


class LoginPage(Base):
    __path = PATH("../Config/LoginConfig.ini")
    __LoginConfig = ConfigUtils(__path)

    def input_user(self, user):
        self.send_keys(loc=self.__LoginConfig.get_value_by_section_and_option_tuple("elements", "username"),
                       message=user)

    def input_password(self, password):
        self.send_keys(loc=self.__LoginConfig.get_value_by_section_and_option_tuple("elements", "password"),
                       message=password)

    def click_login(self):
        self.click_element(loc=self.__LoginConfig.get_value_by_section_and_option_tuple("elements", "login"))

    def click_quit_login(self):
        self.click_element(loc=self.__LoginConfig.get_value_by_section_and_option_tuple("elements", "quit"))

    def quit_or_begin(self):
        if self.judge_if_exist_element(loc=self.__LoginConfig.get_value_by_section_and_option_tuple("elements", "quit")):
            self.click_quit_login()
        else:
            pass

    def alert_or(self):
        if self.is_alert_exist():
            return True
        else:
            return False

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("http://175.168.0.139:10091")
    aa = LoginPage(driver)
    aa.input_user("admin")
    aa.input_password("admin123456")
    aa.click_login()
    time.sleep(10)
    driver.quit()
    pass