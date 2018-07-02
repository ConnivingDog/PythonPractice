#!/bin/python3

import os
import sys

class Practice():


    def Greet():
        print('HELLO WORLD! \n')
    
    def OddEven(x):
        if int(x)%2==0:
            return True
        else:
            return False
    
    def Swapper(x,y):
        temp = x
        x = y 
        y = temp

        return x   

    def SumOfDigits(x):
        num = 0
        for i in range(len(x)):
            num = num + int(x[i])
        
        return num
    
    def Reverser(x):
        
        reversed = 0

        while x!=0:
            temp = int(x) % 10
            reversed = reversed * 10 + temp
            x = int(x) / 10
        
        return reversed