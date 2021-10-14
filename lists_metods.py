numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ["a", "g", "s", "b", "y", "a", "s"]

val = min(numbers)
val = max (numbers)

val = min(letters)
val = max (letters)

val = numbers[3:9]
val = numbers[:3]
val = numbers[4:]

numbers[4] = 40

numbers.append(49) #listenin üzerine sayı eklemek - En sona ekler

numbers.insert(3,78) #listedeki üçüncü elemandan önce 78 eklenir - [1, 10, 5, 78, 16, 40, 9, 10, 49]
numbers.insert(-1,52) #listenin sondan birincisinin önüne 52 ekler - [1, 10, 5, 78, 16, 40, 9, 10, 52, 49]

numbers.pop() # Son rakamı siler - [1, 10, 5, 78, 16, 40, 9, 10, 52]
numbers.pop(0) #[0]daki eleman silinir
numbers.pop(-1) # Sondaki sayı silinir

numbers.remove(49) # 49 Rakamını listeden bul ve onu sil

numbers.sort() # listedeki sayıları küçükten büyüğe sıralar
letters.sort() #listedeki harfleri alfabetik sıralar

numbers.reverse() #listedeki sayıları büyükten küçüğe sıraladı
letters.reverse() #listedeki harfleri ters alfabetik olarak sıralar

print(len(numbers))
print(len(letters))

print(numbers.count(10))
print(letters.count("a"))

numbers.clear() # Tüm elemanları silmek için kullanılır

print(numbers)