
# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz

x = int(input("Bir sayı girin: "))
result = (x > 0 and x < 100)
print(result)

# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz

y = int(input("Bir sayı girin: "))
result = (y > 0) and (y%2 == 0)
print(result)

# 3- Email ve parola bilgileri ile giriş kontrolü yapınız 

email = "email@ezgisoydemir"
password = "abc123"

GirilenEmail = input("email: ")
GirilenPassword = input("password: ")

result = (GirilenEmail == email) and (GirilenPassword == password)
print(f"Uygulamaya Giriş Başarılı Mı? : {result}")

# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız

a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))

result = (a > b) and (a > c)
print(f"a en büyük sayıdır : {result}")

result = (b > a) and (b > c)
print(f"b en büyük sayıdır : {result}")

result = (c > a) and (c > b)
print(f"c en büyük sayıdır : {result}")

# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız
#    Eğer ortalama 50 ve üstüyse geçti değilse kaldı yazınız
#    a-) Ortalama 50 olsa bile final notu en az 50 olmalıdır
#    b-) Finalden 70 aldığında ortalamanın önemi olmasın

vize1 = float(input("Vize1 notunu girin: "))
vize2 = float(input("Vize2 notunu girin: "))
final = float(input("Final notunu girin: "))

NotOrt = (((vize1 + vize2)/2) * 0.6) + (final * 0.4)
result = (NotOrt >= 50) and (final >=50)

print(f'not ortalamanız : {NotOrt} ve dersten geçme durumunuz : {result} ')

# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız
#    Formül : (Kilo / boy uzunluğunun karesi)
#    Aşağıdaki tabloya göre kişi hangi gruba girmektedir
#    0 - 18.4    => Zayıf  
#    18.5 - 24.9 => Normal
#    25.0 - 29.9 => Fazla Kilolu
#    30.0 - 34.9 => Şişman ( Obez)

name = input("Adınız: ")
kg = float(input("Kilonuz: "))
hg= float(input("Boyunuz: "))

index = (kg) / (hg ** 2)
zayif = (index >= 0) and (index <= 18.4)
normal = (index >= 18.4) and (index <= 24.9)
kilolu = (index >= 24.9) and (index <= 29.9)
obez = (index >= 29.9) and (index <= 34.9)

print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen zayıf: {zayif}")
print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen normal: {normal}")
print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen kilolu: {kilolu}")
print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen obez: {obez}")