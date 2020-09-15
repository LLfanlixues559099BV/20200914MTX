#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2020/9/5 18:35
# @Author  : 雪成
# @Software: PyCharm
import requests
import allure
from api.payorder import PayOrder
from api.loginApi import MtxLogin
from api.loginOder import LoginOder


class TestPayOrder:
    def setup_class(self):
        self.session = requests.Session()
        self.pay_obj = PayOrder()
        MtxLogin().login_success(self.session)

    @allure.title("测试支付成功功能")
    def test_pay_order(self):
        LoginOder().order(self.session)
        res_pay = self.pay_obj.pay_order(self.session)
        assert "支付成功" in res_pay.text
