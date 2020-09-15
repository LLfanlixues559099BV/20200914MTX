#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2020/8/31 21:48
# @Author  : 雪成
# @Software: PyCharm
from config import IP, HEADERS


class MtxLogin:
    def __init__(self):
        self.url = IP + "/mtx/index.php?s=/index/user/login.html"

    def login(self, session, data):
        resp_login = session.post(self.url, data=data, headers=HEADERS)
        return resp_login

    def login_success(self, session):
        """
        登录成功的请求
        :return:
        :session:
        """
        data = {'accounts': 'fanxuecheng', 'pwd': 'fxc123456'}
        resp_login = session.post(self.url, data=data, headers=HEADERS)
        return resp_login
