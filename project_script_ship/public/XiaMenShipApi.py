# -*- coding: utf-8 -*-
# @Time    : 2019/7/4 15:56
# @Author  : chenky
# @ProjectName :project_script_ship
# @FileName: XiaMenShipApi.py
# @Software: PyCharm
import hashlib

import requests

from public.public_method import *


class XiaMenShipApi(object):
    __apiId = "111"
    __apiKey = "48d534fc6e7f451ca376baaa750729fc"
    __apiKey_window = "3a8a427582004ce7a30cadb3e13cf057"
    __session = requests.session()

    def __str__(self, *args, **kwargs):
        return "邮轮了旅客出行检票系统接口"

    def __init__(self, host):
        super().__init__()
        self.passenger_query_by_printer = host+"/api/v1/passenger/queryByPrinter"
        self.passenger_ticket_checking = host+"/api/v1/ticket/checking"
        self.passenger_ticket_checking_query = host+"/api/v1/ticket/checking/query"
        self.passenger_ticket_officeUpload = host+"/api/v1/ticket/officeUpload"
        self.passenger_info_new_add = host+"/api/v1/passenger/add"
        self.flight_info_add = host+"/api/v1/flight/add"

    @staticmethod
    def to_md5_str(md5_str: str)->str:
        m = hashlib.md5()
        m.update(md5_str.encode(encoding="utf-8"))
        str_encoding = m.hexdigest()
        return str_encoding

    @staticmethod
    def get_time_stamp():
        return str(round(time.time()*1000))

    @staticmethod
    def get_timestamp_mmss():
        return str(time.strftime("%Y%m%d%H%M%S", time.localtime(time.time())))

    @staticmethod
    def get_uuid():
        return str(uuid.uuid1()).replace("-", "")

    def get_header(self, sign: str, index=1)->dict:
        if index == 1:
            apikey = self.__apiKey
        else:
            apikey = self.__apiKey_window
        time_stamp = self.get_timestamp_mmss()
        header = {"content-type": "application/json;charset=utf-8",
                  "timestamp": time_stamp,
                  "sign": self.to_md5_str(sign+time_stamp+apikey),
                  "apiKey": apikey}
        # print(header["sign"])
        return header

    def api_flight_add(self, reqId="",
                       carrierCh="",
                       carrierEn="",
                       shipNameCh="",
                       shipNameEn="",
                       shipNo="",
                       sailDate="",
                       planArriveTime="",
                       startingPort="",
                       checkTime=""):
        """
        3.1 航班信息新增接口
        :param reqId:
        :param carrierCh:
        :param carrierEn:
        :param shipNameCh:
        :param shipNameEn:
        :param shipNo:
        :param sailDate:
        :param planArriveTime:
        :param startingPort:
        :param checkTime:
        :return:
        """
        body = {"reqId": reqId, "data":
            {"carrierCh": carrierCh,
             "carrierEn": carrierEn,
             "shipNameCh": shipNameCh,
             "shipNameEn": shipNameEn,
             "shipNo": shipNo,
             "sailDate": sailDate,
             "planArriveTime": planArriveTime,
             "startingPort": startingPort,
             "route": "厦门 - 大阪 - 釜山 - 厦门",
             "checkTime": checkTime}}
        try:
            res = self.__session.post(url=self.flight_info_add,
                                      json=body,
                                      headers=self.get_header("api/v1/flight/add"),
                                      verify=False)
            res.close()
            return res
        except Exception as e:
            return str(e)

    def api_passenger_info_new_add(self, reqId="",
                                   userId="",
                                   flightId="",
                                   groupNo="",
                                   passengerName="",
                                   birthDay="",
                                   passportID="",
                                   idNumber="",
                                   contact="",
                                   reserveNo="",
                                   floor="",
                                   roomNo="",
                                   memberLevel="",
                                   ticketType="",
                                   escapeArea=""):
        """
        3.5 旅客新增接口
        :param reqId:
        :param userId:
        :param flightId:
        :param groupNo:
        :param passengerName:
        :param birthDay:
        :param passportID:
        :param idNumber:
        :param contact:
        :param reserveNo:
        :param floor:
        :param checkDeviceNo:
        :param roomNo:
        :param memberLevel:
        :param ticketType:
        :param escapeArea:
        :return:
        """
        body = {"reqId": reqId, "datas": [
            {"userId": userId,
             "flightId": flightId,
             "groupNo": groupNo,
             "passengerName": passengerName,
             "sex": "F",
             "country": "中国",
             "birthDay": birthDay,
             "passportID": passportID,
             "passportValidity":"2020-01-01 09:11:00",
             "idNumber": idNumber,
             "contact": contact,
             "reserveNo": reserveNo,
             "floor": floor,
             "roomNo": roomNo,
             "memberLevel": memberLevel,
             "ticketType": ticketType,
             "escapeArea": escapeArea}]}
        try:
            res = self.__session.post(url=self.passenger_info_new_add,
                                      json=body,
                                      headers=self.get_header("api/v1/passenger/add"),
                                      verify=False)
            res.close()
            return res
        except Exception as e:
            return str(e)

    def api_passenger_query_by_printer(self, passportId="",
                                       idNumber="",
                                       sailDateSt="",
                                       sailDateEnd="",
                                       op=0,
                                       bodynew=None,
                                       reqId=PublicMethod.get_uuid()):
        """3.9 旅客凭证打印查询接口"""
        body = {"reqId": reqId,
                "condition": {"passportId": passportId,
                              "idNumber": idNumber,
                              "sailDateSt": sailDateSt,
                              "sailDateEnd": sailDateEnd}}
        if op == 1:
            body = bodynew
        try:
            res = self.__session.post(url=self.passenger_query_by_printer,
                                      json=body,
                                      headers=self.get_header("api/v1/passenger/queryByPrinter"),
                                      verify=False,
                                      timeout=10)
            res.close()
            return res
        except Exception as e:
            return str(e)
        finally:
            pass

    def api_passenger_ticket_checking(self, reqId="", userBarcode="", checkinId="", checkingTime="",checkDeviceNo="",
                                      op=0,
                                      bodynew=None):
        """3.11 旅客验票接口"""
        body = {"reqId": reqId,
                "data": {"checkinId": checkinId,
                         "userBarcode": userBarcode,
                         "checkingTime": checkingTime,
                         "checkDeviceNo": checkDeviceNo}
                }
        if op == 1:
            body = bodynew
        try:
            res = self.__session.post(url=self.passenger_ticket_checking,
                                      json=body,
                                      headers=self.get_header("api/v1/ticket/checking"),
                                      verify=False,
                                      timeout=10)
            res.close()
            return res
        except Exception as r:
            return str(r)

    def api_ticket_officeUpload(self,reqId="",
                                json_array=None):
        """
        3.12 旅客验票信息离线上传接口
        :param reqId:
        :param json_array:
        :return:
        """
        body = {"reqId": reqId,
                "datas": json_array}

        try:
            res = self.__session.post(url=self.passenger_ticket_officeUpload,
                                      json=body,
                                      headers=self.get_header("api/v1/ticket/officeUpload"),
                                      verify=False,
                                      timeout=10)
            res.close()
            return res
        except Exception as e:
            return str(e.__class__.__name__)+e.args[1]

    def api_passenger_ticket_checking_query(self,reqId="",
                                            pageIndex="",
                                            pageSize="",
                                            passengerName="",
                                            verifyResults="",
                                            passportId="",
                                            idNumber="",
                                            checkingTimeSt="",
                                            checkingTimeEnd="",
                                            op=0,
                                            bodynew=None):
        """
        3.13 查询旅客验票记录
        :param reqId:
        :param pageIndex:
        :param pageSize:
        :param passengerName:
        :param verifyResults:
        :param passportId:
        :param idNumber:
        :param checkingTimeSt:
        :param checkingTimeEnd:
        :return:
        """
        body = {"reqId": reqId,
                "pageIndex": pageIndex,
                "pageSize": pageSize,
                "condition": {"passengerName": passengerName,
                              "verifyResult": verifyResults,
                              "passportId": passportId,
                              "idNumber": idNumber,
                              "checkingTimeSt": checkingTimeSt,
                              "checkingTimeEnd": checkingTimeEnd}}
        if op == 1:
            body = bodynew
        try:
            # print(body)
            res = self.__session.post(url=self.passenger_ticket_checking_query,
                                      json=body,
                                      headers=self.get_header("api/v1/ticket/checking/query"),
                                      verify=False,
                                      timeout=10)
            res.close()
            return res
        except Exception as e:
            return str(e)

    def api_passenger_new_add(self):
        body = {"reqId": "11",
                "datas": []}
        res = self.__session.post(url=self.passenger_info_new_add,
                                  json=body,
                                  headers=self.get_header("api/v1/passenger/add"),
                                  verify=False,
                                  timeout=10)
        return res

if __name__ == '__main__':
    server = XiaMenShipApi(host="http://175.168.0.139:10020")
    print(XiaMenShipApi.to_md5_str('api/v1/passenger/queryByPrinter2019070818161648d534fc6e7f451ca376baaa750729fc'))
