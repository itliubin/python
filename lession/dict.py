#!/usr/bin/python
# encoding:utf-8
'''
@author:ben
@contact:itliubin@163.com
@file:dict.py
@date:2019/4/30_15:09

'''

list=[2,3]
#hash(list)
char = "hello world"
print hash(char)


dicttest = {"name": "zhangsan", "age": 20, "gender": "m"}

print dicttest

dicttest2=dict(name="lisi",age=25,gender="m")
print dicttest2

print 'loc' in dicttest2

for (k, v) in dicttest2.items():
    print k+'='+str(v)

print dicttest2.keys()

print dicttest2.get('loc', None)
print dicttest2.setdefault('loc', 'default')
