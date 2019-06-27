#!/usr/bin/python
# encoding:utf-8
'''
@author:ben
@contact:itliubin@163.com
@file:ex39.py
@date:2019/5/28_17:40

'''


class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line


happy_bday = Song(["happy birthday to you", "I don't want to get sued", "So i'll stop right there"])

bulls_on_parade = Song(["They rally around the family","With pockets full of shells"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
