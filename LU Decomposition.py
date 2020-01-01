# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 13:58:22 2018

@author: munsh
"""

import numpy as np

def getLU(mat,n):
    
    L = [[0.0 for i in range(0,n)] for j in range(0,n)]
    U = [[0.0 for i in range(0,n)] for j in range(0,n)]
    for i in range(0,n):
        L[i][i] = 1
        
    #Transfer mat in U
    for i in range(0,n):
        for j in range(0,n):
            U[i][j] = mat[i][j]
    
    #Determine L,U matrices.
    for j in range(0,n-1):
        for i in range(j+1, n):
            #Condition for divide by 0
            if(U[j][j] == 0):
                return False,False
            c = U[i][j]/U[j][j]
            L[i][j] = c
            for k in range(j, n):
                U[i][k] -= c * U[j][k]
    
    return L,U
                
def solve(L, U, mat, n):
    
    #Store L and U values in temporary matrix A for each step
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
    
    
mat = [[25, 5, 1], [64, 8, 1], [144, 12, 1]]
n = 3
L,U = getLU(np.copy(mat),n)

if(L == False and U == False):
    print("No Solution")
    exit(0)
    
print("Lower Triangular Matrix:--")
for i in range (0,n):
    print(["%0.5f" % j for j in L[i]])
print("------------")

print("Upper Triangular Matrix:--")
for i in range (0,n):
    print(["%0.5f" % j for j in U[i]])   
print("------------")

ans = solve(L,U,mat,n)
print("Ans : ",end=" ")
print(["%0.5f" % j for j in ans])