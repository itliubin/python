#!/usr/bin/python
#encoding:utf-8
'''
@author:ben
@contact:itliubin@163.com
@file:finally.py.py
@date:2019/4/19_10:32

'''

import time
try:
    f=file('poem.txt')
    while True:
        line=f.readline()
        if len(line)==0:
            break
        time.sleep(2)
        print line,
finally:
    f.close()
    print 'cleaning up... closed the file'




