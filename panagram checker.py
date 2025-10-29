word = str(input("Enter String")).lower()
letters = {}
for c in word:
    if c.isalpha():
        if c in letters:
            letters[c] = letters[c] + 1 #increasing the value count of a letter which  is also in the dictionary
        else:
          letters[c] = 1 
print (letters)           