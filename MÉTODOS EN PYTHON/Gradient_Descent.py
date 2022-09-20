#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 11:42:20 2022

@author: felipe
"""

import numpy as np
from numpy import linalg as LA

def is_pos_def(x):
    """check if a matrix is symmetric positive definite"""
    return np.all(np.linalg.eigvals(x) > 0)

def steepest_descent(A, b, x):
    """
    Solve Ax = b
    Parameter x: initial values
    """
    if (is_pos_def(A) == False) | (A != A.T).any():
        raise ValueError('Matrix A needs to be symmetric positive definite (SPD)')
    r = b - A @ x
    k = 0
    while LA.norm(r) > 1e-5 :
        p = r
        print("Iter: "+str(k)+" norm: "+str(LA.norm(r)))
        #print("\nIter: "+str(k)+" P: "+str(p)+" rn: "+str(r))
        q = A @ p
        #print("      "+" q: "+str(q))
        #print("      "+" p.r: "+str(p @ r))
        #print("      "+" p.q: "+str(p @ q))
        alpha = (p @ r) / (p @ q)
        #print("      "+" alpha: "+str(alpha))
        x = x + alpha * p
        r = r - alpha * q
        k = k+ 1
        #print("\nIter: "+str(k)+" xn+1: "+str(x))
        #print("Iter: "+str(k)+" rn+1: "+str(r))

    return x

A = np.array([[10, 2, 1], [2, 1,-2], [1, -2, 10]])
b = np.array([2, 3, 4])
x0 = np.array([0, 0, 0])


steepest_descent(A, b, x0)
