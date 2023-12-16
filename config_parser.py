#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ------information ---------
# @Time: 2023-12-15 19:29
# @File: config_parser.py
# @Author: YeHwong
# @Email: 598318610@qq.com
# @Version ：1.0.0
import yaml


class ConfigParser:
    def __init__(self):
        self.cfg_dict = {}

    def load_cfg(self):
        with open('Config//test_cfg.yaml', encoding="utf-8") as f:
            self.cfg_dict = yaml.load(f, Loader=yaml.FullLoader)

    def get_command_list(self):
        dict_command_list = self.cfg_dict['Command_List']
        print(type(dict_command_list))

    def get_test_list(self):
        dict_test_list = self.cfg_dict['Test_List']
        print(type(dict_test_list))


if __name__ == '__main__':
    cfg_p = ConfigParser()
    cfg_p.load_cfg()
    cfg_p.get_command_list()
    cfg_p.get_test_list()