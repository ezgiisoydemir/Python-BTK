# numbers = [1,2,3,4,5]
# for x in numbers:       # Liste eleman sayısı kadar for döngüsü döner
#     print(x)

names = ["Gizem","Ezgi","Sevgi"]
for name in names:
    print(f"my name is {name}")

name = "Ezgi Soydemir"      # stringler de liste gibidir.Tüm ismi yukarıdan aşağıya kadar tek tek yazar.
for n in name:
    print(n)

tuple = [(1,2),(1,3),(3,5),(5,7)]       #Her liste elemanı bir  tuple listesine karşılık geliyor
for t in tuple:                         #Sonuç kümelerin alt alta sıralanmış hali
    print(t)

tuple = [(1,2),(1,3),(3,5),(5,7)]       #Her liste elemanı bir  tuple listesine karşılık geliyor
for a,b in tuple:                       #Sonuç sadece kümenin ilk elemanlarının sıralanmış hali
    print(a)

tuple = [(1,2),(1,3),(3,5),(5,7)]       #Her liste elemanı bir  tuple listesine karşılık geliyor
for a,b in tuple:                       #Sonuç küme elemanlarının ayrı halde sıralanmış hali
    print(a,b)

d = {"k1":1 ,"k2":2 ,"k3":3 }

for item in d:                          #Sadece key bilgilerini ekrana yazdırır
    print(item)

for item in d.items():                  #.items eklediğimizde eleman gruplarına tek tek ulaşırız
    print(item)

for key,value in d.items():             #key ve dictionary leri ayrı ayrı ekrana yazdırır
    print(key,value)






