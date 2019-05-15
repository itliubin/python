#!/usr/bin/python
#encoding:utf-8
'''
@author:ben
@contact:itliubin@163.com
@file:lambda.py
@date:2019/4/24_10:33

'''

def make_repeater(n):
    return lambda s: s*n

twice= make_repeater(10)
print twice('*')
