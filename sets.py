fruits = { "orange", "apple", "banana"}

#print(fruits[0]) indekslenemez. örneğin 1. elemanı bu şekilde öğrenemezsin

for x in fruits: # liste içerisindeki her bir elemanı sırayla xin yerine kopyalayıp yazıyor.
    print (x)    #Bu şekilde listedeki tüm ürünler alt alta sıralanıyor

fruits.add("charry") # listeye yeni eleman ekleme

fruits.update(["mango","grape"]) # listeye birden fazla eleman ekleme - Aynı elemanı da yazsak 2.kez o elemanı listede göstermiyor

fruits.remove("mango") #listede eleman silme

fruits.discard("apple") #aynı şekil eleman siler

fruits.pop() #normalde en son eleman silinir fakat bu string olmadığından son elemanın hangisi olduğu belli değildir

fruits.clear() #tüm elemanlar silinir              

print(fruits)

myList = [1,2,5,4,4,2,1]
print(set(myList)) #set ile yazarsak listede tekrar eden elemanlar 1 kez gözükür
