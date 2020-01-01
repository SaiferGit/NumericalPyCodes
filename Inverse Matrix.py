# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 13:59:11 2018

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


n = int(input("Size of Square Matrix: "))
mat = [[0.0 for j in range(n)] for i in range(n)]
    
for i in range(0,n):
    a = input("Row {}: ".format(i+1)).split()
    for j in range(0,n):
        mat[i][j] = (float)(a[j])
print("")

L,U = getLU(np.copy(mat),n)

inverse = [[0 for i in range(n)] for j in range(n)]
for col in range(0,n):
    print("Step {}:---".format(col+1))
    C = [0 for i in range(n)]
    C[col] = 1
    ret = solve(L,U,C,mat,n)
    
    print("Column {}:".format(col+1),end=" ")
    print(["%0.5f" % j for j in ret])
    print("--------\n")
    
    for i in range(0,n):
        inverse[i][col] = ret[i]
        
print("Inverse Matrix:-----")
for i in range (0,n):
    print(["%0.5f" % j for j in inverse[i]])
