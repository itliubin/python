#!/usr/bin/python
# encoding:utf-8
'''
@author:ben
@contact:itliubin@163.com
@file:ex32.py
@date:2019/5/24_17:17

'''

the_count = [1, 2, 3, 4, 5]
fruits = ["apples", "orangles", "pears", "apricots"]
change = [1, "pennies", 2, "dimes", 3, "quarters"]

# this first kind of for-loop goes through a list for number in the_count:
for number in the_count:
    print "This is count %d " % number

for fruit in fruits:
    print "A fruit of type: %s " % fruit

# also we can go through mixed lists too notice we have to use %r since we don't know what's in it for i in change:
for i in change:
    print "I got %r " % i

# we can also build lists,first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0,6 ):
    print "Adding %d to the list."  % i
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print "Element was:  %d" % i


