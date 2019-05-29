#!/usr/bin/python
# encoding:utf-8
'''
@author:ben
@contact:itliubin@163.com
@file:sunxu.py
@date:2019/5/23_13:49

'''

# 面向测试的python 学习： 循环判断

for i in range(1, 10, 1):
    print i,

print "\n"

for i in range(5):
    if i < 2:
        pass
    elif i < 4:
        print i
    else:
        print "i >4 ",
        print i


# 给默认参数的值后面的参数必须也有之，比如 add(x,y=100,z) 这种写法是错误的，
def add(x, y=100, z=200):
    return x + y + z


print (add(1, 2, 3))
print (add(1, 2))
print (add(1))
print (add(x=1, y=2, z=3))
print (add(x=1, y=10))


# 用* 来表示没有名字的可变数量的参数，** 表示带名字的可变数量的参数

def myfunc(x, y, *num):
    print (type(num))
    print (num)
    print (x, y, num)


myfunc(1, 2, 10, 9, 8)
myfunc(2, 3, 9, 8, 10, 11)


def myfunc2(**kv):  # k= keyword v= value
    print(type(kv))
    print(kv['name'])
    print(kv['city'])


myfunc2(name='tom', city='shanghai')


