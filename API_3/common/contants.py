# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function： 
"""
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # API_3
print(base_dir)

case_file = os.path.join(base_dir, 'data', 'cases.xlsx')
print(case_file)
