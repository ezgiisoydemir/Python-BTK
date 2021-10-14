
# 1- Girilen iki sayıdan hangisi daha büyüktür?

a = int(input("Birinci sayıyı girin: "))
b = int(input("İkinci sayıyı girin: "))

result = (a > b)
print(f'a:{a} b:{b} den büyüktür: {result} ')

# 2-Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız
#   Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırınız.

vize1 = float(input("Vize1 notunu girin: "))
vize2 = float(input("Vize2 notunu girin: "))
final = float(input("Final notunu girin: "))

NotOrt = (((vize1 + vize2)/2) * 0.6) + (final * 0.4)

print(f'not ortalamanız : {NotOrt} ve dersten geçme durumunuz : {NotOrt>=50} ')

# 3- Girilen bir sayının tek mi çift mi olduğunu yazdırınız

sayi = int(input("Sayı giriniz: "))
tekcift = (sayi % 2 == 0 )
print(f'Girilen sayının çift olma durumu: {tekcift} ')


# 4- Girilen bir sayının negatif pozitif durumunu yazdrınız

sayi = int(input("Sayı Giriniz: "))
pozitifse = (sayi > 0)

print(f'Girilen sayının pozitif olma durumu: {pozitifse} ')


# 5- Parola ve email blgisini isteyip doğruluğunu kontrol ediniz
#    (email : email@ezgisoydemir.com / parola : abc123)

email = "email@ezgisoydemir.com"
password = "abc123"

GirilenMAil = input("email: ")
GirilenPassword = input("parola: ")

isEmail = (email == GirilenMAil.lower())    # .lower girilen değerde büyük küçük harf önemsenmiyorsa kullanılır
isPassword = (password == GirilenPassword.lower())

print(f'Email bilgisi doğru mu: {isEmail} ve parola doğru mu: {isPassword}')

