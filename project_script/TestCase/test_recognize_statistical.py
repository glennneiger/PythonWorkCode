# -*- coding: utf-8 -*-
# @Time    : 2019/6/19 17:38
# @Author  : chenky
# @ProjectName :project_script
# @FileName: test_recognize_statistical.py
# @Software: PyCharm


import json
import unittest

from ddt import ddt, data, unpack

from CommonMethos.ExcelUtil import ExcelUtil
from CommonMethos.XiaMenTerminal import XiaMenTerminal
from CommonMethos.Log import MyLog
from config.Config import ConfigUtils


@ddt
class TestLogin(unittest.TestCase):
    a = ConfigUtils()
    __data = ExcelUtil("recognize_statistical.xlsx", 0).get_list_data()
    __server = XiaMenTerminal(host="http://118.89.216.229:19527")
    __log = MyLog("test_recognize_statistical").logger

    @data(*__data)
    def test_01(self, data1):
        print(data1)
        self.__log.info("测试标题为:" + data1["用例名称"])
        res = self.__server.api_customer_statistical(starttime=data1["starttime"], endtime=data1["endtime"],
                                                     reqId=data1["reqId"])
        try:
            json_data = json.loads(res.text)
            print(json_data)
        except Exception as e:
            self.fail(str(e)+str(res.text))

    def test_02(self):
        res = self.__server.api_customer_statistical(starttime="20180517002322", endtime="20190617002322")
        print(res.text)
if __name__ == '__main__':
    unittest.main()