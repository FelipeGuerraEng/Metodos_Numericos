#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 21:49:43 2022

@author: felipe
"""

from math import *
from numpy import array, zeros, diag, diagflat, dot,linalg
from pprint import pprint

def distinf(x, y):

    return max([abs(x[i] - y[i]) for i in range(len(x))])
    """Implementación distancia dada por la norma infinito"""

"""
Implementación del método de Jacobi
Entradas:
A -- matriz cuadrada
b -- vector
x0 -- aproximación inicial
TOL -- tolerancia
MAX -- número máximo de iteraciones

Salida:
x -- aproximación a solución del sistema Ax = b
None -- en caso de agotar las iteraciones o presentar errores
"""

# def Jacobi(A, b, x0, TOL, MAX):
    
#     n = tamano[0]
#     m = tamano[1]
#     x =np.zeros(n,dtype=float)
#     itera = 0

#     #n = len(A)
#     #x = [0.0 for x in range(n)]
#     #k = 1
    
#     for i in range(0,n,1):
#         nuevo = b[i]
#         for j in range(0,m,1):
#             if(i!=j):
#                 nuevo = nuevo-[A[i][j]*x0[j] 
#         nuevo = nuevo/A[i][i]
#         diferencia[i]=np.abs(nuevo-x0[i])
#         x[i]=nuevo
#         errado = np.max(diferenvia)
    
#     while k <= MAX:
#         for i in range(n):
#             if abs(A[i][i]) <= 1e-15:
#                 print("Imposible iterar")
#                 return None
#             s = sum([A[i][j]*x0[j] for j in range(n) if j != i])
#             x[i] = (b[i] - s)/A[i][i]
#     pprint(x)
#     if distinf(x, x0) < TOL:
#         print(r"Solución encontrada")
#         return x
#     k += 1
#     for i in range(n):
#         x0[i] = x[i]
#     print("Iteraciones agotadas")
#     return None

def jacobi(A,b,N,x):
    """Solves the equation Ax=b via the Jacobi iterative method."""
    # Create an initial guess if needed                                                                                                                                                            
    # if x is None:
    #     x = zeros(len(A[0]))
    n = len(A[0])

    for i in range(0, n) :        

        sum = 0
        for j in range(0, n) :
            sum = sum + abs(A[i][j])    
 
        sum = sum - abs(A[i][i])

        if (abs(A[i][i]) < sum) :
            isdiagDominant= False
        else: isdiagDominant = True
        print("Fila "+str(i)+" "+str(isdiagDominant))
    
    if not (isdiagDominant):
        return "La matriz no es diagonalmente dominante"
    
  
    # Create a vector of the diagonal elements of A                                                                                                                                                
    # and subtract them from A                                                                                                                                                                     
    D = diag(A)
    print("Matriz D:")
    pprint(D)
    R = A - diagflat(D)
    print("diagflat D:")
    pprint(diagflat(D))
    print("Matriz R:")
    pprint(R)

    # Iterate for N times 
    aux =0 
    print("Iter      x1            x2               x3           Error Absoluto")                                                                                                                                                                        
    for i in range(N):
        x2=x.copy()
        aux+=1
        x = (b - dot(R,x)) / D
        error=linalg.norm((x-x2),ord=4)#error absoluto orden 4 
        print(str(aux)+"   "+str(x)+"  "+str(error))

    return x


# A = array([[0.2, 0.25, 0.55], 
#               [0.2, 0.45, 0.2], 
#               [0.6, 0.3, 0.25]])
# b = array([4800, 5800, 5700])
A = array([[0.6, 0.3, 0.25], 
            [0.2, 0.45, 0.2],
            [0.2, 0.25, 0.55]])
b = array([5700, 5800, 4800])
guess = array([2000, 2000, 2000])

sol = jacobi(A,b,100,guess)

print("Matriz A:")
pprint(A)

print("Vector b:")
pprint(b)

print(r"Solución encontrada: ")
pprint(sol)


# A = np.array([[0.2, 0.25, 0.55], 
#               [0.2, 0.45, 0.2], 
#               [0.6, 0.3, 0.25]])
# b = np.array([4800, 5800, 5700])
# x0 = np.array([2000, 2000, 2000])
# print("Matriz A:")
# pprint(A)
# print("Vector b:")
# pprint(b)
# print("Semilla x0:")
# pprint(x0)
# print("Iteración de Jacobi")
# # T OL = 10 −5 , M AX = 50
# Jacobi(A, b, x0, 1e-5, 50)

# A = np.array([[0.6, 0.3, 0.25], 
#               [0.2, 0.45, 0.2],
#               [0.2, 0.25, 0.55]])
# b = np.array([5700, 5800, 4800])
# x0 = np.array([2000, 2000, 2000])
# print("Matriz A:")
# pprint(A)
# print("Vector b:")
# pprint(b)
# print("Semilla x0:")
# pprint(x0)
# print("Iteración de Jacobi")
# # T OL = 10 −10 , M AX = 50
# Jacobi(A, b, x0, 1e-10, 50)