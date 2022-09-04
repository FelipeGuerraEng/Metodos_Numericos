#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 19:43:36 2022

@author: felipe
"""

import numpy as np
from numpy.linalg import solve, inv

a = np.array([[-1.1, 2.5], [1.3, 4.2]])
A = np.array([[2, 1, 3], 
            [-1, 2, 4],
            [0, 1, 3]])
print(a)
print(a.T) # transpuesta
print("INVERSA")
print(inv(A)) # inversa
# matriz forma (2,2)

b = np.array([[2], [-3]]) # vector forma (2,1)
print(b)
s = solve(a, b) # solucionar el sistema de ecuaciones
print(s)