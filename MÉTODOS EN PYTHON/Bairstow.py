#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 22:26:58 2022

@author: felipe
"""

import cmath
import random
'''
Bairstow's Method where:
r = Initial guess
s = Initial guess
roots = Empty Array
a = Coefficient's vector
g = Polinomial's degree   
'''   
def bairstow(a,r,s,g,roots,itera):
    
    if(g<1):
        return None
    if((g==1) and (a[1]!=0)):
        roots.append(round(float(-a[0])/float(a[1]),2))
        return None
    if(g==2):
        D = (a[1]**2.0)-(4.0)*(a[2])*(a[0])
        X1 = (-a[1] - cmath.sqrt(D))/(2.0*a[2])
        X2 = (-a[1] + cmath.sqrt(D))/(2.0*a[2])
        roots.append(X1)
        roots.append(X2)
        return None
    n = len(a)
    b = [0]*len(a)
    c = [0]*len(a)
    b[n-1] = a[n-1]
    b[n-2] = a[n-2] + r*b[n-1]
    i = n - 3
    while(i>=0):
        b[i] = a[i] + r*b[i+1] + s*b[i+2]
       # a = [1.25,-3.875,2.125,2.75,-3.5,1]
        i = i - 1
    print("\narray:b completo "+str(b)+"\n")
    c[n-1] = b[n-1]
    c[n-2] = b[n-2] + r*c[n-1]
    i = n - 3
    while(i>=0):
        c[i] = b[i] + r*c[i+1] + s*c[i+2]
        i = i - 1
    
    Denominador = ((c[2]*c[2])-(c[3]*c[1]))**(-1.0)
    
    deltaR=round((Denominador)*((c[2])*(-b[1])+(-c[3])*(-b[0])),4)
    deltaS=round((Denominador)*((-c[1])*(-b[1])+(c[2])*(-b[0])),4)
    
    r = r + deltaR
    s = s + deltaS
    
    print("Iter: "+str(itera)+" DeltaR: "+str(deltaR))
    print("Iter: "+str(itera)+" DeltaS: "+str(deltaS))
    
   
    errorR=round(abs(deltaR/r)*100,4)
    errorS=round(abs(deltaS/s)*100,4)
    
    print("Iter: "+str(itera)+" errorR: "+str(errorR))
    print("Iter: "+str(itera)+" errorS: "+str(errorS))
    
    itera=itera+1
    
    # if(abs(b[0])>1E-14 or abs(b[1])>1E-14):
    #     return bairstow(a,r,s,g,roots,itera)
    
    if(errorR>1 or errorS>1):
        return bairstow(a,r,s,g,roots,itera)
    
    if (g>=3):
        print("Buscando Raices... \n")
        Dis = ((-r)**(2.0))-((4.0)*(1.0)*(-s))
        X1 = (r - complex(round((cmath.sqrt(Dis)).real,2), round( (cmath.sqrt(Dis)).imag, 2)))/(2.0)
        X2 = (r + complex(round((cmath.sqrt(Dis)).real,2), round( (cmath.sqrt(Dis)).imag, 2)))/(2.0)
        roots.append(X1)
        roots.append(X2)
        
        print("array:b[2:] "+str(b[2:]))
        return bairstow(b[2:],r,s,g-2,roots,itera)	#es como hacer dos divisiones, por eso elimino dos elementos del array
        #y por eso rebaja dos grados el polinomio


k = 0
g = 5
roots = []
# a = [-12*random.random(),2,3,-6,6,-1]
a = [1.25,-3.875,2.125,2.75,-3.5,1]
# r = random.random()
# s = random.random()
r =-1
s = -1
bairstow(a,r,s,g,roots,1)
print("\nFound Roots => \n")
for r in roots:
 	print( "R" + str(k) + " = " + str(r))
 	k += 1
p = ['P','y'] 
print("array P: "+str(p[2:]))



































































