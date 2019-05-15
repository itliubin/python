#!/usr/bin/python
#encoding:utf-8
'''
@author:ben
@contact:itliubin@163.com
@file:inherit.py.py
@date:2019/4/17_16:39

'''
class SchoolMember:
    '''represents any school member.'''
    def __init__(self, name ,age):
        self.name=name
        self.age=age
        #print '(initalized schoolmember:%s)' % self.name
    def tell(self):
        '''tell my details.'''
        print 'name:% s ' %self.name
        print 'age:%s' % self.age
class Teacher(SchoolMember):
    '''a teacher'''
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary=salary
        #print '(initialized Teacher:%s)' % self.name
    def tell(self):
        SchoolMember.tell(self)
        print 'Salary:"%d"' % self.salary

class Student(SchoolMember):
    '''a student'''
    def __init__(self,name,age,marks):
        SchoolMember.__init__(self,name,age)
        self.marks=marks
        #print '(initialize studeng :%s)' %self.name
    def tell(self):
        SchoolMember.tell(self)
        print 'marks:"%d"' %self.marks
t=Teacher('mrs.shri',40,30000)
s=Student('swaroop',22,75)
print

members=[t,s]
for member in members:
    member.tell()




