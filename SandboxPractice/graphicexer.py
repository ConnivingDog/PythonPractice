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
            self.DrawHorizontal()
            self.DrawVertical()
        self.DrawHorizontal()

    def DrawHorizontal(self):
        print('+---' * self.col, end="")
        print('+')

    def DrawVertical(self):
        print('|   ' * self.col, end="")
        print('|')