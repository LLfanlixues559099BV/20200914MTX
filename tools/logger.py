#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2020/9/3 0:34
# @Author  : 雪成
# @Software: PyCharm
import logging.handlers
import config


class GetLog:
    logger = None

    @classmethod
    def get_logger(cls):
        if cls.logger is None:
            # 获取日志器(日记本)
            cls.logger = logging.getLogger()
            # 给日志器设置总的级别,级别是封装在logging里面
            cls.logger.setLevel(logging.INFO)
            fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
            fm = logging.Formatter(fmt)
            # 3.获取处理器  按时间切割的文件处理器工作中用midnight  ,backupCount=3  除了原件，只保存最新的三个
            tf = logging.handlers.TimedRotatingFileHandler(filename=config.DIR_NAME + '/logger/test.log',
                                                           when='H',
                                                           interval=1,
                                                           backupCount=3,
                                                           encoding='utf-8')

            ch = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            tf.setLevel(logging.DEBUG)

            # 在处理器中添加格式器
            tf.setFormatter(fm)
            tf.setFormatter(formatter)
            # 在日志器中添加处理器
            cls.logger.addHandler(tf)
            cls.logger.addHandler(ch)
        return cls.logger

