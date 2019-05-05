# _*_ coding: utf_8 _*_
# @Time     : 2019/3/12
# @Author   : yuandian
# @Email    : 919839065@qq.com
# @file     : class_0312

import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

case_file = os.path.join(base_dir, 'API_1', 'python.xlsx')

sheet_file = os.path.join(base_dir, 'conf', 'changeSheet.cfg')

change_file = os.path.join(base_dir, 'conf', 'changeConf.cfg')

develop_file = os.path.join(base_dir, 'conf', 'develop.cfg')

test_file = os.path.join(base_dir, 'conf', 'test.cfg')

jdbc_file = os.path.join(base_dir, 'conf', 'jdbc.cfg')

log_conf_file = os.path.join(base_dir, 'conf', 'log_conf.cfg')

log_file = os.path.join(base_dir, 'log')