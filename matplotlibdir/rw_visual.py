#!/usr/bin/python
# encoding:utf-8
'''
@author:ben
@contact:itliubin@163.com
@file:rw_visual.py
@date:2019/6/24_16:45

'''

import matplotlib.pyplot as plt
from random_walk import RandomWalk

# rw = RandomWalk()
# rw.fill_walk()
# plt.scatter(rw.x_value, rw.y_value, s=15)
# plt.show()

while True:
    rw = RandomWalk()
    rw.fill_walk()
    plt.scatter(rw.x_value, rw.y_value, s=15)
    plt.show()

    keep_running = raw_input("Make another walk?(y/n):")
    if keep_running == 'n':
        break
    if keep_running == 'y':
        continue



