def gauss(mat,n):
    
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
                

    
n = int(input("Number of Equations: "))
mat = [[0.0 for j in range(n+1)] for i in range(n)]
    
print("\nEnter coefficients of the equations in format ax^n+bx^(n-1)+...+c = d",end = " ")
for i in range(0,n):
    a = input("Equation {}: ".format(i+1)).split()
    for j in range(0,n+1):
        mat[i][j] = (float)(a[j])
print("")

x = gauss(mat,n)
print("Ans : ",end="")
print(x)