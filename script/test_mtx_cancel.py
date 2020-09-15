#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2020/9/4 0:30
# @Author  : 雪成
# @Software: PyCharm
import requests
import allure
from api.enshrineApi import Enshrine
from api.loginApi import MtxLogin
from tools.logger import GetLog

log = GetLog.get_logger()


class TestCancel:
    def setup_class(self):
        self.session = requests.Session()
        self.cancel_obj = Enshrine()
        MtxLogin().login_success(self.session)

    @allure.feature('测试用例取消收藏与收藏成功')
    @allure.title("测试取消收藏与收藏成功功能")
    @allure.story('正向测试用例')
    def test_cancel(self):
        """
        如果获取到status的值==1则断言是否收藏成功否则断言是否取消成功
        :return: 1==收藏成功 or 0 == 取消成功
        """
        response_cancel = self.cancel_obj.cancel(self.session)
        res = response_cancel.json()
        status = res['data']['status']
        if status == 1:
            assert response_cancel.json().get('msg') == "收藏成功"
            log.info(f"参数为{res},获取到的msg的值为: {response_cancel.json().get('msg')}")
        else:
            assert response_cancel.json().get('msg') == "取消成功"
            log.info(f"参数为{res},获取到的msg的值为: {response_cancel.json().get('msg')}")
