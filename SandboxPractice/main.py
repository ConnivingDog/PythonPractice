#!/bin/python3

import os
import sys
from practice import Practice

Practice.Greet()

#Odd or Even Guesser
x = input('Enter a number : ')

if Practice.OddEven(x) == True:
    print('even')
else:
    print('odd')

#Swapper

x = input('enter number x : ')
y = input('enter number y : ')

print('Pre-Swap : {} & {}'.format(x,y))
print('Post-Swap : {} & {}'.format(Practice.Swapper(x,y),Practice.Swapper(y,x)))

#Sum of Digits

x = input("enter a number : ")

print('sum : {}'.format(Practice.SumOfDigits(x)))

#Reverser

x = input("enter a number : ")

print('Reversed number : {}'.format(Practice.Reverser(x)))
