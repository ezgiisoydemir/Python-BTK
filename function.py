# def sayHello():
#     print("Hello")
#                                      #Ekrana fonksiyonla hello yazdık. Çalıştırmak için son satırı eklemek gerek
# sayHello()                           # Son satır fonksiyonu çağırmak ve uygulamak için kullanılır

#-----------------------------------------------------------------------------------------------------------------#

# def sayHello(name):                     # Dışarıdan name parametresi alıyor
#     print("Hello " + name)              # Dışarıdan fonksiyona ne gönderilirse name yerine o yazılacak
# sayHello("Ezgi")                        # Hello Ezgi yazar
# sayHello("Sevgi")                       # Hello Sevgi yazar

#-----------------------------------------------------------------------------------------------------------------#

# def sayHello(name = "user"):              # Eğer isim yazmazsak Hello user yazar.      
#     print("Hello " + name)              
# sayHello()

#-----------------------------------------------------------------------------------------------------------------#

# def sayHello(name = "user"):                  
#     return "Hello " + name                  # İfadenin fonksiyona geriye gönderilmesini sağlarız return ile  

# msg = sayHello("Ezgi")            
# print(msg)

#-----------------------------------------------------------------------------------------------------------------#

def total(num1,num2):
    return num1+num2

result = total (10,20)
print(result)

#-----------------------------------------------------------------------------------------------------------------#

def yasHesapla(dogumyili):
    return 2021 - dogumyili

ageGizem = yasHesapla(1995)
ageEzgi = yasHesapla(1998)
ageSevgi= yasHesapla(2006)

print(ageGizem,ageEzgi,ageSevgi)

#-----------------------------------------------------------------------------------------------------------------#

def EmekliligeKacYilKaldi(dogumyili,isim):
    """
    DOCSTRİNG: Dogum yiliniza gore emekliliginize kac yil kaldi
    INPUT: Dogum yili
    OUTPUT: Hesaplanan yil bilgisi

    """


    yas = yasHesapla(dogumyili)
    emeklilik = 65 - yas

    if emeklilik > 0 :
        print(f"emekliliğinize {emeklilik} yil kaldı")
    else:
        print("Zaten emekli oldunuz")

EmekliligeKacYilKaldi(1983 , "Ali")
EmekliligeKacYilKaldi(1950 , "Ahmet")
EmekliligeKacYilKaldi(1974 , "Yagmur")

#-----------------------------------------------------------------------------------------------------------------#

print(help(EmekliligeKacYilKaldi))                  #"""" arasındaki bilgileri ekrana yazar

