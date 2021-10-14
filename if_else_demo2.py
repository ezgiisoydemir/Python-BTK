
# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz

sayi = float(input("sayi: "))
result = (sayi > 0) and (sayi <= 100 )

if result:
    print('sayı 0-100 arasında')
else:
    print('sayi 0-100 arasında değildir')


# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz

y = int(input("Bir sayı girin: "))
if (y > 0) :
    if (y%2 == 0):
        print("Sayınız çift ve pozitiftir")
    else:
        print("Sayınız pozitiftir ama çift değildir")
else:
    print("Sayınız negatiftir")

# 3- Email ve parola bilgileri ile giriş kontrolü yapınız 

email = "email@ezgisoydemir"
password = "abc123"

GirilenEmail = input("email: ")
GirilenPassword = input("password: ")
if (GirilenEmail == email) : 
    if (password == "abc123"):
        print("Uygulamaya Giriş Başarılı")
    else:
        print("Parolanız Yanliş")

else:
    print("Uygulamaya giriş başarısız")



# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız

a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))

if(a > b) and (a > c):
    print("a en büyük sayıdır")

elif (b > a) and (b > c):
    print(f"b en büyük sayıdır")

elif (c > a) and (c > b):
    print(f"c en büyük sayıdır")

# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız
#    Eğer ortalama 50 ve üstüyse geçti değilse kaldı yazınız
#    a-) Ortalama 50 olsa bile final notu en az 50 olmalıdır
#    b-) Finalden 70 aldığında ortalamanın önemi olmasın

vize1 = float(input("Vize1 notunu girin: "))
vize2 = float(input("Vize2 notunu girin: "))
final = float(input("Final notunu girin: "))

NotOrt = (((vize1 + vize2)/2) * 0.6) + (final * 0.4)


if (NotOrt >= 50):
    if(final>=50):
        print(f"öğrencinin ortalaması: {NotOrt} ve geçme durumu: başarılı")
    else:
        print(f"öğrencinin ortalaması: {NotOrt} ve geçme durumu: başarısız. Finalden en az 50 almalısınız")
else:
    print(f"öğrencinin ortalaması: {NotOrt} ve geçme durumu: başarısız")

if (NotOrt >= 50):
    print(f"öğrencinin ortalaması: {NotOrt} ve geçme durumu: başarılı")
else:
    if(final >= 70):
        print(f"öğrencinin ortalaması: {NotOrt} ve geçme durumu: başarılı. Finalden en az 70 aldığınız için geçtiniz")
    else:
        print(f"öğrencinin ortalaması: {NotOrt} ve geçme durumu: başarısız")

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

if (index >= 0) and (index <= 18.4):
    print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen zayıf")
elif (index >= 18.4) and (index <= 24.9):
    print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen normal")
elif (index >= 24.9) and (index <= 29.9):
    print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen kilolu")
elif (index >= 29.9) and (index <= 45.9):
    print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen obez")
else:
    print("Bilgileriniz yanlış")




