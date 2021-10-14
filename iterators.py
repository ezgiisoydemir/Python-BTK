from typing import Iterator


liste = [1,2,3,4,5]

## For döngüsü bizim yerimize iterable objeden bir iterator oluşturabiliyor
for i in liste:
    print(i)

## Bu fonksiyon, Python’da bize nesnelerin özellikleri hakkında bilgi edinme imkanı sağlar.
print(dir(liste))


## Listedekileri baştan sona aşağıdan yukarı bir şekilde yazar
## For döngüsünden farklı değil. Sadece farklı bir method. For döngüsünün arkasında dönen bir senaryodur
liste = [1,2,3,4,5]

iterator = iter(liste)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

##---------------------------------------------------

iterator = iter(liste)

while True:
    try:
        element = next(iterator)
        print(element)
    except StopIteration:
        break

## ----------------------------------------------------

## Bunu yapmaktaki amacımız list gibi bir sınıfı kendimiz oluşturmak istememiz

class MyNumbers:
    def __init__(self,start,stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration

list = MyNumbers(10,20)

for x in list:
    print(x)
        
         
    