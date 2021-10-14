## Gördüğümüz gibi birçok Python fonksiyonu normal işleyişe uymayan durumlarda bir hata durumu yayınlıyor, 
# ve programımızda bu hata durumunu yakalayarak işlem yapıyoruz. 
# Kendi yazdığımız fonksiyonların içinde raise komutu kullanarak bir hata durumu yayınlanmasını sağlayabiliriz.


x = 10

if x > 5:
  raise Exception("x 5 den büyük değer alamaz")         # raise bir hata fıraltmak

from typing_extensions import ParamSpecKwargs


def check_password(psw):
    import re
    if len(psw) < 8:
        raise Exception("Parola en az 7 karakter olmalıdır")

    elif not re.search("[a-z]" , psw):
        raise Exception("parola küçük harf içermelidir")

    elif not re.search("[A-Z]",psw):
        raise Exception("parola büyük harf içermelidir")

    elif not re.search("[0-9]",psw):
        raise Exception("parola rakam içermelidir")

    elif not re.search("[_ @$]",psw):
        raise Exception("parola alpha numeric karakter içermelidir")
    
    elif not re.search("\s",psw):
        raise Exception("parola boşluk içermelidir")

    else:
        print("Geçerli Parola")

password = "1234567"

try :
    check_password(password)
except Exception as ex:
    print(ex)
else:
    print("Geçerli Parola")
finally :
    print("Validation tamamlandı")


##### Bir başka örnek #####

class Person:
    def __init__(self , name, year):
        if len(name) > 10:
            raise Exception("Name alanı fazla karakter içeriyor")
        else:
            self.name = name

p= Person("Aliiiiiiiiii" , 1989)