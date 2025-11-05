word = str(input("Enter String ")).lower()
letters = {}
for c in word:
    if c.isalpha():
        if c in letters:
            letters[c] = letters[c] + 1 #increasing the value count of a letter which  is also in the dictionary
        else:
          letters[c] = 1 
print (letters)

p = True
for i in letters.values():
    if i == 0:
        p = False
if p == False:
    print("It isn't a panagram.")
else:
    print("It is a panagram")    