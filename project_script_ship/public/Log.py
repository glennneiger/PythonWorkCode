# -*- coding: utf-8 -*-
# @Time    : 2019/7/4 17:16
# @Author  : chenky
# @ProjectName :project_script_ship
# @FileName: Log.py
# @Software: PyCharm
import os
import logging


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
log_path = PATH("../logs")


class Log(object):
    def __init__(self, name):
        self.logname = os.path.join(log_path, name+".log")
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - - %(message)s")

    def output(self, level, message):
        """
        :param level: 日志等级
        :param message: 日志需要打印的信息
        :return:
        """

        # send logging output to a disk file
        fh = logging.FileHandler(self.logname, 'a', encoding="utf-8")
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # send logging output to streams
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warn':
            self.logger.warn(message)
        elif level == 'error':
            self.logger.error(message)

        # 防止重复打印
        self.logger.removeHandler(fh)
        self.logger.removeHandler(ch)
        fh.close()

    def info(self, message):
        self.output('info', message)

    def debug(self, message):
        self.output('debug', message)

    def warn(self, message):
        self.output('warn', message)

    def error(self, message):
        self.output('error', message)

if __name__ == '__main__':
    pass