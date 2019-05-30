#!/usr/bin/python
# encoding:utf-8
'''
@author:ben
@contact:itliubin@163.com
@file:ex41-1.py
@date:2019/5/30_15:47

'''


# Animal is-a object (yes,sort of confusing) look at the extra credit
class Animal(object):
    def __init__(self, leg):
        self.leg = leg



# # ??
class Dog(Animal):
    def __init__(self, name):
        # # ??
        self.name = name
        self.leg = 4


class Cat(Animal):
    def __init__(self, name):
        self.name = name


class Persion(object):
    def __init__(self, name):
        self.name = name
        # person has-a pet of some kind
        self.pet = None


class Employee(Persion):
    def __init__(self, name, salary):
        self.salary = salary
        super(Employee, self).__init__(name)


class Fish(object):
    pass


class Salmon(Fish):
    pass


class Halibut(Fish):
    pass


# rover is-a dog
rover = Dog("Rosver")
print rover.leg
satan = Cat("Satan")
mary = Persion("Mary")


