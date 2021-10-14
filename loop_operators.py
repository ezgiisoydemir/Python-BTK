# RANGE
liste = [1,2,3]

for item in liste:
    print(item)

for item in range(10):          # Liste yerine range yazarız. Range sayıları 1'den 10'a kadar yazdırır
    print(item)

for item in range(2,10):        # 2'den başlar 10'a kadar gider
    print(item)


for item in range(50,100,10):       # 50den başlar 100 e kadar 10 ar 10ar artarak ilerler
    print(item)

print(list(range(5,100,10)))            #Range'i list'e çevirdik

# ENUMERATE

greeting = "Hello There"
for letter in greeting:
    print(letter)

index = 0
greeting = "Hello"
for letter in greeting:
    print(f"index: {index} letter: {letter}")
    index += 1

"""YUKARIDAKİYLE AYNI ÖRNEK SADECE LETTER'I FARKLI ŞEKİLDE YAZDI """
index = 0
greeting = "Hello"
for letter in greeting:
    print(f"index: {index} letter: {greeting[index]}")
    index += 1

"""ENUMERATE İLE YAZIMI"""
greeting = "Hello"
for index,letter in enumerate(greeting):
    print(f"index: {index} letter: {letter}")

# ZİP

""" İki listeyi birleştirmek istiyorum"""

list1 = [1,2,3,4,5]
list2 = ["a","b","c","d","e"]
list3 = [100,200,300,400,500]

print(list(zip(list1,list2)))              # Birleştirdiğim listeleri tekrar list halinde yazmasını istiyorum
                                           # Sonuç [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]

print(list(zip(list1,list2,list3)))        # Sonuç [(1, 'a', 100), (2, 'b', 200), (3, 'c', 300), (4, 'd', 400), (5, 'e', 500)]

for item in zip(list1,list2,list3):
    print(item)                            # (1, 'a', 100)
                                           # (2, 'b', 200) 
                                           # (3, 'c', 300) 
                                           # (4, 'd', 400)
                                           # (5, 'e', 500)
                               
""" Her bir elemana ulaşmak istersek """

for a,b,c in zip(list1,list2,list3):
    print(a)                               # Sadece list1'deki elemanlar sıralanır











