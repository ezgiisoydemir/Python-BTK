# global scope
x = "global x"

def function():
    # local scope
     x = "local x"
     print(x)

function()                                          # Kod sonucunda  ilk önce local x daha sonra global x yazar
print(x)                                            # İlk önce fonksiyonun içindekini yazar

#-----------------------------------------------------------------------------------------------------------------

name = "Ezgi"

def changeName(new_name):
    name=new_name
    print(name)

changeName("Sevgi")
print(name)

#--------------------------------------------------------------------------------------------------------------

name = "Global String"

def greeting():
    name = "Ezgi"

    def hello():
        print("Hello" + name)

    hello()
greeting()

#------------------------------------------------------------------------------


name = "Global String"

def greeting():
   # name = "Ezgi"

    def hello():
        #name = "Sevgi"
        print("Hello" + name)

    hello()
greeting()                                                      # Sonuç Hello Global String 

#---------------------------------------------------------------------------------------------------------

x = 50
def test(x):
    print(f"x : {x}")

    x=100
    print(f"changed x to : {x}")                            

test(x)
print(x)                                                        #x : 50
                                                                #changed x to : 100
                                                                #50

#------------------------------------------------------------------------------------------------------

# Eğer bir önceki örnekteki x 50 değerini fonksiyon içinde de değiştirmek istersek

x = 50
def test():
    global x
    print(f"x : {x}")

    x=100
    print(f"changed x to : {x}")                            

test(x)
print(x)                                                        #x : 50
                                                                #changed x to : 100
                                                                #100
















