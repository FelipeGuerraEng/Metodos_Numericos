#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 19:29:31 2022

@author: felipe
"""

from math import *

def trig(x):
    return sin(2/x) # retorna trig(x) = sin(2/x)

#Polinomio
def pol(x):
    return x**2 - 12 # retorna pol(x) = x^2 − 12


"""
Implementación método de la secante
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

def secante(f, p0, p1, tol, n):

    i = 0
    while i < n:
        p = p1 - (f(p1)*(p1 - p0))/(f(p1) - f(p0))
        errorAbs = abs(p - p1) 
        print("Iter = {0:<2}, p = {1:.12f}, E = {2:.12f}".format(i, p, errorAbs))
        if errorAbs < tol:
            return p
        p0 = p1
        p1 = p
        i += 1
    print("Iteraciones agotadas: Error!")
    return None

# pol(x), p 0 = −3.0, p 1 = 3.0, T OL = 10 −8 , N 0 = 100
print("Secante función pol(x):")
secante(pol, 2, 3, 1e-8, 100)

# trig(x), p 0 = 1.1, p 1 = 0.8, T OL = 10 −8 , N 0 = 100
#print("Secante función trig(x):")
#secante(trig, 1.1, 0.8, 1e-8, 100)