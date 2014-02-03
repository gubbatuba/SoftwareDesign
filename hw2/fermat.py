# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 03:56:54 2014

@author: sgubba
"""

def check_fermat(a,b,c,n):
    
    if a**n + b**n == c**n and n >= 2:
        print "Holysmokes, Fermat was wrong!"
    else:
        print "No, that doesn't work"

def fermat():
    
    a = int(raw_input('A = '))
    b = int(raw_input('B = '))
    c = int(raw_input('C = '))
    n = int(raw_input('n = '))
    
    check_fermat(a,b,c,n)
    
fermat()