#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2020/9/4 0:00
# @Author  : 雪成
# @Software: PyCharm
import requests
import allure
from api.loginOder import LoginOder
from api.loginApi import MtxLogin


class TestOrder:
    def setup_class(self):
        self.session = requests.Session()
        self.order = LoginOder()
        MtxLogin().login_success(self.session)

    @allure.title("测试下订单功能")
    def test_order(self):
        res_order = self.order.order(self.session)
        assert res_order.json().get('msg') == "提交成功"
