#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 21:35:56 2022

@author: felipe
"""

from sympy import sin, cos, Matrix
from sympy.abc import x, y



def newton(F, Jacobian, aproximaciones, tol, n):
    
    i = 1
    while i <= n:
        
        aprox_iniciales = aproximaciones.copy()
        
        Jacobia_evaluada = Jacobian.subs([(x,aproximaciones[0]), (y,aproximaciones[1])])
        F_evaluada = F.subs([(x,aproximaciones[0]), (y,aproximaciones[1])])
        
        Inversa_Jacob = Jacobia_evaluada.inv(method="LU")
        producto_matrices= Inversa_Jacob*F_evaluada
        
        aproximaciones = aproximaciones - producto_matrices
        
        errorAbs=(aproximaciones-aprox_iniciales).norm(2) 
        errorRel = (aproximaciones-aprox_iniciales).norm(2)/aproximaciones.norm(2)  
        
        print(str(i)+"   "+str(aproximaciones)+"  "+str(errorRel)+" "+str(errorAbs))

        if errorAbs < tol:
            return aproximaciones
        i += 1
    print("Iteraciones agotadas: Error!")
    return None


F = Matrix([x**2 +x*y-10, y + (3*x)*y**2 - 57])
Variables = Matrix([x, y])

aproximaciones = Matrix([1.5,3.5]);

# aproximaciones2 = Matrix([3.5,7.5]);
# print((aproximaciones2-aproximaciones).norm(2))

Jacobian = F.jacobian(Variables)

newton(F, Jacobian, aproximaciones, 1e-8, 100)

#F = Matrix([x**2 +x*y-10, y + (3*x)*y**2 - 57]).subs([(x,1.5), (y,3.5)])