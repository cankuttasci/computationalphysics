#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 16:47:16 2022

@author: cankuttasci
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
grid=100
x=np.linspace(-5,5,grid)
pot=x*x
ne=1
#Firt order derivative
     
def KSDFT(ne,grid,pot,x):
     h=x[1]-x[0]
     D=-np.eye(grid)+np.diagflat(np.ones(grid-1),1)
     D = D / h
     #Second order derivative
     D2=D.dot(-D.T)
     #Getting rid of the ends
     D2[-1,-1]=D2[0,0]
     #Density
     # integral
     # integral(Mean value method)
     def integral(x,y):
         a=x[0]
         b=x[-1]
         N=len(x)
         sum1=0
         for i in range(N):
             sum1+=y[i]
         return (b-a)*sum1/N

     def density(ne, psi, x):
         # normalization
    
         C=integral(x,psi**2)
         normed_psi=psi/np.sqrt(C)
         oc=[]
         for i in range(ne//2):
              oc.append(2)
         if ne%2:
              oc.append(1)
         n=np.zeros(grid)
         if len(oc)>=grid:
           for j in range(grid):
               n+=oc[j]*normed_psi.T[j,:]**2
         else:
           for j in range(len(oc)):
               n+=oc[j]*normed_psi.T[j,:]**2
         #print(n)
         return n

     def Exchange(n,x):
        Eex=-3/4*(3/np.pi)**(1/3)*integral(x,n**(4/3))
        Vex=-(3/np.pi)**(1/3)*n**(1/3)
        return Eex, Vex
     def Hatree(n,x, eps=1e-1):
        h=x[1]-x[0]
        Eh=0
        for i in range(len(n)):
               for j in range(len(n)):
                   Eh+=1/2*(n[i]*n[j]*h**2)/(np.sqrt((x[i]-x[j])**2+eps))
        Vh=[]
        for i in range(len(n)):
            V0=0
            for j in range(len(n)):
                V0+=n[j]*h/(np.sqrt((x[i]-x[j])**2+eps))
            Vh.append(V0)
        Vh=np.array(Vh)
        return Eh, Vh
     def print_log(i,log):
          print(f"step: {i:<5} energy: {log['energy'][-1]:<10.4f} energy_diff: {log['energy_diff'][-1]:.10f}")

     max_iter=1000
     energy_tolerance=1e-5
     log={"energy":[float("inf")], "energy_diff":[float("inf")]}
     n=np.zeros(grid)
     for i in range(max_iter):
             ex_energy, ex_potential=Exchange(n,x)
             ha_energy, ha_potential=Hatree(n,x)
          # Hamiltonian
             H=-D2/2+np.diagflat(ex_potential+ha_potential+pot)
             energy, psi= np.linalg.eigh(H)
           # log
             log["energy"].append(energy[0])
             energy_diff=energy[0]-log["energy"][-2]
             log["energy_diff"].append(energy_diff)
             print_log(i,log)
      
             # convergence
             if abs(energy_diff) < energy_tolerance:
                 print("converged!")
                 break
   
             n=density(ne,psi,x)

     else:
                print("not converged")
KSDFT(ne,grid,pot,x)
