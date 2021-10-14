# error => Hata
 
# print(a) => NameError
# int ("1a2") => ValueError
# print(10/0) => ZeroDivisionError              DİVİSİON = BÖLÜNME             
# print("denem"e) => SyntaxError                SYNTAX = SÖZDİZİMİ


# error handling => hata yönetimi 

try:
    x = int(input("x : "))
    y = int(input("y : "))
    print(x/y)                      # İkinci sayıyı sıfıra bölersek zerodevision hatası verir.
except ZeroDivisionError:
    print("y için sıfır girilemez")
except ValueError:
    print("x ve y için sayısal değer girmelisiniz")

""""
Hata yakalama, yazdığımız beklenmedik durumlarda karşılaşacağımız hatalarda programın hata vermesi
 ya da kendini durdurması yerine hataya kendi istediğimiz şekilde cevap vermesini sağlama durumudur. 
 Hata yakalama program yazmanın önemli bir parçasıdır. 
 Python’da hata yakalamayı try – except blokları ile yapıyoruz.
"""

## Yukarıdaki örneği hataları bir arada yazarak da kullanabiliriz
try:
    x = int(input("x : "))
    y = int(input("y : "))
    print(x/y)                      # İkinci sayıyı sıfıra bölersek zerodevision hatası verir.
except (ZeroDivisionError , ValueError) as e:
    print("Yanlış Bilgi Girdiniz") 
    print(e)                        # Hangi hata olduğunu ekrana basar

## Yukarıdaki örneği hataları yazmayarak da kullanabiliriz
try:
    x = int(input("x : "))
    y = int(input("y : "))
    print(x/y)                      
except :
    print("Yanlış Bilgi Girdiniz")
else:
    print("Her şey yolunda") 

# Yukarıdaki örneği hataları yazmayarak ve while kullanarak da çalıştırabiliriz
while True:
    try:
        x = int(input("x : "))
        y = int(input("y : "))
        print(x/y)                      
    except Exception as ex:                         # Hataların genel ismini yazdık
        print("Yanlış Bilgi Girdiniz" , ex)
    else:                                           # Programın çalışma mantığı doğru girene kadar x ve y sorar
        break                                       # eğer doğruysa else bloğunu görür ve programı bitirir
    finally:
        print("try except sonlandı")                # Kaynakların kapatılması için yazılır
                                                    # Else bloğu burada geçersiz olur





