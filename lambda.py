# Lambda fonksiyon tanımlamak için kullanılır
# Lambda fonksiyonlarını, bir fonksiyonun işlevselliğine ihtiyaç duyduğumuz, ama konum olarak bir fonksiyon tanımlayamayacağımız 
# veya fonksiyon tanımlamanın zor ya da meşakkatli olduğu durumlarda kullanabiliriz

# Sayının karesini alma
def square(num):return num**2
result = square(2)
print(result)

# Listedeki sayıların karesini alıp yazdırma
numbers = [1,3,5,9]                                     # Buradaki map metodu ya bir listeyle ya da for döngüsü içinde yazılmalı
result = list(map(square,numbers))                      # Yani her bir eleman tek tek dönmeli ki çalışsın
print(result)

for item in map(square,numbers):
    print(item)

# Fonksiyonu lambda ile denemek istersek
numbers = [1,3,5,9]
result = list(map(lambda num : num**2,numbers))         # Lambda anonymous(anonim) bir fonksiyon tanımladık.
print(result)                                           # Herhangi bir return kullanmadan fonksiyonu çalıştırdık.

# Yaptığımız işleme bir değişkenşn içine atıp isim de verebiliriz
square = lambda num : num**2         
numbers=[1,3,5,9]
result = square(3)                   
print(result)

# Filtre işlemi yapmak istersek
numbers = [1,3,5,9,10,4]

def check_even(num):                                     # Return = Gönderdiğimiz sayının modunu al.    
    return num%2==0                                      # Eğer sonuç sıfırsa geriye TRUE değeri gönder
                                                         # Eğer tek ise yani sonuç birse geriye FALSE değeri gönder
result = list(filter(check_even,numbers))                # Filter methodu içerisine fonksiyonu gönder = check_even                                      
print(result)                                            # Numbers lar üzerinde işlem yapsın
                                                         # Sonuç = [10,4] Tek sayılar gelmemiş oldu

# Bir önceki örneği lambda ile yapmak istersek
result = list(filter(lambda num:num%2==0,numbers))  
print(result)                                            # Sonuç yine [10,4] çıkar           

# Yaptığımız işleme bir değişkenin içine atıp isim de verebiliriz
check_even = lambda num:num%2==0
result = list(filter(check_even,numbers))
print(result)

# Doğruluğunu kontrol etmek istersek
check_even = lambda num:num%2==0
result =check_even(numbers[2])                             # Numbers listesindeki ikinciyi sayıyı kontrol edersek
print(result)                                              # Sonuç FALSE. Çünkü 5 tek sayı