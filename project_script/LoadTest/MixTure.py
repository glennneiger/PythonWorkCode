# -*- coding: utf-8 -*-
# @Time    : 2019/6/20 16:38
# @Author  : chenky
# @ProjectName :project_script
# @FileName: MixTure.py
# @Software: PyCharm
import json
import os

from locust import TaskSequence, HttpLocust, task, log

from CommonMethos.XiaMenTerminal import XiaMenTerminal
from CommonMethos.common_method import *
from config.Config import ConfigUtils


class MyTask(TaskSequence):
    path = "C:/chenkeyun/InnerTest/集装箱码头/project_script/config"
    a = ConfigUtils(path+"/config.ini")
    __server = XiaMenTerminal(host=a.get_value_by_section_and_option("server", "host"))

    @task
    def first_task_login(self):
        body = {"reqId": get_uuid(),
                "username": "admin",
                "password": "admin123456"}
        with self.client.post(url="/api/v1/login",
                              headers=self.__server.get_headers("/api/v1/login"),
                              json=body,
                              verify=False,
                              catch_response=True) as response:
            try:
                json_data = json.loads(str(response.text))
                assert json_data["msg"] == "登录成功"
                response.success()
            except Exception as e:
                response.failure(str(e)+str("失败"))

    @task
    def second_task_post_recognize(self):
        body = {"reqId": get_uuid(),
                "UserId": "testuserId",
                "Name": "testname",
                "Sex": "男",
                "LivePhoto": to_base64(shiwanli+"/"+"0.jpg"),
                "UserPhoto": to_base64(shiwanli+"/"+"0.jpg"),
                "IdentifiedResult": "1",
                "score": "0.9512154",
                "RecognizeTime": get_time_mmss()}
        with self.client.post(url="/api/v1/face/recognize",
                              headers=self.__server.get_headers("/api/v1/face/recognize"),
                              json=body,
                              verify=False,
                              catch_response=True) as response:
            try:
                dict_data = json.loads(str(response.text))
                assert dict_data["msg"] == "上传成功"
                response.success()
            except Exception as e:
                response.failure(str(e)+"failed!")

    @task
    def third_task_recognize(self):
        body = {"reqId": get_uuid(),
                "starttime": "20190618052211",
                "endtime": "20190619052211",
                "name": "",
                "IdentifiedResult": "1",
                "pageSize": 1,
                "pageIndex": 1}
        with self.client.post(url="/api/v1/query/recognize/record",
                              headers=self.__server.get_headers("/api/v1/query/recognize/record"),
                              json=body,
                              verify=False,
                              catch_response=True) as response:
            try:
                dict_data = json.loads(str(response.text))
                assert dict_data["msg"] == "查询成功"
                response.success()
            except Exception as e:
                response.failure(str(e)+"failed!")

    @task
    def fourth_task_statistical(self):
        body = {"reqId": get_uuid(),
                "starttime": "20190618052211",
                "endtime": "20190619052211"}
        with self.client.post(url="/api/v1/customer/statistics",
                              headers=self.__server.get_headers("/api/v1/customer/statistics"),
                              json=body,
                              verify=False,
                              catch_response=True) as response:
            try:
                dict_data = json.loads(str(response.text))
                assert dict_data["msg"] == "查询成功"
                response.success()
            except Exception as e:
                response.failure(str(e)+"failed!")


class MyH(HttpLocust):
    task_set = MyTask
    min_wait = 300
    max_wait = 6000
    host = "http://118.89.216.229:19527"

if __name__ == '__main__':
    command1 = "c:"
    command2 = r"cd C:/chenkeyun/InnerTest/集装箱码头/project_script/LoadTest"
    command3 = r"locust -f MixTure.py --web-host=127.0.0.1"
    os.system(command1)
    os.system(command2)
    os.system(command3)