#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2020/8/31 21:59
# @Author  : 雪成
# @Software: PyCharm
import requests
import pytest
import allure
from api.loginApi import MtxLogin
from tools.analyse_data import parse_data


class TestLogin:
    def setup_class(self):
        self.session = requests.Session()
        self.login_obj = MtxLogin()

    @allure.title("测试登录成功的正向用例")
    def test_login_success(self):
        resp_login = self.login_obj.login_success(self.session)
        # print(resp_login.json())
        assert resp_login.json().get('msg') == '登录成功'

    @pytest.mark.parametrize('value', parse_data('mtx_Login', 'test_login'))
    @allure.title("测试登录逆向用例")
    def test_login_error(self, value):
        data = {'accounts': value['accounts'], 'pwd': value['pwd']}
        resp_login = self.login_obj.login(self.session, data)
        assert resp_login.json().get('msg') == value['exp']
