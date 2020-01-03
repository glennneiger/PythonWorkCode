# -*- coding: utf-8 -*-
# @Time    : 2019/7/8 9:43
# @Author  : chenky
# @ProjectName :project_script_ship
# @FileName: test_passenger_officeUpload.py.py
# @Software: PyCharm
import unittest
import sys
from ddt import *
import os

from public.Config import ConfigUtils
from public.Log import Log
from public.XiaMenShipApi import XiaMenShipApi
from public.public_method import PublicMethod


class TestPassengerOfficeUpLoad(unittest.TestCase):
    config = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "config/config.ini")
    __config = ConfigUtils(configfile=config)
    __log = Log("test_passenger_officeUpload")
    __server = XiaMenShipApi(host=__config.get_value_by_section_and_option("server", "host"))

    def tearDown(self):
        super().tearDown()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def setUp(self):
        super().setUp()

    def test_01(self):
        a = 2
        json_array = []
        info_1 = {"checkinId": PublicMethod.get_uuid(),
                  "userBarcode": "",
                  "checkingTime": "",
                  "checkDeviceNo": ""}
        for i in range(0, a):
            info = {"checkinId": PublicMethod.get_uuid(),
                    "userBarcode": "000000000006",
                    "checkingTime": PublicMethod.get_time_format(),
                    "checkDeviceNo": "device_id1"}
            json_array.append(info)
        try:
            res = self.__server.api_ticket_officeUpload(reqId="uuid32位", json_array=json_array)
            self.__log.info(res.text)
        except Exception as e:
            self.__log.error(str(e))

if __name__ == '__main__':
    unittest.main()