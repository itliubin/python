#!/usr/bin/python
#encoding:utf-8
'''
@author:ben
@contact:itliubin@163.com
@file:cat.py.py
@date:2019/4/23_10:58

'''

import sys
def readfile(filename):
    '''  print file to the standard output '''
    f = file(filename)
    while True:
        line=f.readline()
        if len(line) == 0:
            break
        print line, #notice comma
    f.close()
#script starts from here
if len(sys.argv)<2:
    print 'no action specified.'
    sys.exit()
if sys.argv[1].startswith('--'):
    option=sys.argv[1][2:]
    #fetch sys.argv[1] but without the first two characters
    if option=='version':
        print 'version 1.2'
    elif option == 'help':
        print '''\
        this program prints files to the standard output.
        any number of files can be specified.
        OPtions include:
        --version: prints the version number
        --help: display this help
        '''
    else:
        print 'unkonwn option.'
    sys.exit()
else:
    for filename in sys.argv[1:]:
        readfile(filename)
