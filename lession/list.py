#!/usr/bin/python
# encoding:utf-8
'''
@author:ben
@contact:itliubin@163.com
@file:list.py
@date:2019/4/30_14:45

'''

y = list()
y.append(1)
print y

x = [20,30,40]
print x
print x[0]

z = (2,3,4)
print z


def add(w, m):
    return w, m, w+m


print add(20, 30)
q = ("hello", "world", "python")

print q

print " ".join(q)
print ",".join(q)




