def panagram_check(text):
    s1 = set("abcdefghijklmnopqrstuvwxyz")
    s2 = set()
    for alphabet in text:
        if alphabet.isalpha():
            s2.add(alphabet)
    print(s2)        
panagram_check("Hello World")
