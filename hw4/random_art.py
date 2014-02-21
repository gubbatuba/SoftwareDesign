# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:34:57 2014

@author: Subhash Gubba
"""

# you do not have to use these particular modules, but they may help
from random import randint
import Image
from math import *


im = Image.new("RGB",(350,350))
pixel = im.load()
def build_random_function(min_depth, max_depth):
    # your doc string goes here
    """ Recursively generates a random function with some random depth using:

        > prod(a,b) = ab
        > cos_pi(a) = cos(pi*a)
        > sin_pi(a) = sin(pi*a)
        > l(a,b) = a
        > k(a,b) = b
        > div-sum-rand(a,b) = divides a and b by a random number and sums them
        > rando(a,b) = [randomly selects either a or b]
        
        min_depth is the minimum level of nesting the function will have
        max_depth is the maximum level of nesting the function will have         
    """
    # your code goes here
    runc = ["sin_pi","cos_pi","prod","l","k","div-sum-rand","rando"]    
    xy = ["a","b"]
    depth = randint(min_depth,max_depth)
    if depth == 1:
        return xy[randint(0,1)]
    elif depth > 1:
        start = runc[randint(0,len(runc)-1)]
        if start == runc[0:2]:
            return [start,build_random_function(depth-1,depth-1)]
        else:
            return [start,build_random_function(depth-1,depth-1),build_random_function(depth-1,depth-1)]
                        
def evaluate_random_function(f, x, y):
    # your doc string goes here
    """ Converts the list given from build_random_funciton into an actual
        function which takes x and y and returns the result of the function.
        
        f is the randomly generated function list
        x is the first input
        y is the second input
    """
    # your code goes here
    if f[0] == "a":
        return x
    elif f[0] == "b":
        return y
    elif f[0] == "sin_pi":
        return sin(pi*evaluate_random_function(f[1],x,y))
    elif f[0] == "cos_pi":
        return cos(pi*evaluate_random_function(f[1],x,y))
    elif f[0] == "prod":
        return evaluate_random_function(f[1],x,y)*evaluate_random_function(f[2],x,y)
    elif f[0] == "l":
        return evaluate_random_function(f[1],x,y)
    elif f[0] == "k":
        return evaluate_random_function(f[2],x,y)
    elif f[0] == "div-sum-rand":
        return (((evaluate_random_function(f[1],x,y))/randint(2,100))+(evaluate_random_function(f[2],x,y))/randint(2,100))
    elif f[0] == "rando":
        land = [evaluate_random_function(f[1],x,y),evaluate_random_function(f[2],x,y)]
        return land[randint(0,1)]

        
def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Maps the input value that is in the interval [input_interval_start, input_interval_end]
        to the output interval [output_interval_start, output_interval_end].  The mapping
        is an affine one (i.e. output = input*c + b).
    
        TODO: please fill out the rest of this docstring
    """
        
    output_range = output_interval_start - output_interval_end
    input_range = input_interval_end - input_interval_start
    relative_val = val - input_interval_end
    return (float(output_range)/input_range)*relative_val+output_interval_start
        
    # your code goes here
    # return (((float(output_interval_end)) - float(output_interval_start))/(float(input_interval_end) - float(input_interval_start)))*(float(val) - float(output_interval_end)) + float(output_interval_start)

def trip_balls(width,length):
    """ Draws the artwork from RGB functions.
    """    
    Red = build_random_function(5,10)
    Green = build_random_function(3,15)
    Blue = build_random_function(2,12)
    for i in range(0,width-1):
        for j in range(0,length-1):
            aye = remap_interval(i,0,width-1,-1,1)
            jay = remap_interval(j,0,length-1,-1,1)
            r = remap_interval(evaluate_random_function(Red,aye,jay),-1,1,0,255)
            g = remap_interval(evaluate_random_function(Green,aye,jay),-1,1,0,255)
            b = remap_interval(evaluate_random_function(Blue,aye,jay),-1,1,0,255)
            '''
            print r
            print g
            print b
            '''
            pixel[i,j] = (int(r),int(g),int(b))
    im.save("colorpuke.png")


if __name__=="__main__":
    print build_random_function(3,6)
    print evaluate_random_function(build_random_function(3,6),1,-1)
    trip_balls(349,349)
 