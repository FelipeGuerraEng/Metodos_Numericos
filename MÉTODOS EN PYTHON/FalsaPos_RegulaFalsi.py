#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 21:20:44 2022

@author: felipe
"""

from math import *

def func(x):
    return x**2 + 1 - exp(x)

def pol(x):
    return x**3 + 4*x**2 - 10 # retorna pol(x) = x 3 + 4x 2 − 10

def trig(x):
    return x*cos(x-1) - sin(x)
# retorna trig(x) = x cos(x − 1) − sin(x)

def pote(x):
    return pow(7, x) - 13 # retorna pote(x) = 7 x − 13


"""
Implementación método de regula falsi
Entradas:
f -- función
p0 -- aproximación inicial
p1 -- aproximación inicial
tol -- tolerancia
n -- número máximo de iteraciones

Salida:
p aproximación a cero de f
None en caso de iteraciones agotadas
"""
def regula(f, p0, p1, tol, n):

    i = 0
    while i <= n:
        q0 = f(p0)
        q1 = f(p1)
        p = p1-(q1*(p1 - p0))/(q1 - q0)
        errorAbs = abs(p - p1) 
        print("Iter = {0:<2}, p = {1:.12f}, E = {2:.12f}".format(i, p, errorAbs))
        if errorAbs < tol:
            return p
        i += 1
        q = f(p)
        if q*q1 < 0:
            p0 = p1
            q0 = q1
        p1 = p
        q1 = q
    print("Iteraciones agotadas: Error!")
    return None


# pol(x), a = 1.0, b = 2.0, T OL = 10 −8 , N 0 = 100
#print("Regula falsi función pol(x):")
#regula(pol, 1, 2, 1e-8, 100)

# trig(x), a = 4.0, b = 6.0, T OL = 10 −8 , N 0 = 100
#print("Regula falsi función trig(x):")
#regula(trig, 4, 6, 1e-8, 100)

# pote(x), a = 0, b = 2.0, T OL = 10 −8 , N 0 = 100
print("Regula falsi función e(x):")
regula(func, -1, 1, 1e-8, 100)