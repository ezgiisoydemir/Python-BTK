"""
x = input ("1.Sayi: ")
y = input ("2.Sayi: ")
# Bu sekilde sistem sayiyi string alir! Ilk once int haline getirmen lazim

toplam = int(x) + int (y)

print(toplam)

"""

x=5                 #int
y=2.5               #float
name="Çınar"        #str
isOnline = True     #bool

#Type Conversion

#int to float

x = float(x)
print(x)
print(type(x))

y = int(y)
print(y)
print(type(y))

result = str(x) + str (y)
print(result)
print(type(result))

#bool to str

isOnline = str(isOnline)
print(isOnline)       #Sonuc sadece ekrana True yazar
print(type(isOnline))

#bool to int

isOnline = False

isOnline = int(isOnline)
print(isOnline)       # snucu 0 verir cunku false
print(type(isOnline))



