# -*- coding: utf-8 -*-
# @Time    : 2019/6/20 9:09
# @Author  : chenky
# @ProjectName :project_script
# @FileName: readConfig.py
# @Software: PyCharm


import configparser
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class ConfigUtils(object):

    def __init__(self, configfile):
        self.config = configparser.ConfigParser()
        self.config.read(configfile, encoding="utf-8")

    def get_sections(self)->list:
        return self.config.sections()

    def get_options_by_sections(self, section):
        return self.config.options(section)

    def get_items_by_sections(self, section):
        return self.config.items(section)

    def get_value_by_section_and_option_tuple(self, section, option, rule=0):
        if rule == 0:
            try:
                tuple_obj = eval(self.config.get(section, option))
                return tuple_obj
            except Exception as e:
                return str(e)
        else:
            return self.config.get(section, option)

    def __str__(self):
        return ""


def read_name():
    conf = configparser.ConfigParser()
    conf.read("./Config.ini", encoding="utf-8")
    sections = conf.sections()
    return sections

if __name__ == '__main__':
    config_path = PATH("../Config/LoginConfig.ini")
    c = ConfigUtils(config_path)
    print(c.get_value_by_section_and_option_tuple("elements", "username"))
    print(type(c.get_value_by_section_and_option_tuple("elements", "username")))