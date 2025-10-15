dict_1 = {"Flower":"a plant","Car":"a vehicle","Bird":"a animal","Chair":"a piece of furniture"}
print(dict_1)
for key in dict_1:
    print(key + ":" + dict_1[key])
#we respresent the value by writing name of the dictionary and inside of the sqare brackets write the name of the key whose value we want to know
input_key = str(input("What is the key you want to write? "))
input_value = str(input("What is the value you want to write? "))
dict_1[input_key] = input_value
print(dict_1)