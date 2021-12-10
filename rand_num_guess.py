#!/usr/bin/env python3
# Created by: Zack isingoma
# Created on: Dec 9th , 2021
# This program makes users guess a random number


import random

hidden = random.randint(1, 10)
# print hidden

guess = int(input("Guess a number between 1 and 10: "))

if guess == hidden:
    print("Well done")
if guess != hidden:
    print("OOh so close")

print("The correct number was")
print(hidden)