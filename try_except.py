#!/usr/bin/python
#encoding:utf-8
'''
@author:ben
@contact:itliubin@163.com
@file:try_except.py
@date:2019/4/18_16:03

'''

import sys
try
    s = raw_input('enter something--->')
except EOFError:
    print '\n WHY did you do an EOF on me?'
    sys.exit()
except:
    print '\n some error/exception occurred.'

print 'done'

