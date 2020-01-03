# -*- coding: utf-8 -*-
# @Time    : 2019/11/5 16:24
# @Author  : chenky
# @ProjectName :xiaMenWeb
# @FileName: loginPage.py
# @Software: PyCharm
import time
from selenium import webdriver

from public.Base import Base
from public.ReadYaml import ReadYamlUtils
from public.readConfig import PATH


class LoginPage(Base):
    _name = PATH("../element_data/ship_ticket.yml")
    _data = ReadYamlUtils(_name).read_data()["loginPage"]

    def input_user_name(self, username):
        self.send_keys(username, eval(self._data["user_name"]))

    def input_passwd(self, password):
        self.send_keys(password, eval(self._data["password"]))

    def click_login(self):
        self.click_element_by_css_js(eval(self._data["login"]))

    def get_error_passwd_info(self):
        text = self.find_element(eval(self._data["box_text"])).text
        if text is not None:
            return text

    def login_(self, username, password):
        self.input_user_name(username)
        self.input_passwd(password)
        self.click_login()

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("http://62.234.35.213:8080/cx/")
    a = LoginPage(driver)
    # a.input_user_name("admin")
    # a.input_passwd("Admin")
    a.login_("admin", "admin")
    print(a.get_error_passwd_info())
    time.sleep(10)
    driver.quit()
    pass