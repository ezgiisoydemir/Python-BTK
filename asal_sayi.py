
"""
Girilen sayının asal olup olmadığını bulun
** Asal sayı 1 ve kendisi hariç tam böleni olayan sayılara denir
"""

sayi= int(input("sayi:"))
asalmi = True

if sayi == 1:
    asalmi = False

for i in range(2,sayi):
    if (sayi % i == 0):
        asalmi = False     
        break

if asalmi:
    print("Sayi asaldır")

else:
    print("Sayı asal değil")
