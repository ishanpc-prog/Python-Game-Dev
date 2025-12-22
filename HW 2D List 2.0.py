row = int(input("Enter the number of rows: "))
column = int(input("Enter the number of columns: "))
list1 = []
print("Enter the matrix elements row by row: ")
for i in range(row):
    smth = []
    for j in range(column):
        x = int(input("Element " + "[" + str(i) + "]" + "[" + str(j) +"]" + " = "))
        smth.append(x)
    list1.append(smth)
print("")
for i in range(0,row):
    for j in range(0,column):
        print(list1[i][j],end = " ")
    print("\n")