#!/usr/bin/python
# encoding:utf-8
'''
@author:ben
@contact:itliubin@163.com
@file:ex44.py
@date:2019/5/30_16:48

'''

# 类的继承

class Parent(object):
    def override(self):
        print "PARENT override()"

    def implicit(self):
        print "Parent implicit()"

    def altered(self):
        print "Parent altered()"


class Child(Parent):
    def override(self):
        print "CHILD override()"

    def altered(self):
        print "Child ,before parent altered()"
        super(Child, self).altered()
        print "Child,after parent altered()"


dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()






