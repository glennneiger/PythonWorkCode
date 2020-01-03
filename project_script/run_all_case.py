# -*- coding: utf-8 -*-
# @Time    : 2019/6/20 9:54
# @Author  : chenky
# @ProjectName :project_script
# @FileName: run_all_case.py
# @Software: PyCharm
import os
import unittest

from CommonMethos import HTMLTestRunner_cn


def add_all_case(case_dir: str):
    current_path = os.path.realpath(__file__)
    parent_path = os.path.dirname(current_path)
    case_dirname = os.path.join(parent_path, case_dir)
    discover_case = unittest.defaultTestLoader.discover(start_dir=case_dirname, pattern="test*.py")
    return discover_case


def run_all_case(discover_case, report_name: str)->None:
    current_path = os.path.realpath(os.path.dirname(__file__))
    report = os.path.join(current_path, "TestResultReport/"+report_name+".html")
    fp = open(report, "wb")
    runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
                                              verbosity=2,
                                              title=u"接口自动化测试报告",
                                              description=u"测试用例执行如下",
                                             )
    runner.run(discover_case)
    fp.close()

if __name__ == '__main__':
    aa = add_all_case("TestCase")
    # print(aa)
    run_all_case(aa, "report")
    pass