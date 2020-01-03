# -*- coding: utf-8 -*-
# @Time    : 2019/6/17 15:24
# @Author  : chenky
# @ProjectName :project_script
# @FileName: test_Login.py
# @Software: PyCharm
import json
import unittest

from ddt import ddt, data, unpack

from CommonMethos.ExcelUtil import ExcelUtil
from CommonMethos.XiaMenTerminal import XiaMenTerminal


@ddt
class TestLogin(unittest.TestCase):
    __data = ExcelUtil("login.xlsx", 0).get_list_data()
    __server = XiaMenTerminal(host="http://118.89.216.229:19527")

    @data(*__data)
    def test_01(self, data1):
        print("当前测试的标题为----------%s"%data1["用例标题"])
        res = self.__server.api_login(data1["username"], data1["password"])
        result = None
        try:
            result = json.loads(res.text)
            assert result["msg"] == data1["expect(期望结果status)"]
            print(result)
        except Exception as e:
            self.fail("断言失败"+result["msg"]+"\n"+str(e))

    def test_02(self):
        """请求体为空时"""
        res = self.__server.api_login(index=0, username="1", password="2")
        print(res.text)

if __name__ == '__main__':
    unittest.main()
