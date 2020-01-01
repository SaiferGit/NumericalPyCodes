# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 16:13:12 2018

@author: munsh
"""

import numpy as np


def gauss_method_here(mat,n):
    
    for j in range(0,n-1):
        
        max_row, val = j, 0
        for i in range(j, n):
            if(abs(mat[i][j]) > val):
                val = abs(mat[i][j])
                max_row = i
        
        #Find the max row and swap (Partial pivoting)
        for k in range(0, n+1):
            mat[j][k],mat[max_row][k] = mat[max_row][k],mat[j][k]
            
        #COnvert all rows beneath the pivot to 0
        for i in range(j+1, n):
            c = mat[i][j]/mat[j][j]
            for k in range(j, n+1):
                mat[i][k] -= c * mat[j][k]
        
        #Print the matrix at every step
        """print("Step {}:--".format(j+1))
        for p in range(0,n):
            print(mat[p])
        print("-------------")"""
        
    #Solve equation from Upper Triangle Matrix
    ans = [0 for k in range(n)]
    for i in range(n-1, -1, -1):
        ans[i] = mat[i][n]/mat[i][i]
        for k in range(i-1, -1, -1):
            mat[k][n] -= mat[k][i] * ans[i]
    return ans

def U(mat,n):
    
    U = [[0.0 for i in range(0,n)] for j in range(0,n)]
    
    for i in range(0,n):
        for j in range(0,n):
            U[i][j] = mat[i][j]
            
    for j in range(0,n-1):
        for i in range(j+1, n):
            if(U[j][j] == 0):
                return False
            c = U[i][j]/U[j][j]
            for k in range(j, n):
                U[i][k] -= c * U[j][k]
    
    return U


def getLU(mat,n):
    
    L = [[0.0 for i in range(0,n)] for j in range(0,n)]
    U = [[0.0 for i in range(0,n)] for j in range(0,n)]
    
    #partial pevoting start
    for j in range(0,n-1):
        
        max_row, val = j, 0
        for i in range(j, n):
            if(abs(mat[i][j]) > val):
                val = abs(mat[i][j])
                max_row = i
        
        #Find the max row and swap (Partial pivoting)
        for k in range(0, n+1):
            mat[j][k],mat[max_row][k] = mat[max_row][k],mat[j][k]
    #partial pevoting done
    
    for i in range(0,n):
        L[i][i] = 1
    
    
    

    
    #Transfer mat in U
    for i in range(0,n):
        for j in range(0,n):
            U[i][j] = mat[i][j]
    
    #Determine L,U matrices.
    for j in range(0,n-1):
        for i in range(j+1, n):
            
            if(U[j][j] == 0):
                return False,False
            c = U[i][j]/U[j][j]
            L[i][j] = c
            for k in range(j, n):
                U[i][k] -= c * U[j][k]
    return L,U
                
def solv(L, U, mat, n):
    
    
    A = [[0.0 for i in range(0,n+1)] for j in range(0,n)]
    for i in range(0,n):
        for j in range(0,n):
            A[i][j] = L[i][j]
    for i in range(0,n):
        A[i][n] = mat[i][n]
        
    #Solve LZ=C and determine Z
    z = [0.0 for i in range(0,n)]
    for i in range(0, n):
        z[i] = A[i][n]/A[i][i]
        for k in range(i+1, n):
            A[k][n] -= A[k][i] * z[i]
    
    print("Z : ",end=" ")
    print(["%0.5f" % j for j in z])
    
    for i in range(0,n):
        for j in range(0,n):
            A[i][j] = U[i][j]
    for i in range(0,n):
        A[i][n] = z[i]
        
    #Solve UX=Z and determine X
    ans = [0 for k in range(n)]
    for i in range(n-1, -1, -1):
        ans[i] = A[i][n]/A[i][i]
        for k in range(i-1, -1, -1):
            A[k][n] -= A[k][i] * ans[i]
    return ans

def solve(L, U, C, mat, n):
    
    #Store L and U values in temporary matrix A for each step
    A = [[0.0 for i in range(0,n+1)] for j in range(0,n)]
    for i in range(0,n):
        for j in range(0,n):
            A[i][j] = L[i][j]
    for i in range(0,n):
        A[i][n] = C[i]
        
    #Solve LZ=C and determine Z
    z = [0.0 for i in range(0,n)]
    for i in range(0, n):
        z[i] = A[i][n]/A[i][i]
        for k in range(i+1, n):
            A[k][n] -= A[k][i] * z[i]
    
    #print("Z : ",end=" ")
    #print(["%0.5f" % j for j in z])
    
    for i in range(0,n):
        for j in range(0,n):
            A[i][j] = U[i][j]
    for i in range(0,n):
        A[i][n] = z[i]
        
    #Solve UX=Z and determine X
    ans = [0 for k in range(n)]
    for i in range(n-1, -1, -1):
        ans[i] = A[i][n]/A[i][i]
        for k in range(i-1, -1, -1):
            A[k][n] -= A[k][i] * ans[i]
    
    return ans




mat = [[25., 5., 1., 106.8], [64., 8., 1., 177.2], [144., 12., 1., 279.2]]
n=3
L,U = getLU(np.copy(mat),n)

if(L == False and U == False):
    print("No Solution")
    exit(0)
    
print("Lower Triangular Matrix:")
for i in range (0,n):
    print(["%0.5f" % j for j in L[i]])
print("\n")

print("Upper Triangular Matrix:")
for i in range (0,n):
    print(["%0.5f" % j for j in U[i]])

print("\n")
ans = solv(L,U,mat,n)

print("Roots of LU ",end=" ")

print(["%0.5f" % j for j in ans])

print("\n")
    
x=gauss_method_here(mat,n)

print("Roots of Gaussian Elimination:")

print(x)




