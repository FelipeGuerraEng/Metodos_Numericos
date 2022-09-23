#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 13:51:56 2022

@author: felipe
"""

import matplotlib.pyplot as plt
import numpy as np
from typing import Tuple, List
from math import *


def func(x):
    return 0.4*exp(x**2)

def pol(x):
    return (4/5)*x**2 

def expo(x):
    return exp(-x)

def iteration(given_function, x0, min_error=0.01, max_iteration=3) -> Tuple[float, List]:
    i = 0
    error = 1
    err=[]
    xp = []
    x = None
    while error > min_error and i < max_iteration:
        x = given_function(x0)
        print(x)
        error = abs(x0 - x)
        errorRel = abs(x0 - x)/abs(x)
        x0 = x
        xp.append(x0)
        err.append(error)
        #error = errorRel
        i += 1
    print(xp)
    print(err)
    return x, xp


def plot(xf, xp, x_start, given_function):
    function_v = np.vectorize(given_function)

    x = np.linspace(0, 2, 100)
    y = function_v(x)
    plt.plot(x, y)
    plt.plot(xp, function_v(xp), 'bo')
    plt.plot(x_start, given_function(x_start), 'ro')
    plt.plot(xf, given_function(xf), 'go')
    plt.plot(x, x, 'k')
    plt.show()
    

def main():
    #fx = input("Write function: ")
   # fx = func
    #given_function = lambda x: eval(fx)

    x_start = 0
    xf, xp = iteration(expo, x_start)

    plot(xf, xp, x_start, expo)


if __name__ == '__main__':
    main()