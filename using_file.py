#!/usr/bin/python
#encoding:utf-8
'''
@author:ben
@contact:itliubin@163.com
@file:using_file.py.py
@date:2019/4/18_11:41

'''

poem = '''
programming is fun
when the work is done
if you waanna make your work aslo fun:
     use python!
'''
f = file('poem.txt', 'w')
f.write(poem)
f.close()

f=file('poem.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print line ,
f.close()


