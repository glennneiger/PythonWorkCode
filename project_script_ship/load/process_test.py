# -*- coding: utf-8 -*-
# @Time    : 2019/7/12 13:51
# @Author  : chenky
# @ProjectName :project_script_ship
# @FileName: process_test.py
# @Software: PyCharm
import json
import os

import time

from public.Config import ConfigUtils
from public.Log import Log
from public.XiaMenShipApi import XiaMenShipApi
from public.public_method import PublicMethod

_config = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "config/config.ini")
__config = ConfigUtils(configfile=_config)
__log = Log("process_test")
__server = XiaMenShipApi(host=__config.get_value_by_section_and_option("server", "host"))


def process_test():
    """对流程从-添加旅客信息->验票再进行查询进行全流程测试"""
    # 进行旅客信息添加
    a = 1
    while True:
        __log.info("开始进行第{}次流程".format(a))
        res = __server.api_passenger_info_new_add(reqId=PublicMethod.get_uuid(),
                                                  userId="userIdA00{}".format(a),
                                                  flightId="a027d0582e6842a59ab2f9eacd544213",
                                                  groupNo="groupNoA00{}".format(a),
                                                  passengerName="nameA{}".format(a),
                                                  birthDay=PublicMethod.get_time_format(),
                                                  passportID="passportIdA00{}".format(a),
                                                  idNumber="idNumberA00{}".format(a),
                                                  contact="contactA00{}".format(a),
                                                  reserveNo="reserverA00{}".format(a),
                                                  floor="floorA00{}".format(a),
                                                  roomNo="roomNoA00{}".format(a),
                                                  memberLevel="memberLevel",
                                                  ticketType="vipA00{}".format(a),
                                                  escapeArea="escapeAreaA00{}".format(a))
        userCode = ""
        try:
            dict_data = json.loads(res.text)
            userCode = dict_data["rows"][0]["userBarcode"]
            # __log.info("添加旅客信息+-----idNumberA00{}成功".format(a))
        except Exception as e:
            __log.error("添加旅客信息失败"+"\n"+str(e))
        time.sleep(0.2)

        # 进行验票
        res_a = __server.api_passenger_ticket_checking(reqId=PublicMethod.get_uuid(), userBarcode=userCode,
                                                       checkinId=PublicMethod.get_uuid(),
                                                       checkingTime=PublicMethod.get_time_format(),
                                                       checkDeviceNo="checkDeviceNo001")
        try:
            dict_data_a = json.loads(res_a.text)
            assert dict_data_a["verifyResult"] == 0
            # __log.info("验票旅客----idNumberA00{}成功".format(a))
        except Exception as e:
            __log.error("验票旅客----idNumberA00{}失败".format(a)+"\n"+str(e))
        time.sleep(0.3)

        # 进行查询
        try:
            res_b = __server.api_passenger_ticket_checking_query(reqId=PublicMethod.get_uuid(),
                                                                 pageIndex=0,
                                                                 pageSize=1,
                                                                 passportId="passportIdA00{}".format(a),
                                                                 checkingTimeSt="",
                                                                 checkingTimeEnd="")
            dict_data_b = json.loads(res_b.text)
            assert dict_data_b["rows"][0]["barcode"] == userCode
            # __log.info("查询旅客-----idNumberA00{}成功".format(a))
        except Exception as e:
           __log.error("查询旅客----idNumberA00{}失败".format(a)+"\n"+str(e))
        # __log.info("结束第{}次流程".format(a))
        a += 1
        time.sleep(0.3)
if __name__ == '__main__':
    process_test()