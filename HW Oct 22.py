letters_input = str(input("Enter string."))
letters = {"a":0,"d":0,"h":0,"i":0,"r":0}
for l in letters_input:
    if l in letters:
        letters[l] = letters[l] + 1
print(letters)

p = True
for i in letters.values():
    if i == 0:
        p = False
if p == True:
    print("Tested Correct.")
else:
    print("Tested False.")            