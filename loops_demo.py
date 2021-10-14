"""
    1-100 arasındaki rastgele üretilecek bir sayıyı aşağı yukarı ifadeler ile buldurmaya çalışın
    ** "random modülü" için "python random" şeklinde arama yapın
    ** 100 üzerinden puanlama yapın. Her soru 20 puan.
    ** Hak bilgisini kullanıcılardan alın ve her soru belirtilen can sayı üzerinden hesaplansın. (Hak=5)
"""

import random

sayi = random.randint(1, 100)
hak = 5
sayac = 0

while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input("Tahmin: "))

    if sayi == tahmin:
        print(f"Tebrikler {sayac}.defada bildiniz. Toplam puanınız {100 - (20)* (sayac-1)} ")
        break
    elif sayi > tahmin:
        print("Yukarı")
    else:
        print("Aşağı")

    if hak == 0:
        print(f"Hakkınız bitti. Tutulan sayı: {sayi}")

### Hak bilgisini kullanıcıdan alırsak

import random

sayi = random.randint(1, 100)
can = int(input("Kaç hak kullanmak istersiniz : "))
hak = can
sayac = 0

while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input("Tahmin: "))

    if sayi == tahmin:
        print(f"Tebrikler {sayac}.defada bildiniz. Toplam puanınız {100 - (100/can)* (sayac-1)} ")
        break
    elif sayi > tahmin:
        print("Yukarı")
    else:
        print("Aşağı")

    if hak == 0:
        print(f"Hakkınız bitti. Tutulan sayı: {sayi}")
