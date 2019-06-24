#!/usr/bin/python
# encoding:utf-8
'''
@author:ben
@contact:itliubin@163.com
@file:mpl_squares.py
@date:2019/6/24_12:02

'''

import matplotlib.pyplot as plt

# input_value = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]
# plt.plot(input_value, squares, linewidth=5)
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
# plt.tick_params(axis='both', labelsize=14)
#
# plt.show()

# 使用scagter() 绘制散点图

# plt.scatter(2, 4, s=200)
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
plt.scatter(x_values, y_values, s=200)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)
plt.tick_params(axis="both", which='major', labelsize=14)
# plt.show()

# 保存图片,使用保存图片，就不能在使用plt.show()了，否则生成的数据无法保存到图片上
# plt.savefig("squares_polt.png", bbox_inches='tight')
plt.savefig("squares_polt.png")


