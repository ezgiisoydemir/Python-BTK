x, y, z =5 ,10, 20

x,y = y,x #x ve ynin değerlerini değiştirmek istersem

x += 5          # x = x + 5
x -= 5          # x = x - 5
x *= 5          # x = x * 5
x /= 5          # x = x / 5
x %= 5          # x = x + 5 mod
x //= 5         # x = x - 5 tam bölme (kalansız bölme)
x **= 5         # x = x + 5 üs alma
x **= 5         # x = x ** y

print(x,y,z)

# Atama operatörlerinin etkisi üzerine konuşursak;

values = 1 , 2 , 3

print(values)
print(type(values))

x, y, z = values        # Values taki değerler direk x y z ye geçti

print(x,y,z)            # Sonuc 1 2 3 çıkar

values = 1 , 2 , 3 , 4 , 5
x, y, *z = values       # Sonuç 1 2 [3,4,5]
                        #z liste oluşturur
