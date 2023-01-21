# -*- coding:utf-8 -*-
# @Time     :2022/6/2 15:04
# @Author   :CHNJX
# @File     :logger_utils.py


import logging
import os
import sys
import time
from logging.handlers import TimedRotatingFileHandler


class LoggerUtils:
    workdir = os.path.split(os.path.realpath(__file__))[0]

    @classmethod
    def get_logger(cls, name, package_name):
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        time_format = '%Y%m%d'
        now_string = time.strftime(time_format, time.localtime(time.time()))
        file_name = 'log_{}.log'.format(now_string)
        # os.chdir(workdir)
        root_path = os.path.abspath(
            os.path.join(cls.workdir, ".."))
        _folder_path = os.path.join(root_path, package_name)
        if not os.path.exists(_folder_path):
            os.mkdir(_folder_path)
        file_path = os.path.join(_folder_path, file_name)
        t = int(time.time())
        if TimedRotatingFileHandler(file_path).when.startswith('D') and time.localtime(t).tm_mday == time.localtime(
                TimedRotatingFileHandler(file_path).rolloverAt).tm_mday:
            return 1
        else:
            pass

        # FileHandler
        fh = logging.FileHandler(file_path, mode='a', encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            '******%(asctime)s - %(name)s - %(filename)s,line %(lineno)s - %(levelname)s: %(message)s')
        fh.setFormatter(formatter)

        sh = logging.StreamHandler(sys.stdout)
        sh.setFormatter(formatter)
        sh.setLevel(logging.DEBUG)
        logger.addHandler(fh)
        logger.addHandler(sh)
        # logger.addHandler(uh)

        return logger
