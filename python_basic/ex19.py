#!/usr/bin/python
# encoding:utf-8
'''
@author:ben
@contact:itliubin@163.com
@file:ex19.py
@date:2019/5/5_17:54

'''

def cheese_and_crackers(cheesed_count, boxes_of_crackers):
    print "You have %d cheese!" % cheesed_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "OR,we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two,variables and match:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)




