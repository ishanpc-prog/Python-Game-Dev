matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
print(len(matrix)) #this instruction shows you the number of rows in your 2d list
print(len(matrix[0])) #this is to know the number of columns
print(matrix[2][2]) #acessing an element in 2d list
for i in range(0,len(matrix)):
    for j in range(0,len(matrix[0])):
        print(matrix[i][j],end = " ")
    print("\n")    