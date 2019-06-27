#!/usr/bin/python
# encoding:utf-8
'''
@author:ben
@contact:itliubin@163.com
@file:while-caishuzi.py
@date:2019/6/27_16:27

'''

# print "I am thinking of a number between 1 and 20"
# count = 0
# active = True
# while active:
#     num = raw_input("take a guess.")
#     num = int(num)
#     if num < 16:
#         print "Your guess is too low."
#         count += 1
#     elif num > 16:
#         print "Your guess is too high."
#         count += 1
#     elif num == 16:
#         count += 1
#         print " Good job! Your guess my number in " + str(count) + "  guesses!"
#         active = False
#

# This ia a guess the number game.
import random

secret_number = random.randint(1, 20)
print "I am thinking of a number between 1 and 20."

# Ask the player to guess 6 times.
for guesses_taken in range(1, 7):
    print "Take a guess."
    guess = int(raw_input())

    if guess < secret_number:
        print "Your guess is too low."
    elif guess > secret_number:
        print "Your guess is too high."
    elif guess == secret_number:
        print " Good job! Your guess my number in " + str(guesses_taken) + "  guesses!"
        break

print "Nope. The number I was thinking of was " + str(secret_number)

