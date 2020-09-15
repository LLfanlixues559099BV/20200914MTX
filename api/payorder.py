#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2020/9/5 18:29
# @Author  : 雪成
# @Software: PyCharm
import config


class PayOrder:
    def __init__(self):
        self.url = config.JUMP_URL

    def pay_order(self, session):
        # 对接口进行重定向 allow_redirects = False
        res_pay_order = session.get(self.url, allow_redirects=False)
        resp_pay = session.get(res_pay_order.headers['Location'])
        return resp_pay
