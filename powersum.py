#!/usr/bin/python
#encoding:utf-8
'''
@author:ben
@contact:itliubin@163.com
@file:powersum.py
@date:2019/4/24_10:16

'''

def powersum(power, *args):
    '''return the sum of each argument raised to specified power'''
    total=0
    for i in args:
        total += pow(i, power)
    return total


powersum(2, 3, 4)
powersum(2, 10)




