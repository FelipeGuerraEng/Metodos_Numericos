# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

@author: felipe
"""

import math


def func(x):
    return math.exp(x)-math.sin(3* x) - 2

def pol(x):
    return x**3 + 4*x**2 - 10
# retorna pol(x) = x 3 + 4x 2 − 10

def trig(x):
    return x*math.cos(x-1) - math.sin(x)
# retorna trig(x) = x cos(x − 1) − sin(x)

def biseccion(xa,xb,count):
    a=xa
    b=xb
    m = (a + b) / 2
    
    while(func(m)!=0 and count < 18 ):
        if func(a) * func(m) < 0:
            b=m
        else:
            a=m
        m = (a + b) / 2
        count += 1
        print(m)
    
    return m, count


def bis(lower, upper, maxiter, tol):

    if lower >= upper:
        raise ValueError('Range error: lower >= upper')
    if func(lower) == 0:
        return lower
    elif func(upper) == 0:
        return upper
    elif func(lower) * func(upper) > 0:
        raise ValueError('Range error: interval must contain the root')

    i = 0
    while True:
        print("a " + str(lower))
        print("b " + str(upper))
        
        if i > maxiter:
            break
        
        center = (lower + upper) / 2
        print("center " + str(center))
        
        if abs(func(center)) <= tol:
            break
        if func(lower) * func(center) < 0:
            upper = center
        else:
            lower = center 
        i += 1
    return center, i

"""
Implementación método de bisección
Entradas:
f -- función
a -- inicio intervalo
b -- fin intervalo
tol -- tolerancia
n -- número máximo de iteraciones

Salida:
p aproximación a cero de f
None en caso de iteraciones agotadas
"""
def bisec(f, a, b, tol, n):

    i = 0
    while i < n:
        p = a + (b - a)/2
        error = abs(f(p))
        print("i = {0:<2}, p = {1:.12f}, E = {2:.12f}".format(i, p, error))
        if  error <= 1e-15 or (b - a)/2 < tol:
            return p
        i += 1
        if f(a)*f(p) > 0:
            a = p
        else:
            b = p
    print("Iteraciones agotadas: Error!")
    return None


def main():
    a = 0.0
    b = 1.0
    #punto_medio, iteraciones = biseccion(a,b,0)
    #punto_medio, iteraciones = bis(a,b,1000,0.00000001)

    print("Bisección función trig(x):")
    bisec(func, a, b, 1e-8, 100)
        
    # pol(x), a = 1, b = 2, T OL = 10 −8 , N 0 = 100
    #print("Bisección función pol(x):")
    #bisec(pol, 1, 2, 1e-8, 100)
  
    # trig(x), a = 4, b = 6, T OL = 10 −8 , N 0 = 100
    #print("Bisección función trig(x):")
    #bisec(trig, 4, 6, 1e-8, 100)
    #print(f'Punto Medio: {punto_medio}, iteraciones: {iteraciones}')
    
    
main()

