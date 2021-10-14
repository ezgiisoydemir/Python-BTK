## Bellekte yer işgal etmeyen iterators anlamına gelir

# Burada listedeki veriler bir yerde saklanıyor 
from typing import Iterator


def cube():
    result = []

    for i in range(5):
        result.append(i**3)
    return result

print(cube())

# Eğer biz bu listedeki değerleri saklamak istemez ve sadece ekrana yazılmasını istersek
#### YIELD = TESLİM OLMAK , VERİM , ÜRÜN
## Python’da en kolay şekilde bir generator oluşturma return yerine yield ifadesini kullanmaktır.
# Eğer bir fonksiyon yield ifadesi içeriyorsa bir generator fonksiyonu haline dönüşür. 
# Aslında bir fonksiyonda yield ve return ifadesi aynı değeri döndürür. 
# Ancak, return ifadesi bir fonksiyonu sonlandırırken, yield ifadesi değeri döndürür, saklar ve fonksiyonu çağırma devam eder.

## Örneği inceleyip, yukarıdaki maddeleri tekrar okuyalım. 
# i değeri her çağırma işleminde (next) yield bölümüne kadar fonksiyon çalışır.
# Burada duraklar ve yeni bir çağırma bekler. Yeni çağırmada tekrar çalışır. 
# Durum kalmayıncaya kadar işlem devam eder. Ve durum kalmayınca bir StopIteration oluşur.

def cube():
    for i in range(5): 
        yield i**3

generator = cube()
iterator = iter(generator)

print(cube())
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator)) 

## Bunu iteratoru cube e eşitleyrek de yapabiliriz
def cube():
    for i in range(5):
        yield i**3

iterator = cube()

print(cube())
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator)) 

##
def cube():
    for i in iterator:
        print(i)

## Buradaki listeyi generator haline getirmek istiyorsak değişmesi gereken tek şey köşeli parantez
liste = [i**3 for i in range(5)]
print(liste)

liste = (i**3 for i in range(5))
print(liste)
""" Çıktı almak için birinci yol """
print(next(liste))
print(next(liste))
print(next(liste))

""" Çıktı almak için ikinci yol """
for i in generator:
    print(i)