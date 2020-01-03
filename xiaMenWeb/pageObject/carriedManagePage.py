# -*- coding: utf-8 -*-
# @Time    : 2019/11/6 9:48
# @Author  : chenky
# @ProjectName :xiaMenWeb
# @FileName: carriedManagePage.py
# @Software: PyCharm


from public.Base import Base
from public.ReadYaml import ReadYamlUtils
from public.readConfig import PATH, ConfigUtils


class SystemManagePage(Base):
    _name = PATH("../element_data/ship_ticket.yml")
    _data = ReadYamlUtils(_name).read_data()["systemManage"]
    _ini = ConfigUtils(PATH("../config/Web.ini"))

    def click_system_manage(self):
        self.click_element(eval(self._data["systemManage"]))

    def click_carried_manage(self):
        self.click_element(eval(self._data["carried_manage"]))

    def click_add_carried(self):
        self.click_element(eval(self._data["add_carried_person"]))

    def input_carried_name(self, name):
        self.send_keys(name, eval(self._data["input_carried_name"]))

    def input_carried_english_name(self, name):
        self.send_keys(name, eval(self._data["input_carried_english_name"]))

    def click_sure(self):
        self.click_element(eval(self._data["click_sure"]))

    def login_to_system_manage(self):
        self.send_keys("admin", self._ini.get_value_by_section_and_option_tuple("login", "username"))
        self.send_keys("Admin", self._ini.get_value_by_section_and_option_tuple("login", "password"))
        self.click_element(self._ini.get_value_by_section_and_option_tuple("login", "login"))


if __name__ == '__main__':
    pass