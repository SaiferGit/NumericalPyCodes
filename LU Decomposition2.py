# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 14:02:41 2018

@author: munsh
"""


def pprint(A):
    n=len(A)
    
    for i in range(0,n):
        line=""
        for j in range(0,n):
            line+=str(A[i][j])+"   "
            
        print (line)
    print("")
        
        
        

def LU(A):
    
    n = len(A) # Give us total of liness

    # (1) Extract the b vector
    b = [0 for i in range(n)]
    for i in range(0,n):
        b[i]=A[i][n]

    # (2) Fill L matrix and its diagonal with 1
    L = [[0 for i in range(n)] for i in range(n)]
    for i in range(0,n):
        L[i][i] = 1

    # (3) Fill U matrix
    U = [[0 for i in range(0,n)] for i in range(n)]
    for i in range(0,n):
        for j in range(0,n):
            U[i][j] = A[i][j]

    #n = len(U)

    # (4) Find both U and L matrices
    for i in range(0,n): # for i in [0,1,2,..,n]
        # (4.1) Find the maximun value in a column in order to change lines
        #pivoting starts
        '''
        maxRow = i
        
        b[i],b[maxRow]=b[maxRow],b[i]
        # (4.2) Swap the rows pivoting the maxRow, i is the current row
        for k in range(i, n): # Interacting column by column
            tmp=U[maxRow][k]
            U[maxRow][k]=U[i][k]
            U[i][k]=tmp
            '''
            #pivoting ends
        # (4.3) Subtract lines
        for k in range(i+1,n):
            c = -U[k][i]/float(U[i][i])
            L[k][i] = -c # (4.4) Store the multiplier
            for j in range(i, n):
                U[k][j] += c*U[i][j] # Multiply with the pivot line and subtract

        # (4.5) Make the rows bellow this one zero in the current column
        for k in range(i+1, n):
            U[k][i]=0
        
    print("Upper triangular Matrix: ")
    pprint(U)
    n = len(L)
    print("    ")
    print ("Lower triangular Matrix: ")
    pprint(L)
    
    #print (U)
   # print (L)

    # (5) Perform substitutioan Ly=b
    y = [0 for i in range(n)]
    for i in range(0,n,1):
        y[i] = b[i]/float(L[i][i])
        for k in range(0,i,1):
            y[i] -= y[k]*L[i][k]
           

    #n = len(U)
    #print ("y==")
    print (y)
    
  
    # (6) Perform substitution Ux=y
    
    x = []
    for i in range(0,n):
        x.append(0)
   # print("n-1",n-1)
    
    for i in range(n-1,-1,-1):
        x[i] = y[i]
        for k in range (i+1,n,1):
            x[i] -= x[k]*U[i][k]
        x[i]/=float(U[i][i]);

    return x

n=int(input("Enter n: "))
l=[]
for i in range (0,n):
    row=[]
    ar = list(map(float, input().strip().split(' ')))
    l.append(ar)
    
   
#print(l)
x=LU(l)
for i in range(1,n+1):
    line="x"+str(i)
    print(line ,"=", x[i-1])
    
    


''''
3

25 5 1 106.8

64 8 1 177.2

144 12 1 279.2
'''
