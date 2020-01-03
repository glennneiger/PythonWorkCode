# -*- coding: utf-8 -*-
# @Time    : 2019/7/4 16:11
# @Author  : chenky
# @ProjectName :project_script_ship
# @FileName: public_method.py
# @Software: PyCharm
import os
import uuid
import sys

import time
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class PublicMethod(object):
    def __str__(self, *args, **kwargs):
        return super().__str__(*args, **kwargs)

    @staticmethod
    def __new__(cls, *more):
        return super().__new__(cls, *more)

    def __init__(self):
        super().__init__()

    def __delattr__(self, *args, **kwargs):
        return super().__delattr__(*args, **kwargs)

    @staticmethod
    def get_uuid():
        return str(uuid.uuid1()).replace("-", "")

    @staticmethod
    def get_time_stamp():
        return str(round(time.time()*1000))

    @staticmethod
    def get_time_format(_patten: str="%Y-%m-%d %H:%M:%S"):
        return str(time.strftime(_patten, time.localtime(time.time())))

if __name__ == '__main__':
    print(PublicMethod.get_uuid(), file=sys.stderr)
    print(uuid.uuid5(uuid.NAMESPACE_OID, ""))
    print(uuid.uuid3(uuid.NAMESPACE_OID, ""))
    print(PublicMethod.get_time_format())