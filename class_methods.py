# class

class Person:
    #class attributes
    address = "no information"

    #constructor (yapıcı metod)
    def __init__ (self, name, year): 

    #object attributes
        self.name = name
        self.year = year
    print("init metodu çalıştı")

    # instance methods 
    def intro(self):
        print("Hello There. I am "+ self.name )

    def calculateAge(self):
        return 2021-self.year

    

# object (instence)
p1 = Person(name="Ali", year=1990)
p2 = Person(name="Ahmet", year=1995)

p1.intro()
p2.intro()

print(f"adım: {p1.name} ve yasım: {p1.calculateAge()}")
print(f"adım: {p2.name} ve yasım: {p2.calculateAge()}")

#---------------------------------------------------------------------------------------------------

