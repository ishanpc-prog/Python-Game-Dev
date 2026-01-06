list1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
x = 0
print("The diagonal entries will now be shown under this sentence.")
for i in range(0,4):
    print(list1[i][i])
    x = x + list1[i][i]   
print("The sum is " + str(x) + ".")