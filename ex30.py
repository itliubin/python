#!/usr/bin/python
# encoding:utf-8
'''
@author:ben
@contact:itliubin@163.com
@file:ex30.py
@date:2019/5/24_16:10

'''

people = 30
cars = 40
buses = 15


if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we cloud take the buses."
else:
    print "We still can't decice."

if people > buses:
    print "Alright,let's just take the buses."
else:
    print "Fine,let's stay home then."