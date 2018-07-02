#!/bin/python3

import os
import sys

class Practice():

    #A cliche
    def Greet():
        print('HELLO WORLD! \n')
    
    #Determines whether the number is odd or even.
    def OddEven(x):
        if int(x)%2==0:
            return True
        else:
            return False
    
    #Swaps variable values
    def Swapper(x,y):
        temp = x
        x = y 
        y = temp

        return x   

    #Computes for the sum of each individual digits of a number
    def SumOfDigits(x):
        num = 0
        for i in range(len(x)):
            num = num + int(x[i])
        
        return num
    
    #Reverses the numerical input with no use of any string functions
    def Reverser(x):
        
        reversed = 0

        while x!=0:
            temp = int(x) % 10
            reversed = reversed * 10 + temp
            x = int(x) / 10
        
        return reversed