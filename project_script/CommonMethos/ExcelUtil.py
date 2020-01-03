# -*- coding: utf-8 -*-
# @Time    : 2019/6/14 16:23
# @Author  : chenky
# @ProjectName :project_script
# @FileName: ExcelUtil.py
# @Software: PyCharm
import os

import xlrd


class ExcelUtil(object):
    __current_path = os.path.realpath(__file__)
    __case_excel_path = os.path.join(os.path.dirname(os.path.dirname(__current_path)), "case_excel/")

    def get_case_excel_path(self):
        return self.__case_excel_path

    def get_current_path(self):
        return self.__current_path

    def get_sheets_name(self):
        return self.book_instance.sheet_names()

    def __init__(self, excel_name: str,
                 sheet_index: int):
        super().__init__()
        self.book_instance = xlrd.open_workbook(self.__case_excel_path+excel_name)
        self.sheet_instance = self.book_instance.sheet_by_index(sheet_index)

    def get_rows(self):
        """
        获取总行数
        :return:
        """
        return self.sheet_instance.nrows

    def get_columns(self):
        """
        获取总列数
        :return:
        """
        return self.sheet_instance.ncols

    def get_list_data(self):
        keys = self.sheet_instance.row_values(0)  # 获取第一行的值作为keys
        data_list = []
        # 从第二行开始取测试数据的值
        for i in range(1, self.get_rows()):
            # 获得从第二行开始的值
            values = self.sheet_instance.row_values(i)
            data_dict = {}
            for k in range(0, len(keys)):
                data_dict[keys[k]] = values[k]
            data_list.append(data_dict)
        return data_list

if __name__ == '__main__':
    a = ExcelUtil("login.xlsx", 0)
    print(a.get_list_data())
    # a = "你的选择"
    # print("test{}{}".format(a, a))