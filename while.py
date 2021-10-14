numbers = [1,2,3,4,5]

#1'den 100'e kadar sayıları ekranda yazdırmak istersem

x = 0
while x < 100 :
    print(x)
    x = x + 1
print("bitti...")

x = 1
while x <= 100 :
    print(x)
    x += 1
print("bitti...")

x = 1
while x <= 100 :
    if x % 2 == 0:              # Eğer belli bir koşulda bunları yazdırmak istersek. Örneğin 1'den 100'e kadar 2'ye bölünenler
        print(x)
    x += 1
print("bitti...")

x = 1
while x <= 100 :
    if x % 2 == 1:              #  1'den 100'e kadar olan tek sayıların yazımı
        print(x)
    x += 1
print("bitti...")

x = 1
while x <= 100 :
    if x % 2 == 1:              #  1'den 100'e kadar olan tek ve çift sayıların ayrı ayrı yazımı
        print(f"sayı tek: {x}")
    else:
        print(f"sayı çift: {x}")
    x += 1
print("bitti...")

name = "" #False
while not name:
    name = input("isminizi giriniz: ")
print(f"merhaba, {name}")
















