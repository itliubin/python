#!/usr/bin/python
#encoding:utf-8
'''
@author:ben
@contact:itliubin@163.com
@file:rasing.py.py
@date:2019/4/19_9:44

'''

class ShortInputException(Exception):
    '''a user-defined exception class.'''
    def __init__(self,length,atleast):
        Exception.__init__(self)
        self.length=length
        self.atleast=atleast

try:
    s=raw_input('Enter somthing-->')
    if len(s) < 3:
        raise ShortInputException(len(s),3)
except EOFError:
        print '\n why did you do an EOF on me ?'
except ShortInputException,x:
    print 'ShortInputException:The input was of length %d ,\
          was expecting at least %d ' % (x.length, x.atleast)
else:
    print 'No exception was raised'



