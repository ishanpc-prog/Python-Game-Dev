marks = [62, 14, 88, 3, 91, 55, 27, 49, 75, 10, 80, 5, 33, 97, 21, 68, 42, 7, 50, 19]
marks.sort()
print("")

list_0_to_30 =[x for x in marks if 0 <= x <= 30]
list_31_to_69 = [x for x in marks if 31 <= x <= 69]
list_70_to_100 = [x for x in marks if 70 <= x <= 100]

list_0_to_30.sort()
list_31_to_69.sort()
list_70_to_100.sort()

print("This is the original list:")
print(marks)
print("This is the first list:")
print(list_0_to_30)
print("This is the second list:")
print(list_31_to_69)
print("This is the third list:")
print(list_70_to_100)