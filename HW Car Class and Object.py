class Car:
    def __init__(self,companyname,foundingyear,founder,foundingcountry):
        self.companyname = companyname
        self.foundingyear = foundingyear
        self.founder = founder
        self.foundingcountry = foundingcountry
    def greet(self):
        print("Company name of the car: " + self.companyname)
        print("Founding year of the company: " + self.foundingyear)
        print("Founder of the company: " + self.founder)
        print("Founding country of the car: " + self.foundingcountry)
        print("")
        print("")

car1 = Car("Mercedes-Benz","1926","Carl Benz und Gottlieb Daimler","Germany")
car1.greet()

car2 = Car("Toyota","1937","Kiichiro Toyoda","Japan")
car2.greet()

car3 = Car("Ford","1903","Henry Ford","United States of America")
car3.greet()

car4 = Car("Ferrari","1939","Enzo Ferrari","Italy")
car4.greet()