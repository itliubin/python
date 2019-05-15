#!/usr/bin/python
#encoding:utf-8
'''
@author:ben
@contact:itliubin@163.com
@file:pickling.py.py
@date:2019/4/18_15:44

'''
import cPickle as p
shoplist=['apple', 'mango', 'caarot']
shoplistfile='shoplist.data'
f=file(shoplistfile,'w')
p.dump(shoplist,f)
f.close()
del shoplist
f=file(shoplistfile)
storedlist=p.load(f)
print storedlist
