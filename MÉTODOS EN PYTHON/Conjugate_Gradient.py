#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 12:39:11 2022

@author: felipe
"""
import numpy as np
from numpy import linalg as LA

def is_pos_def(x):
    """check if a matrix is symmetric positive definite"""
    return np.all(np.linalg.eigvals(x) > 0)

def conjugate_gradient(A, b, x):
    
    if (is_pos_def(A) == False) | (A != A.T).any():
        raise ValueError('Matrix A needs to be symmetric positive definite (SPD)')
    r = b - A @ x
    k = 0
    #x = np.zeros(A.shape[-1])
    
    while LA.norm(r) > 1e-6 :
        print("\nIter: "+str(k)+" norm: "+str(LA.norm(r)))
        print("Iter: "+str(k)+" xn: "+str(x))
        print("Iter: "+str(k)+" rn: "+str(r))
        if k == 0:
            p = r
        else: 
            gamma = - (p @ A @ r)/(p @ A @ p)
            print("      "+" gamma "+str(gamma))
            p = r + gamma * p
            print("      "+" p "+str(p))
        alpha = (p @ r) / (p @ A @ p)
        print("      "+" alpha: "+str(alpha))
        x = x + alpha * p
        print("Iter: "+str(k)+" r: "+str(r)+" A: "+str(A)+" p: "+str(p)+" A.p: "+str(A @ p)+" alpha * A.p: "+str(np.round((alpha * (A @ p)),4)))
        r = np.round(r,4) - np.round((alpha * (A @ p)),4)
        
        print("\nIter: "+str(k)+" xn+1: "+str(x))
        print("Iter: "+str(k)+" rn+1: "+str(r))
        k =+ 1
    return x


A = np.array([[3, -2], [-2, 4]])
b = np.array([4, 8])
x0 = np.array([1, 1 ])

conjugate_gradient(A, b, x0)