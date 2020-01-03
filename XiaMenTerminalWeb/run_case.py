# -*- coding: utf-8 -*-
# @Time    : 2019/7/19 17:51
# @Author  : chenky
# @ProjectName :XiaMenTerminalWeb
# @FileName: run_case.py
# @Software: PyCharm


import unittest
import os

from BeautifulReport import BeautifulReport

from Public.Log import PATH


def discover_case(rule="test*.py"):
    case_path = PATH("../Case")
    discover = unittest.defaultTestLoader.discover(start_dir=case_path,pattern=rule)
    return discover


def main(discover):
    BeautifulReport(suites=discover).report(description="厦门码头web平台自动化测试",
                                            filename="report",
                                            log_path="./ResultReport")
if __name__ == '__main__':
    discover_ = discover_case()
    main(discover_)
