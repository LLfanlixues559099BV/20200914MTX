#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2020/9/3 23:44
# @Author  : 雪成
# @Software: PyCharm
import config
from config import IP, HEADERS
from tools.logger import GetLog

log = GetLog().get_logger()

class LoginOder:
    def __init__(self):
        self.url = IP + '/mtx/index.php?s=/index/buy/add.html'

    def order(self, session):
        data = {
            'goods_id': 4,
            'buy_type': 'goods',
            'stock': 1,
            'spec': '',
            'address_id': 1155,
            'payment_id': 1,
            'site_model': 0
        }

        response = session.post(self.url, data=data, headers=HEADERS)
        config.JUMP_URL = response.json().get('data').get('jump_url')
        # log.info(f"=====config.JUMP_URL的值是{config.JUMP_URL}=======")
        return response
