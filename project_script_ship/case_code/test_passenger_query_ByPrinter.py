# -*- coding: utf-8 -*-
# @Time    : 2019/7/5 11:28
# @Author  : chenky
# @ProjectName :project_script_ship
# @FileName: test_passenger_query_ByPrinter.py
# @Software: PyCharm
import unittest

import sys
from ddt import *
import os

from public.Config import ConfigUtils
from public.Log import Log
from public.ReadYaml import ReadYaml
from public.XiaMenShipApi import XiaMenShipApi


@ddt
class TestPassengerByPrinter(unittest.TestCase):
    yaml_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "yaml_case_file/")
    config = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "config/config.ini")
    __config = ConfigUtils(configfile=config)
    __data = ReadYaml(yaml_path+"test.yaml").all_data()
    __log = Log("test_passenger_query_ByPrinter")
    __server = XiaMenShipApi(host=__config.get_value_by_section_and_option("server", "host"))

    def __init__(self, methodName='runTest'):
        super().__init__(methodName)

    def setUp(self):
        super().setUp()

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def __str__(self):
        return super().__str__()

    def tearDown(self):
        super().tearDown()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    # @file_data(path+"test.yaml")

    @data(*__data)
    @unpack
    def test_01(self, **value):
        self.__log.info("开始进行测试"+"   "+value["casetitle"])
        try:
            res = self.__server.api_passenger_query_by_printer(op=1, bodynew=value["body"])
            dict_data = json.loads(res.text)
            self.assertEqual(dict_data["status"], value["expect"])
            self.__log.info("用例{}执行成功".format(value["casetitle"])+"\n"+str(value["body"]))
        except Exception as e:
            print(res.text, file=sys.stderr)
            self.__log.error("用例{}执行失败，失败的原因为{}".format(value["casetitle"], str(e))+"\n"+res.text)
            self.fail()

    def test_02(self):
        try:
            res = self.__server.api_passenger_query_by_printer(passportId="passportId1", idNumber="500238199312134390",
                                                               sailDateSt="", sailDateEnd="2019-07-08 17:09:20")
            print(res.text)
        except Exception as e:
            print(e.__class__.__name__)

    def test_03(self):
        print(type(self.__config.get_value_by_section_and_option("server", "host")))
if __name__ == '__main__':
    unittest.main()
