#!/usr/bin/python
# encoding:utf-8
'''
@author:ben
@contact:itliubin@163.com
@file:2.2.1.py
@date:2019/5/29_17:48

'''

# 面向测试的python 学习 2.2 循环 判断和 字符串函数

def f(n):
    if n <1:
        return  -1
    elif (n == 1) or (n == 2):
        return 1
    else:
        return f(n - 1) + f(n - 2)


print(f(3))
print(f(4))
print(f(5))
print(f(6))


# lambda
numbers = [1,2,3,4,5,6,7,8,9]
squares = map(lambda x: x * x,numbers)
print (list(squares))
