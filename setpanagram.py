def panagram_check(text):
    s1 = set("abcdefghijklmnopqrstuvwxyz")
    s2 = set()
    text = text.lower()
    print("There are " + str(len(text)) + " alphabets in this statement of yours.")
    for alphabet in text:
        if alphabet.isalpha():
            s2.add(alphabet)
    print((s2)) 
    if s2 == s1:
        print("It is a panagram.")
    else:
        print("It is not a panagram.")
panagram_check(str(input("What is the panagram you wish to write? ")))