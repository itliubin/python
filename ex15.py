#!/usr/bin/python
# encoding:utf-8
'''
@author:ben
@contact:itliubin@163.com
@file:ex15.py
@date:2019/5/5_11:49

'''

from sys import argv
script, filename = argv
txt = open(filename)
print "Here's your file %r:" % filename
print txt.read()
txt.close()
print "Type the filename again:"
file_again = raw_input(">")
txt_again = open(file_again)
print txt_again.read()
txt_again.close()


