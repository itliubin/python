#!/usr/bin/python
# encoding:utf-8
'''
@author:ben
@contact:itliubin@163.com
@file:fuhao.py
@date:2019/5/23_11:04

'''

# **  表示乘方

# // 表示结果向下取整

print (100 // 7)
print (2 ** 8)

# type() 显示类型
x = 123456.789
print (type(x))

# dir() 查看当前对象的方法

print (dir(x))

#

print ('%s, %d, %.2f' % ('str', 20, 40.123))

print ("%s，%d") % ('stt2', 20)

# 去掉空格 lstrip() rsstrip() strip()
# upper()  lower() ;capitalize()
# split()
s = "abc, def, ghi"
ss = s.split(",")
print (ss)
rs = '-'.join(ss)
print (rs)

print (int("123"))
print (float("1234.56"))

s = '''
x = 1
y = 2
z = x + y
'''
exec(s)
print(z)
