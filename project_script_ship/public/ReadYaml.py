# -*- coding: utf-8 -*-
# @Time    : 2019/7/4 17:54
# @Author  : chenky
# @ProjectName :project_script_ship
# @FileName: ReadYaml.py
# @Software: PyCharm
import yaml

from public.Log import Log


class ReadYaml(object):
    __log = Log("ReadYaml")

    def __init__(self, filename):
        self.path = filename

    def get_yaml(self):
        """
        读取yaml文件
        :return:
        """
        try:
            f = open(self.path, encoding="utf-8")
            data = yaml.load(f, Loader=yaml.FullLoader)
            f.close()
            # print(type(data))
            return data
        except Exception as e:
            return str(e.__class__.__name__)+" "+e.args[1]

    def all_data(self):
        data = self.get_yaml()
        try:

            if not isinstance(data, list):
                return list(data)
            elif not isinstance(data, dict):
                return data
        except Exception as e:
            self.__log.error(str(e))
            return


if __name__ == '__main__':
    path = "../yaml_case_file/"
    a = ReadYaml(path+"test.yaml")
    print(a.all_data())