print("Task 1")
students_dict = {"Bob": 12,"Laura": 14,"Billy": 13}
print(students_dict)
students_dict["Sarah"] = 11
print(students_dict) 
print("")

print("Task 2")
fruits = {"apple":10,"banana":5,"orange":8}
print(fruits)
banana_fruit = fruits["banana"]
fruits["apple"] = 15
del fruits["orange"]
print(fruits)
print("")

print("Task 3")
dict_3 = {"flower":"a plant","bonsai":"a tree","BMW":"a car brand","diamond":" a metall","blue":"a color"}
search = str(input("What is the name of key you are searching?"))
if search in dict_3:
    print("Your searched word is in the dictionary!")
else:
    print("Your searched word hasn't been found")
print("")

print("Task 4")
dict_4 = {"flower":"a plant","bonsai":"a tree","BMW":"a car brand","diamond":" a metall","blue":"a color"}
print(dict_4)
len_dict = len(dict_4)
print(len_dict)
print("")
