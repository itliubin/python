#!/usr/bin/python
# encoding:utf-8
'''
@author:ben
@contact:itliubin@163.com
@file:ex33-while.py
@date:2019/5/27_16:45

'''

i = 0
numbers = []
while i < 6:
    print "at the top i is %d" % i
    numbers.append(i)
    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d " % i

print "The numbers:"
for num in numbers:
    print num


animals = ["bear", "tiger", "penguin", "zebra"]
print "animals 0 is："
print animals[0]
print "animals 1 is："
print animals[1]
print "animals 2 is："
print animals[2]
print "animals 3 is："
print animals[3]


