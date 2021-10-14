from raise import check_password
import re

liste = ["1" , "2" , "5a" , "10b" , "abc" , "10" , "50"]

# 1: Liste elemanları içindeki sayısal değerleri bulunuz

for x in liste:
    try: 
        result = int(x)
        print(result)
    except ValueError:
        continue

# 2: Kullanıc 'q' değerini girmedikçe aldığınız her inputun sayı
#    olduğundan emin olunuz aksi halde hata mesajı yazın

while True:
    sayi = input("sayi: ")
    if sayi == "q" :
        break

    try:
        result = float(sayi)
        print("Girdiğiniz sayi: " , result)
        break
    
    except ValueError:
        print("Geçersiz Sayı : ")
        continue

# 3: Girilen parola içinde türkçe karakter hatası veriniz

def checkPAssword(parola):
    turkce_karakterler = "şçğüöıİ"

    for i in parola:
        if i in turkce_karakterler:
            raise TypeError("Parola türkçe karakter içeremez")
        else:
            pass
    print("Geçerli Parola")

parola = input("parola: ")
try:
    checkPAssword(parola)

except TypeError as err:
    print(err)

# 4: Faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajı veriniz 

def faktoriyel(x):
    x = int(x)

    if x < 0:
        raise ValueError("Negatif Değer")

    result = 1

    for i in range( 1, x+1):
        result *= i
    
    return result

for x in [5,10,20,-3,"10a"]:
    try:
        y = faktoriyel(x)
    except ValueError as err:
        print(err)
        continue
    print(y)





