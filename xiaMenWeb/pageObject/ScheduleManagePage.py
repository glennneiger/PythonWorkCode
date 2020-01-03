# -*- coding: utf-8 -*-
# @Time    : 2019/11/6 11:54
# @Author  : chenky
# @ProjectName :xiaMenWeb
# @FileName: ScheduleManagePage.py
# @Software: PyCharm
from element_data.scheduleManageElement import ScheduleManageElement
from public.Base import Base
from public.ReadYaml import ReadYamlUtils
from public.readConfig import PATH, ConfigUtils


class ScheduleManagePage(Base):
    ele = ScheduleManageElement()
    _name = PATH("../element_data/ship_ticket.yml")
    _data = ReadYamlUtils(_name).read_data()["scheduleManage"]
    _ini = ConfigUtils(PATH("../config/Web.ini"))

    def click_schedule_manage(self):
        self.click_element(eval(self._data["scheduleManage"]))

    def click_boat_manage(self):
        self.click_element(eval(self._data["boatManage"]))

    def click_add_boat(self):
        self.click_element(eval(self._data["addBoat"]))

    def input_boat_name(self, name):
        self.send_keys(name, eval(self._data["boatName"]))

    def input_boat_weight(self, weight):
        self.send_keys(weight, eval(self._data["boatWeight"]))

    def input_boat_length(self, length):
        self.send_keys(length, eval(self._data["boatLenght"]))

    def click_note1(self):
        self.click_element(eval(self._data["note1"]))

    def input_note2(self,note):
        self.send_keys(note, eval(self._data["note2"]))

    def click_sure(self):
        self.click_element(eval(self._data["sure"]))

    def click_ship_manage(self):
        self.click_element(eval(self._data["shipMange"]))

    def click_add_ship(self):
        self.click_element(eval(self._data["addShip"]))

    def input_ship_name(self, name):
        self.send_keys(name, eval(self._data["shipNameZh"]))

    def input_ship_name_en(self, name):
        self.send_keys(name, eval(self._data["shipNameEn"]))

    def input_ship_imo(self, imo):
        self.send_keys(imo, eval(self._data["shipImo"]))

    def input_ship_call_sign(self, call):
        self.send_keys(call, eval(self._data["shipCallSign"]))

    def input_ship_length(self,length):
        self.send_keys(length, eval(self._data["shipLength"]))

    def input_ship_width(self, width):
        self.send_keys(width, eval(self._data["shipWidth"]))

    def input_ship_height(self, height):
        self.send_keys(height, eval(self._data["shipHeight"]))

    def input_ship_grt(self, grt):
        self.send_keys(grt, eval(self._data["shipGrt"]))

    def input_ship_nrt(self, nrt):
        self.send_keys(nrt, eval(self._data["shipNrt"]))

    def input_ship_dwt(self, dwt):
        self.send_keys(dwt, eval(self._data["shipDwt"]))

    def input_shipExtreMedraft(self, shipExtreMedraft):
        self.send_keys(shipExtreMedraft, eval(self._data["shipExtreMedraft"]))

    def click_choose(self):
        self.click_element(eval(self._data["choose"]))

    def choose_Company(self):
        self.click_element(eval(self._data["chooseCompany"]))

    def click_date(self):
        self.click_element(eval(self._data["date"]))

    def click_right_date(self):
        self.click_element(eval(self._data["rightSure"]))

    def click_outSure(self):
        self.click_element(eval(self._data["outSure"]))

    def login(self):
        self.send_keys("admin", self._ini.get_value_by_section_and_option_tuple("login", "username"))
        self.send_keys("Admin", self._ini.get_value_by_section_and_option_tuple("login", "password"))
        self.click_element(self._ini.get_value_by_section_and_option_tuple("login", "login"))

    def click_boat_plan(self):
        self.click_element(self.ele.boat_plan)

    def click_add_boat_plan(self):
        self.click_element(self.ele.add_boat_plan_apply)

    def click_choose_ship(self):
        self.click_element(self.ele.click_choose_ship)

    def click_choose_base_ship(self, name):
        self.click_element_by_action(self.ele.get_choose_ship(name))

    def click_plan_near_boat_time(self):
        self.click_element(self.ele.plan_near_boat_time)

    def click_plan_near_boat_time_inner_sure(self):
        self.click_element(self.ele.click_plan_near_boat_time_sure)

    def click_plan_depart_time(self):
        self.click_element(self.ele.plan_planDepartTime)

    def click_plan_depart_time_inner_sure(self):
        self.click_element(self.ele.click_plan_planDepartTime_sure)

    def click_choose_near_boat(self):
        self.click_element(self.ele.click_choose_boat)

    def click_choose_base_boat(self, boat):
        self.click_element(self.ele.get_select_boat(boat))

    def input_person_number(self, number):
        self.send_keys(number, self.ele.person_number_capacity)

    def click_outSure_boat_plan(self):
        self.click_element(self.ele.click_out_sure)
if __name__ == '__main__':
    pass