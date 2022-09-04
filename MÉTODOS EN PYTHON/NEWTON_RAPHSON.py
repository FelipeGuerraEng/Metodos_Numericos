#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 20:15:07 2022

@author: felipe
"""

from math import *

def expo(x):
    return 50*x - 0.35 * exp(0.75*x)
# retorna expo(x) = x 2 + e −2x − 2xe −x

def expoprima(x):
    return 50 - 0.2625 * exp(0.75*x)


#def expoprima(x):
  #  return 2*x - 2*exp(-2*x) - 2*exp(-x) + 2*x*exp(-x)

def trig(x):
    return cos(x) - x # retorna trig(x) = cos(x) − x

def trigprima(x):
    return -sin(x) - 1
# retorna trigprima(x) =

"""
Implementación método de Newton
Entradas:
f -- función
fprima -- derivada función f
p0 -- aproximación inicial
tol -- tolerancia
n -- número máximo de iteraciones

Salida:
p aproximación a cero de f
None en caso de iteraciones agotadas
"""

def newton(f, fprima, p0, tol, n):
    i = 1
    while i <= n:
        p = p0 - f(p0)/fprima(p0)
        errorAbs = abs(p - p0) 
        errorRel = abs(p - p0)/abs(p)
        print("Iter = {0:<2}, p = {1:.12f}, ErrAbs = {2:.12f}, ErrRel = {3:.12f}".format(i, p, errorAbs,errorRel))

        if errorAbs < tol:
            return p
        p0 = p
        i += 1
    print("Iteraciones agotadas: Error!")
    return None

# trig(x), trigprima(x), p 0 = π 4 , T OL = 10 −8 , N 0 = 100
#print("Newton función trig(x):")
#newton(trig, trigprima, pi/4, 1e-8, 100)

# expo(x), expoprima(x), p 0 = 4.0, T OL = 10 −8 , N 0 = 100
print("Newton función expo(x):")
newton(expo, expoprima, 9.5, 1e-8, 100)