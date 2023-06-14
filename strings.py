name = "Ezgi"
surname = "Soydemir"
age=22

greeting = "My name is " + name + " " + surname + " and \nI am "+ str(age) + " years old"
print(greeting)

length = len(greeting)
print(greeting[0])
print(greeting[3])
print(greeting[length-1]) #Sonn karakteri aldik. 0'dan basladigi icin 1 eksiltmek gerek
print(greeting[-1])
print(greeting[3:7])  #3'ten baslar ve 7.index'e kadar gider. Sonuc => name
print(greeting[3:])   #3'ten basla sonuna kadar git
print(greeting[:15])    #Bastan basla 15.karaktere kadar git
print(greeting[2:40:2])   #2'den 40'a kadar git. Ama 2 karakterde birini al
print(greeting[2:40:3])   #3 karakterden birini alir
