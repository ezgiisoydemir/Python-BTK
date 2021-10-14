try:
    file = open("newfile.txt" , "r")
    print(file)
except FileNotFoundError:
    print("Dosya okuma hatası")


try:
    file = open("nemfile.txt" , "r")
    print(file)
except FileNotFoundError:
    print("Dosya okuma hatası")
finally:
    print("Dosya kapandı")
    file.close()

file = open("newfile.txt", "r" ,encoding="utf-8")

# For döngüsü ile okuma

for i in file:
    print(i)

file.close()

# read() fonksiyonu ile okuma
content = file.read()
print(content)
file.close()

""" Örnek 1 """
content1 = file.read()
print("içerik 1")
print(content1)

file = open("newfile.txt", "r" ,encoding="utf-8")
content2 = file.read()
print("içerik 2")
print(content2)

file.close()

""" Örnek 2 """
content = file.read(5)                  # Dosya içindeki ilk 5 kelimeyi okur
content = file.read(3)                  # İkinci okumada bir öncekine ekleme yapar. Sıfırdan başlamaz 
print(content)
file.close()

# readline() fonksiyonu ile okuma
#   *** readline() fonksiyonu her seferinde bir satır okur

file.readline()
file.close()

# readlines() fonksiyonu ile okuma
#   *** Hersatırdaki bilgiyi dizi elemanları şeklinde yazar  
        
liste = file.readlines()
print(liste[0])
print(liste[1])
print(liste[2])

file.close()




