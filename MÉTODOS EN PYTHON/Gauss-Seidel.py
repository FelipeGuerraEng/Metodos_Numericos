#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 18:38:28 2022

@author: felipe
"""


from numpy import array, zeros, diag, diagflat, dot,linalg
from pprint import pprint

def gaussSeidel(A,b,N,x):
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

 
    aux=seidel(20,n,R,D,b,x,0)

    # errorRel=(linalg.norm((x-x2)/linalg.norm((x-x2)),ord=4)#error absoluto orden 4 
    # print(str(aux)+"   "+str(x)+"  "+str(errorRel))

    return aux

def seidel(N,n,R,D,b,x,iteraciones):
   x2=x.copy()

   if N == 0:
       return x
   else:
       iteraciones +=1
       
       for i in range(0, n):        
           # temp variable d to store b[j]
           temp = b[i]                  
             
           # to calculate respective xi, yi, zi
           for j in range(0, n):     
               if(i != j):
                   temp-=R[i][j] * x[j]
           # updating the value of our solution        
           x[i] = temp / D[i]
           
       errorRel=linalg.norm(x-x2,ord=2)/linalg.norm(x,ord=2)#error absoluto orden 4 
       print(str(iteraciones)+"   "+str(x)+"  "+str(errorRel))
       return seidel(N-1,n,R,D,b,x,iteraciones)

# A = array([[0.2, 0.25, 0.55], 
#               [0.2, 0.45, 0.2], 
#               [0.6, 0.3, 0.25]])
# b = array([4800, 5800, 5700])
A = array([[4.0, -1.0, 0.0, -1.0], 
            [-1.0, 4.0, -1.0, 0.0],
            [0.0, -1.0, 4.0, 0.0],
            [-1.0, 0.0, 0.0, 4.0]])
b = array([330.0, 325.0, 475.0, 355.0])
guess = array([100.0, 100.0, 100.0, 100.0])

sol = gaussSeidel(A,b,100,guess)

print("Matriz A:")
pprint(A)

print("Vector b:")
pprint(b)

print(r"Solución encontrada: ")
pprint(sol)

