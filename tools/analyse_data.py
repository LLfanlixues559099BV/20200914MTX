#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2020/9/3 0:10
# @Author  : 雪成
# @Software: PyCharm
import yaml
import config


def parse_data(filename, key):
    """
    读取 data目录下 mtx_login.yml 文件
    :param filename: mtx_login.yml
    :param key: mtx_login.yml 文件中的 test_login
    :return: 列表嵌套字典 格式的数据
    """

    with open(file=config.DIR_NAME + '/data/%s.yml' % filename, mode='r', encoding='utf-8') as f:
        # print(config.DIR_NAME)
        yaml_login_data = yaml.load(f, Loader=yaml.FullLoader)
        temp = list()
        data_list = yaml_login_data.get(key)
        for val in data_list.values():
            temp.append(val)
        return temp


if __name__ == '__main__':
    data = parse_data('mtx_login', 'test_login')
    print(data)
