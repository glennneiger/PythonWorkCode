# -*- coding: utf-8 -*-
# @Time    : 2019/6/14 10:08
# @Author  : chenky
# @ProjectName :project_script
# @FileName: XiaMenTerminal.py
# @Software: PyCharm

from CommonMethos.common_method import *


class XiaMenTerminal(object):
    __apiId = "123"
    __apiKey = "123"

    def __init__(self, host):
        self.host = host
        self.post_recognize_info = self.host+"/api/v1/face/recognize"
        self.login = self.host+"/api/v1/login"
        self.query_record = self.host+"/api/v1/query/recognize/record"
        self.customer_statistical = self.host+"/api/v1/customer/statistics"

    def get_headers(self, sign: str):
        """
        获取api header
        :param sign:
        :return:
        """
        time_stamp = get_time_stamp()
        header = {"apiId": self.__apiId, "sign": to_md5_str(sign+time_stamp+self.__apiKey),
                  "timestamp": time_stamp}
        return header

    def api_post_recognize(self, UserId="",
                           Name="", Sex="", LivePhoto="", UserPhoto="", IdentifiedResult="", score="", RecognizeTime="",index=1):
        """
        识别成功，发送识别成功的用户信息；识别未成功发送top1的识别分数与信息
        IdentifiedResult
        1，成功识别；2，陌生人；3，已经识别陌生人
        :return:
        """
        body = {"reqId": get_uuid(),
                "UserId": UserId,
                "Name": Name,
                "Sex": Sex,
                "LivePhoto": LivePhoto,
                "UserPhoto": UserPhoto,
                "IdentifiedResult": IdentifiedResult,
                "score": score,
                "RecognizeTime": RecognizeTime}
        if index == 0:
            body = None
        res = requests.post(url=self.post_recognize_info, headers=self.get_headers("/api/v1/face/recognize"),
                            json=body,
                            verify=False)
        res.close()
        return res

    def api_login(self, username, password,index=1):
        """用户登录"""
        body = {"reqId": get_uuid(),
                "username": username,
                "password": password}
        if index == 0:
            body = None
        res = requests.post(self.login, headers=self.get_headers("/api/v1/login"),
                            json=body,
                            verify=False)
        res.close()
        return res

    def api_query_record(self, starttime="",
                         endtime="",
                         name="",
                         IdentifiedResult="",
                         pageSize="",
                         pageIndex="",
                         reqId=get_uuid()):
        """识别结果查询"""
        body = {"reqId": get_uuid(),
                "starttime": starttime,
                "endtime": endtime,
                "name": name,
                "IdentifiedResult": IdentifiedResult,
                "pageSize": pageSize,
                "pageIndex": pageIndex}
        res = requests.post(self.query_record, headers=self.get_headers("/api/v1/query/recognize/record"),
                            json=body,
                            verify=False)
        res.close()
        return res

    def api_customer_statistical(self, starttime="",
                                 endtime="",
                                 reqId=get_uuid(),):
        """识别结果统计接口"""
        body = {"reqId": reqId,
                "starttime": starttime,
                "endtime": endtime}
        res = requests.post(self.customer_statistical, headers=self.get_headers("/api/v1/customer/statistics"),
                            json=body,
                            verify=False)
        res.close()
        return res

if __name__ == '__main__':
    a = "int"
    print(type(eval(a)))
    print(eval(a))
    xx = XiaMenTerminal(host="http://192.168.5.140:8889")
    res = xx.api_customer_statistical()
    print(res.text)
    print("")

