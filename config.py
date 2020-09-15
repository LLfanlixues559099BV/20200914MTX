#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2020/8/31 21:51
# @Author  : 雪成
# @Software: PyCharm
import os

HEADERS = {'X-Requested-With': 'XMLHttpRequest'}
IP = 'http://121.42.15.146:9090'
ABS_PATH = os.path.abspath(__file__)
DIR_NAME = os.path.dirname(ABS_PATH)
JUMP_URL = None
