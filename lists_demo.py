# 1. "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
liste = ["Bmw","Mercedes","Opel","Mazda"]

# 2. Liste kaç elemanlıdır?
len=len(liste)

# 3. Listenin ilk ve son elemanı nedir?
a = liste[0]
b =liste[-1]

# 4. Mazda değerini Toyota ile değiştirin
liste[-1] = "Toyota"
result = liste

# 5. Mercedes listenin bir elemanı mıdır?
result = "Mercedes" in liste

# 6. Listenin -2 indeksindeki değer nedir?
result = liste[-2]

# 7. Listenin ilk üç elemanını alın.
result = liste[:3]
result = liste[0:3]
result = liste[-2:]

# 8. Listenin son 2 elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin
liste[-2:] = ["Toyota" , "Renault"]

# 9. Listenin üzerinde "Audi" ve "Nissan" değerlerini ekleyin
liste = liste + ["Audi" , "Nissan"]

# 10. Listenin son elemanını silin
liste[-2:] = [ ]
result = liste

del liste[-1]
result = liste

# 11. Liste elemanlarını tersten yazın
result = liste[::-1]

# 12. Aşağıda verilenleri bir liste içinde saklayın

     # studentA: Yigit Bilgi 2010, (70,60,70)
     # studentB: Sena Turan 1999,  (80,80,70)
     # studentC: Ahmet Turan 1998, (80,70,90)
    
studentA = ["Yigit", "Bilgi", 2010, [70,60,70]]
studentB = ["Sena", "Turan", 1999, [80,80,70]]
studentC = ["Ahmet", "Turan", 1998, [80,70,90]]

# 13. Liste elemanlarını ekrana yazdırın.

result = studentA[0]
result = studentB[1]
result = studentC[3][1]

result=f"{studentA[0]} {studentA[1]} {2020-studentA[2]} yaşında ve not ortalaması {(studentA[3][0]+studentA[3][1]+studentA[3][2])/3}"

print(result)
