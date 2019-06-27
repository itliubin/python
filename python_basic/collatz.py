#!/usr/bin/python
# encoding:utf-8
'''
@author:ben
@contact:itliubin@163.com
@file:collatz.py
@date:2019/6/27_17:06

'''


# def collatz(number):
#     if number % 2 == 0:
#         print number // 2
#         y = number
#         return y
#     else:
#         print number
#         y = 3 * number + 1
#         return y
#
#
# number = int(raw_input("输入一个数： "))
# collatz(number)
# collatz(collatz(number))
# collatz(collatz(collatz(number)))


def c(n):
    global A
    if n % 2 == 0:
        n = n // 2
        print(str(n))
    elif n % 2 == 1:
        n = 3 * n + 1
        print(str(n))
    A = n


while True:
    try:
        A = int(raw_input("输入一个大于1的整数"))
        while A > 1:
            c(A)
    except ValueError:
        print "数据类型不正确，请重新输入"
