import numpy as np

def lu_decompose_gaussian_elimination_no_pivoting(A, b):
    n =  len(A)
    L=np.zeros(shape=(n,n))

    np.fill_diagonal(L,1.)
    #np.diag(x)
    if b.size != n:
        raise ValueError("Not compatible between A & b.", b.size, n)
    for pivot_row in range(n-1):
        for row in range(pivot_row+1, n):
            multiplier = A[row][pivot_row]/A[pivot_row][pivot_row]
            #A[row][pivot_row] = multiplier

            L[row][pivot_row] = multiplier
            A[row][pivot_row] = 0.
            for col in range(pivot_row + 1, n):
                A[row][col] = A[row][col] - multiplier*A[pivot_row][col]
#            #SOLUTION
            #b[row] = b[row] - multiplier*b[pivot_row]

    print ("\nLU decomposition with no partial pivoting..\n")
    print ("Upper triangular Matrix")
    print (A)
    print ("Lower Triangular Matrix")
    print (L)

    for i in range(n):
        b[i] = b[i]/L[i][i]
        for j in range(n):
            if j != i:
                b[i] -= L[i][j]*b[j]

    z=np.zeros(n)

    print ("[L][Z]=[b]...finding [Z]")
    z=b
    print (z)
    print ("[U][X]=[Z]....finding [X]")
    x = np.zeros(n)
    k = n-1
    x[k] = z[k]/A[k,k]
    while k >= 0:
        x[k] = (z[k] - np.dot(A[k,k+1:],x[k+1:]))/A[k,k]
        k = k-1
    return x



if __name__ == '__main__':
    ''''
    a1 = input("a1 = ");
    a2 = input("a2 = ");
    a3 = input("a3 = ");
    b1 = input("b1 = ");
    b2 = input("b2 = ");
    b3 = input("b3 = ");
    c1 = input("c1 = ");
    c2 = input("c2 = ");
    c3 = input("c3 = ");
    d1 = input("d1 = ");
    d2 = input("d2 = ");
    d3 = input("d3 = ");
'''
    #a = np.array([[a1,b1,c1],[a2,b2,c2],[a3,b3,c3]])
    #b = np.array([[d1],[d2],[d3]])
    a = np.array([[25.,5.,1.],[64.,8.,1.],[144.,12.,1.]])
    b =  np.array([[106.8],[177.2],[279.2]])
    print (a)
    print (b)

    print (lu_decompose_gaussian_elimination_no_pivoting(np.copy(a), np.copy(b)))