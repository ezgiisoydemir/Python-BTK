# Yöntem 1
import math 

value = dir(math)           # Dir içindeki nesnenin tüm niteliklerini döndürmeye çalışır.
                            # Math kütüphanesi içindeki fonksiyonları gösterir

value = help(math)          # Math kütüphanesindeki tüm fonksiyonları açıklar

value = help(math.factorial)    # Sadece faktöriyel i açıklar

value = math.sqrt(49)

value=math.factorial(5)

value=math.floor(5.9)

value=math.ceil(5.9)

print(value)

import math as islem

value = islem.factorial(5)

print(value)

# Yöntem 2
from math import *                              # Math kütüphanesinden hepsini import et
from math import factorial,sqrt                 # Math kütüphanesinden kullanacaklarını import et    

def sqrt(x):                                    # İlk önce def fonksiyonu çalışır. Bu yüzden matematik işlemi yapılmaz        
    print("x : " + str(x))

value = factorial(5)
value = sqrt(9)

print(value)


