#!/bin/python3

import os
import sys
import time
from practice import Practice

#Odd or Even Guesser
def OddEven():
    x = input('Enter a number : ')

    if Practice.OddEven(x) == True:
        print('even')
    else:
        print('odd')

#Swapper
def Swapper():
    x = input('enter number x : ')
    y = input('enter number y : ')

    print('Pre-Swap : {} & {}'.format(x,y))
    print('Post-Swap : {} & {}'.format(Practice.Swapper(x,y),Practice.Swapper(y,x)))


#Sum of Digits
def SumOfDigits():

    x = input("enter a number : ")

    print('sum : {}'.format(Practice.SumOfDigits(x)))


#Reverser
def NumberReverse():

    x = input("enter a number : ")

    print('Reversed number : {}'.format(Practice.Reverser(x)))

#Determines wich method to run
def Selector(Activity):
    if Activity == 1:
        OddEven()
    elif Activity == 2:
        Swapper()
    elif Activity == 3:
        SumOfDigits()
    elif Activity == 4:
        NumberReverse()
    else:
        os.system('cls')
        quit()
    

def PrintMenu():
    print('[1]. Odd or Even')
    print('[2]. Swapper')
    print('[3]. Sum of Digits')
    print('[4]. Number Reverse')
    print('[5]. Exit\n')

def main():
    os.system('cls')
    Practice.Greet()
    PrintMenu()
    Activity = int(input('Select Activity : '))
    Selector(Activity)
    time.sleep(2)
    main()

main()