class Student:
    def __init__(self,name,birthdate,nameofschool,agegroup):
        self.name = name
        self.agegroup = agegroup
        self.birthdate = birthdate
        self.nameofschool  = nameofschool
    def greet(self):
        print("Hello my name is " + self.name + ".")
        print("My age group is " + self.agegroup + ".")
        print("My birthdate is the " + self.birthdate + ".")
        print("The name of my school is " + self.nameofschool + ".")
        print("")
        print("")

person1 = Student("Billybob", "12.04.2011", "Local School", "Year 9")
person1.greet()

person2 = Student("Bibi", "31.12.2010", "Local School", "Year 10")
person2.greet()

person3 = Student("Josh", "12.07.2015", "Private School", "Year 5")
person3.greet()

person4 = Student("Lily", "20.05.2013", "Private School", "Year 7")
person4.greet()