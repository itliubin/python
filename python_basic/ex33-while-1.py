#!/usr/bin/python
# encoding:utf-8
'''
@author:ben
@contact:itliubin@163.com
@file:ex33-while-1.py
@date:2019/5/27_17:13

'''


def while_num(x):
    i = 0
    numbers = []
    while i < x:
        print "at the top i is %d" % i
        numbers.append(i)
        i = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d " % i


y = int(raw_input("input a number:"))
while_num(y)




