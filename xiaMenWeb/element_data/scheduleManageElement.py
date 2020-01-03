# -*- coding: utf-8 -*-
# @Time    : 2019/11/7 17:03
# @Author  : chenky
# @ProjectName :xiaMenWeb
# @FileName: scheduleManageElement.py
# @Software: PyCharm


# noinspection PyRedundantParentheses
class ScheduleManageElement():
    boat_plan = ("css selector", "#westnavtree_7_span")
    add_boat_plan_apply = {"xpath", "//div[@class='funcbtngroup']/button[text()='新增靠离泊申请']"}
    click_choose_ship = ("css selector", "select[name='shipId']")

    @staticmethod
    def get_choose_ship(value):
        """
        动态返回选择具体的公司
        :param value:
        :return:
        """
        return ("xpath", "//select[@name='shipId']/option[text()='{}']".format(value))

    plan_near_boat_time = ("css selector", "input[name='planArriveTime']")
    click_plan_near_boat_time_sure = ("css selector", "div[x-placement='bottom-start']>div:nth-child(2)>button")
    plan_planDepartTime = ("css selector", "input[name='planDepartTime']")
    click_plan_planDepartTime_sure = click_plan_near_boat_time_sure
    click_choose_boat = ("css selector", "select[name='berthId']")

    @staticmethod
    def get_select_boat(boat):
        return ("xpath", "//select[@name='berthId']/option[text()='{}']".format(boat))

    person_number_capacity = ("css selector", "input[name='capacity']")
    click_add = ("css selector", "img[src='cx/dispatch/31_03.png']")
    click_out_sure = ("css selector", "div.modal-footer>button:nth-child(1)")
if __name__ == '__main__':
    print(ScheduleManageElement.get_choose_ship("node"))