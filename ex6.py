#!/usr/bin/python
# encoding:utf-8
'''
@author:ben
@contact:itliubin@163.com
@file:ex6.py
@date:2019/4/24_17:32

'''

x = "there are %d types of people." %  10
binary = "binary"
do_not = "don't"
y = "those who know %s and those who %s." % (binary, do_not)
print x
print y

print "I said: %r." % x
print "I also said :%s." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string with a right side."
print w + e


