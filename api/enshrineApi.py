#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2020/9/4 0:25
# @Author  : 雪成
# @Software: PyCharm

import config


class Enshrine:
    def __init__(self):
        self.url = config.IP + "/mtx/index.php?s=/index/userfavor/cancel.html"

    def cancel(self, session):
        """
        调用取消收藏
        :param session:
        :return:
        """

        data = {'id': 4}
        res_cancel = session.post(self.url, data=data, headers=config.HEADERS)
        print(res_cancel)
        return res_cancel
