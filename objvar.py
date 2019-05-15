#!/usr/bin/python
#encoding:utf-8
'''
@author:ben
@contact:itliubin@163.com
@file:objvar.py.py
@date:2019/4/16 17:27
'''

class Person:
    ''' Represents a person.'''
    population = 0
    def __init__( self ,name ):
        '''initializes the person's data.'''
        self.name=name
        print'(initializing %s)' % self.name
        Person.population += 1
    def __del__(self):
        '''i am dying'''
        print "%s says bye." % self.name
        Person.population -= 1
        if Person.population == 0 :
            print 'i am the last one.'
        else:
            print 'There are still % d people left.' % Person.population
    def sayHi(self):
        '''greeting by persion.
        really ,that's all it does.
        '''
        print 'hi,my name is %s .' % self.name
    def howMany(self):
        '''Prints the current population.'''
        if Person.population == 1:
            print 'i am the only person here.'
        else:
            print 'we have  % d persons here.' % Person.population

swaroop=Person('swaroop')
swaroop.sayHi()
swaroop.howMany()

kalam=Person('abdul kalam')
kalam.sayHi()
kalam.howMany()

swaroop.sayHi()
swaroop.howMany()



