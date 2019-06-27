#!/usr/bin/python
# encoding:utf-8
'''
@author:ben
@contact:itliubin@163.com
@file:ex14.py
@date:2019/5/5_10:46

'''

from sys import argv
script, user_name = argv
prompt = '>'
print "hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s" % user_name
likes = raw_input(prompt)

print "Where do you live %s " % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright ,so you said %r about liking me.
You LIVE IN %r .Not sure where that is.
And you have a %r computer.Nice.
""" % (likes, lives, computer)
