marks = [71, 9, 44, 82, 13, 98, 25, 60, 3, 55, 38, 87, 16, 92, 49, 6, 77, 34, 21, 64]
marks.sort()
print("")

list1 =[x for x in marks if 0 <= x <= 30]
list2 = [x for x in marks if 31 <= x <= 69]
list3 = [x for x in marks if 70 <= x <= 100]

list1.sort()
list2.sort()
list3.sort()

print("Original list:")
print(marks)
print("")
print("First list:")
print(list1)
print("")
print("Second list:")
print(list2)
print("")
print("Third list:")
print(list3)
print("")
# use random pls