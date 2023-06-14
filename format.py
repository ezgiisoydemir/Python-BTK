name = "Ezgi"
surname = "Soydemir"
age =22

print("My name is {} {}" .format(name,surname))
# My name is Ezgi Soydemir

print("My name is {0} {1}" .format(name,surname))
# name index 0 , surname index 1
# My name is Ezgi Soydemir

print("My name is {1} {0}" .format(name,surname))
# Index yerlerini degistirdik
# My name is Soydemir Ezgi 

print("My name is {s} {n}" .format(n=name,s=surname))
# My name is Soydemir Ezgi 

print("My name is {} {} and I'm {} years old" .format(name,surname,age))
# My name is Ezgi Soydemir and i am 22 years old

result = 200/700
print("the result is {r:1.3}".format(r=result))
# 1'i yazmamızın nedeni tam kısımdan önce ne kadar boşluk kalacağını belirlemek
#3 ise virgülden sonra kaç basamak yazacağımızı belirlemek 

#Fstring
print(f"My name is {name} {surname} and I'm {age} years old.")
