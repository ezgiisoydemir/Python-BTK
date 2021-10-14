x , y , z = 2 , 5 , 10 

numbers = 1 , 5 , 7 , 10, 6

# 1- Kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir?
a = int(input("Bir sayı giriniz : "))
b = int(input("Bir sayı giriniz : "))

result = (a*b) - (x+y+z)
print(result)

# 2- y'nin x'e kalansız bölümünü hesaplayınız

result = y//x

# 3- (x,y,z) toplamının mod 3'ü nedir?

result = (x+y+z) % 3

# 4- y'nin x. kuvetini hesaplayınız 

result = y ** x

# 5- x, *y, z = numbers işelmine göre z'nin küpü kaçtır?

numbers = 1 , 5 , 7 , 10 , 6
x , *y , z = numbers # x=1 y=5,7,10 z=6
result =z ** 3
 
# 6- x, *y, z = numbers işlemine göre y'nin değerleri toplamı kaçtır? 

numbers = 1 , 5 , 7 , 10 , 6
x , *y , z = numbers

result = y[0] + y[1] + y[2]

print(result)