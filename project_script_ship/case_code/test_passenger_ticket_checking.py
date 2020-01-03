# -*- coding: utf-8 -*-
# @Time    : 2019/7/5 16:18
# @Author  : chenky
# @ProjectName :project_script_ship
# @FileName: test_passenger_ticket_checking.py
# @Software: PyCharm


import unittest

import sys
from ddt import *
import os

from public.Config import ConfigUtils
from public.Log import Log
from public.ReadYaml import ReadYaml
from public.XiaMenShipApi import XiaMenShipApi
from public.public_method import PublicMethod


@ddt
class TestPassengerTicketChecking(unittest.TestCase):
    __yaml_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "yaml_case_file/")
    config = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "config/config.ini")
    __data = ReadYaml(__yaml_path+"passenger_ticket_checking.yaml").all_data()
    __config = ConfigUtils(configfile=config)
    __log = Log("test_passenger_ticket_checking")
    __server = XiaMenShipApi(host=__config.get_value_by_section_and_option("server", "host"))

    def setUp(self):
        super().setUp()

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def tearDown(self):
        super().tearDown()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def __init__(self, methodName='runTest'):
        super().__init__(methodName)

    def __str__(self):
        return super().__str__()

    @data(*__data)
    @unpack
    def test_01(self, **value):
        self.__log.info("开始进行测试"+"   "+value["casetitle"])
        try:
            res = self.__server.api_passenger_ticket_checking(op=1, bodynew=value["body"])
            dict_data = json.loads(res.text)
            self.assertEqual(dict_data["status"], value["expect"])
            self.__log.info("用例{}执行成功".format(value["casetitle"]))
        except Exception as e:
            print(res, file=sys.stderr)
            self.__log.error("用例{}执行失败，失败的原因为{}".format(value["casetitle"], str(e)))
            self.fail()

    def test_02(self):
        try:
            res = self.__server.api_passenger_ticket_checking(reqId="1645", userBarcode="userBarcode001",
                                                              checkinId="1125", checkingTime=PublicMethod.get_time_format(),
                                                              checkDeviceNo="testNo001")
            print(res.text)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    unittest.main()