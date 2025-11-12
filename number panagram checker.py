numbers_input = str(input("Enter number: "))
numbers = {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}
for n in numbers_input:
    if n in numbers:
        numbers[n] = numbers[n] + 1
print(numbers)

p = True
for i in numbers.values():
    if i == 0:
        p = False
if p == True:
    print("It contains all the numbers.")
else:
    print("It doesn't contain all numbers.")            