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
    #methods 

# object (instence)
p1 = Person(name="Ali", year=1990)
p2 = Person(name="Ahmet", year=1995)

# updating
p1.name = "Arda"
p1.address = "İstanbul"

# accessing object attributes
print(f"p1 name: {p1.name} year:{p1.year} address: {p1.address}")
print(f"p1 name: {p1.name} year:{p1.year} address: {p1.address}")

print(p1)
print(p2)
print(type(p1))
print(type(p2))