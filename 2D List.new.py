matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
print(len(matrix)) #this instruction shows you the number of rows in your 2d list
print(len(matrix[0])) #this is to know the number of columns
print(matrix[2][2]) #acessing an element in 2d list
for i in range(0,len(matrix)):
    for j in range(0,len(matrix[0])):
        print(matrix[i][j],end = " ")
    print("\n") 

# take input for a matrix and print the elements

row = int(input("How many rows do you want? "))
column = int(input("How many columns do you want? "))
matrix1 = [] 
for i in range(row):
    temp = []
    for j in range(column):
        x = int(input("What number do you want to add? "))
        temp.append(x)
    matrix1.append(temp)
for i in range(0,row):
    for j in range(0,column):
        print(matrix1[i][j],end = " ")
    print("\n")
