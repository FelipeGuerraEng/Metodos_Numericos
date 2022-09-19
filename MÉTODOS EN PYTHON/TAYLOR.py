#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 00:49:37 2022

@author: felipe
"""

from scipy.misc import derivative
import math

class TaylorSeries():
    def __init__(self, function, order, center=0):
        self.center = center
        self.f = function 
        self.order = order
        self.d_pts = order*2
        self.coefficients = []

        # number of points (order) for scipy.misc.derivative
        if self.d_pts % 2 == 0: # must be odd and greater than derivative order
            self.d_pts += 1

        self.__find_coefficients()

    def __find_coefficients(self):
        for i in range(0, self.order+1):
            self.coefficients.append(round(derivative(self.f, self.center, n=i, order=self.d_pts)/math.factorial(i), 5))
            
    def print_equation(self):
        eqn_string = ""
        for i in range(self.order + 1):
            if self.coefficients[i] != 0:
               eqn_string += str(self.coefficients[i]) + ("(x-{})^{}".format(self.center, i) if i > 0 else "") + " + "
        eqn_string = eqn_string[:-3] if eqn_string.endswith(" + ") else eqn_string
        print(eqn_string)

    def print_coefficients(self):
        print(self.coefficients)

    def get_coefficients(self):
        """
            Returns the coefficients of the taylor series 
        """
        return self.coefficientsx
    
def f(x):
    return 2 + x**3 + x**7 + x**2

if __name__ == '__main__':
    terms = 3
    center = 0
    precision = 3

    ts = TaylorSeries(f, terms, center)
    ts.print_coefficients()
    ts.print_equation()