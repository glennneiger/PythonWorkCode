# -*- coding: utf-8 -*-
# @Time    : 2019/6/17 16:41
# @Author  : chenky
# @ProjectName :project_script
# @FileName: test_post_recognize.py
# @Software: PyCharm
import unittest

from ddt import *

from CommonMethos.ExcelUtil import ExcelUtil
from CommonMethos.Log import MyLog
from CommonMethos.XiaMenTerminal import XiaMenTerminal
from CommonMethos.common_method import *


@ddt
class TestPostRecognize(unittest.TestCase):
    __data = ExcelUtil("post_recognize.xlsx", 0).get_list_data()
    __server = XiaMenTerminal(host="http://118.89.216.229:19527")
    __log = MyLog("test_post_recognize").logger

    @data(*__data)
    def test_01(self, data1):
        self.__log.info("标题----%s" % data1["用例标题"])
        res = self.__server.api_post_recognize(UserId=data1["UserId"], Name=data1["Name"], Sex=data1["Sex"],
                                               LivePhoto=to_base64(shiwanli+"/"+"0.jpg"), UserPhoto=to_base64(shiwanli+"/"+"0.jpg"),
                                               IdentifiedResult=data1["IdentifiedResult"],
                                               score=data1["score"],
                                               RecognizeTime=get_time_mmss())
        json_data = None
        try:
            json_data = json.loads(res.text)
            self.assertEqual(json_data["msg"], data1["expect-msg"])
        except Exception as e:
            self.__log.error(str(data1)+"\n"+str(json_data))
            self.fail(str(e))

    def test_02(self):
        """验证请求体为空时服务器能正确响应"""
        res = self.__server.api_post_recognize(index=0)
        print(res.text)

if __name__ == '__main__':
    unittest.main()