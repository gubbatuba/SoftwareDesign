# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 04:27:54 2014

@author: sgubba
"""

def compare():

    x = int(raw_input('x = '))
    y = int(raw_input('y = '))

    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1

print compare()