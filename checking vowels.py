vowels_input = str(input("Enter string."))
vowels = {"a":0,"e":0,"i":0,"o":0,"u":0}
for v in vowels_input:
    if v in vowels:
        vowels[v] = vowels[v] + 1
print(vowels)

p = True
for i in vowels.values():
    if i == 0:
        p = False
if p == True:
    print("It contains all the vowels.")
else:
    print("It doesn't contain all vowels.")            
