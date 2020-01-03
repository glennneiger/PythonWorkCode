# -*- coding: utf-8 -*-
# @Time    : 2019/6/19 15:27
# @Author  : chenky
# @ProjectName :project_script
# @FileName: test_query_recognize_record.py
# @Software: PyCharm

import json
import unittest

from ddt import ddt, data, unpack

from CommonMethos.ExcelUtil import ExcelUtil
from CommonMethos.XiaMenTerminal import XiaMenTerminal
from CommonMethos.Log import MyLog


@ddt
class TestLogin(unittest.TestCase):
    __data = ExcelUtil("query_recognize_record.xlsx", 0).get_list_data()
    __server = XiaMenTerminal(host="http://118.89.216.229:19527")
    __log = MyLog("test_query_recognize_record").logger

    @data(*__data)
    def test_01(self, data1):
        self.__log.info("测试标题为:"+data1["用例标题"])
        res = self.__server.api_query_record(reqId=data1["reqId"],
                                             starttime=data1["starttime"], endtime=data1["endtime"],
                                             name=data1["name"],
                                             IdentifiedResult=data1["IdentifiedResult"],
                                             pageSize=data1["pageSize"],
                                             pageIndex=data1["pageIndex"])
        json_data = None
        try:
            json_data = json.loads(res.text)
            self.assertEqual(json_data["msg"], data1["expect"])
            print(json_data)
        except Exception as e:
            self.__log.error(str(json_data)+"\n"+str(data1))
            self.fail(str(e))

    def test_02_01(self):
        """对查询数据进行测试"""
        res = self.__server.api_query_record(starttime="20190517002322", endtime="20190626162322",
                                             name="",
                                             IdentifiedResult=None,
                                             pageSize=5,
                                             pageIndex=20)
        print(res.content.__len__())

if __name__ == '__main__':
    unittest.main()

