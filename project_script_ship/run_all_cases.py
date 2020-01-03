# -*- coding: utf-8 -*-
# @Time    : 2019/7/5 17:03
# @Author  : chenky
# @ProjectName :project_script_ship
# @FileName: run_all_cases.py
# @Software: PyCharm
import os
import unittest

from public import HTMLTestRunner_cn
from BeautifulReport import BeautifulReport


def add_case(rule: str):
    case_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "case_code")
    discover = unittest.defaultTestLoader.discover(start_dir=case_path,
                                                   pattern=rule)
    return discover


def add_test_result(result_name: str, unittest_suit: unittest.suite.TestSuite)->None:
    result_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "result")
    f = open(result_path+result_name, "wb")
    run = HTMLTestRunner_cn.HTMLTestRunner(stream=f,
                                           description="详细测试结果",
                                           title="厦门邮轮旅客出行平台接口测试")
    run.run(unittest_suit)
    f.close()


def run_beautiful_report(discover):
    BeautifulReport(suites=discover).report(description="厦门邮轮旅客出行平台接口",
                                            filename="result",
                                            log_path="./result")


if __name__ == '__main__':
    a = add_case(rule="test*.py")
    run_beautiful_report(a)