t1 = ("Billybob",1,1,1)
print(t1)
# packing 
address = (12,"Liverpool","Bavaria","Latvia")
for i in address:
    print(i)
#unpacking
housenumber,town,state,country = address
print(housenumber)
print(town)
print(state)
print(country)    
# a tuple can be craeted without the brackets 
# nested tuple 
t2 = (1,(1,2,3))
print(t2[1])
print(t2[1][2])