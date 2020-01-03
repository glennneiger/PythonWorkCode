# -*- coding: utf-8 -*-
# @Time    : 2019/6/20 9:09
# @Author  : chenky
# @ProjectName :project_script
# @FileName: Config.py
# @Software: PyCharm


import configparser


class ConfigUtils(object):

    def __init__(self, configfile="config.ini"):
        self.config = configparser.ConfigParser()
        self.config.read(configfile, encoding="utf-8")

    def get_sections(self)->list:
        return self.config.sections()

    def get_options_by_sections(self, section):
        return self.config.options(section)

    def get_items_by_sections(self, section):
        return self.config.items(section)

    def get_value_by_section_and_option(self, section, option):
        return self.config.get(section, option)

    def __str__(self):
        return ""


def read_name():
    conf = configparser.ConfigParser()
    conf.read("./config.ini", encoding="utf-8")
    sections = conf.sections()
    return sections

if __name__ == '__main__':
    c = ConfigUtils("config.ini")
    print(c.get_options_by_sections("server"))
    print(c.get_value_by_section_and_option("server", "host"))

    aa = " 57549 root      20   0 3407040  59144  27472 S"
    print(aa.__len__())