#!/bin/python3

import os
import sys

class GraphicExer():
    row = 0
    col = 0

    def __init__(self, row, col):
        self.row += row
        self.col += col

    def Draw(self): #add 'self' as params on class methods
        for i in range(self.row):
            for j in range(self.col):
                print('+---', end="")
            print('+')
            for h in range(self.col):
                print('|   ', end="")
            print('|')
        for i in range(self.col):
                print('+---', end="")
        print('+')
            
