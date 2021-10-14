# ÖRNEK 1
for x in range(10):
    print(x)

numbers = [x for x in range(10)]            # For döngüsü ile yazdırdığımız range i bir x değişkenine attık. Sonra bunu list halinde yazdırdık
print(numbers)                              # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers = []                                  # Bu kısımda bir dizi tanımladık
for x in range(10):                           # Dizi içerisinde elemanları range içerisinden teker teker aldık ve append ettik
    numbers.append(x)
print(numbers)                                # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# ÖRNEK
for x in range(10):
    print(x**2)

numbers =[x**2 for x in range(10)]            # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(numbers)

numbers =[x*x for x in range(10)]             # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(numbers)

numbers =[x*x for x in range(10) if x % 3 == 0]             # Sadece 3'e bölünenleri yazdırmak istersek = [0, 9, 36, 81]
print(numbers)

# ÖRNEK
myString = "Hello"
myList = []                                    # Listeye çevirmek için                     

for letter in myString:
    myList.append(letter)
print(myList)                                  # ['H', 'e', 'l', 'l', 'o']             

""" Daha kısa yoldan yapmak istersek """

myList = [letter for letter in myString]
print(myList)

# ÖRNEK
years = [1983 , 1999 , 2008 , 1956 , 1986]
ages = [2021-year for year in years]
print(ages)

result = [x if x%2 == 0 else "TEK" for x in range(1,10)]        # Çift olduğunda kendini liste içine dahil eder. Tek olduğunda ise TEK yazar
print(result)                                                   # ['TEK', 2, 'TEK', 4, 'TEK', 6, 'TEK', 8, 'TEK']

# ÖRNEK
result = []
for x in range(3):                                              # İlk önce y'nin içindeki biter daha sonra x arttırılır
    for y in range(3):
        result.append((x,y))
print(result)                                                   # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

""" Daha kısa yoldan yapmak istersek """

numbers = [(x,y) for x in range(3) for y in range(3) ]          
print(numbers)                                                  # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

numbers = [(x,y,z) for x in range(3) for y in range(3) for z in range(3)]
print(numbers)
























