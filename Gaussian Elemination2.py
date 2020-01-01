# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 14:00:17 2018

@author: munsh
"""
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 20:51:19 2018

@author: Satabdi
"""


def pprint(a):
    n = len(a)
    for i in range(0, n):
        line = ""
        for j in range(0, n+1):
            line += str(a[i][j]) + "\t"
            if j == n-1:
                line += "| "
        print(line)
    print("")


def gauss(a):
    n = len(a)

    for i in range(0, n):
        # Search for maximum in this column
        pprint(a)
        maxEl = abs(a[i][i])
        maxRow = i
        for k in range(i+1, n):
            if abs(a[k][i]) > maxEl:
                maxEl = abs(a[k][i])
                maxRow = k

        # Swap maximum row with current row (column by column)
        for k in range(i, n+1):
            tmp = a[maxRow][k]
            a[maxRow][k] = a[i][k]
            a[i][k] = tmp

        # Make all rows below this one 0 in current column
        for k in range(i+1, n):
            c = -a[k][i]/a[i][i]
            for j in range(i, n+1):
                if i == j:
                    a[k][j] = 0
                else:
                    a[k][j] += c * a[i][j]

    # Solve equation Ax=b for an upper triangular matrix A
    x = [0 for i in range(n)]
    for i in range(n-1, -1, -1):
        x[i] = a[i][n]/a[i][i]
        for k in range(i-1, -1, -1):
            a[k][n] -= a[k][i] * x[i]
    return x


if __name__ == "__main__":

    n = int(input())
    a = []
    for i in range(n):
        a.append([float(j) for j in input().split()])
    # Print input
    
    pprint(a)

    # Calculate solution
    x = gauss(a)

    # Print result
    line = "Result:\t"
    for i in range(0, n):

        line += str(x[i]) + "\t"
    print(line)