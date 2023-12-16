#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ------information ---------
# @Time: 2023-12-15 19:13
# @File: main.py
# @Author: YeHwong
# @Email: 598318610@qq.com
# @Version ：1.0.0
from log_set import Logger

test_logger = Logger(base_dir='./TEST_LOG', level='info').my_logger


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
