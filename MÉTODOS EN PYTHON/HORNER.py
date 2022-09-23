#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 15:53:51 2022

@author: felipe
"""



def horner(poly, n, x):
    result = poly[0]
    for i in range(1, n):
        result = result * x + poly[i]
    print ("the value of polynomial at x = " + str(x) + " is " + str(result))


def main():
    # Let us evaluate value of 2x3 - 6x2 + 2x - 1 for x = 3
    poly = [1, -3, 7, -2, 1]
    x = 1
    n = len(poly)
    horner(poly, n, x)
    
if __name__ == '__main__':
    main()