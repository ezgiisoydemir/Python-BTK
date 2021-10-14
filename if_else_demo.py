# 1 - Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz.
#     Ehliyet alma koşulu en az 18 ve eğitim durumu lise ya da üniversite olmalıdır.

name = input("Lütfen isminizi giriniz: ")
yas = int(input("Lütfen yaşınızı giriniz: "))
egitim = input("Lütfen eğitim durumunuzu giriniz: ")

if (yas >= 18) and ((egitim == "universite") or (egitim == "lise")):
    print("Ehliyet alabilir")
# else :
    print("Ehliyet alamaz")


# 2 - Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre not aralığına karşılık  
#     gelen not bilgisini yazdırınız.
#     0  - 24  => 0
#     25 - 44  => 1
#     45 - 54  => 2
#     55 - 69  => 3
#     70 - 84  => 4
#     85 - 100 => 5

yazılı1 = int(input("Birinci yazılı notunu giriniz: "))
yazılı2 = int(input("İkinci yazılı notunu giriniz: "))
sozlu = int(input("Sözlü notunuzu giriniz: "))

ortalama = (yazılı1 + yazılı2 + sozlu) / 3

if (ortalama > 0) and (ortalama < 24):
    print("Notunuz 0")                            #print(f"ortalamanız: {ortalama} notunuz: 0")
elif (ortalama > 25) and (ortalama < 44):
    print("Notunuz 1")
elif (ortalama > 45) and (ortalama < 54):
    print("Notunuz 2")
elif (ortalama > 55) and (ortalama < 69):
    print("Notunuz 3")
elif (ortalama > 70) and (ortalama < 84):
    print("Notunuz 4")
else:
    print("Notunuz 5")


# 3 - Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayınız
#     1. Bakım => 1. yıl
#     2. Bakım => 2. yıl
#     3. Bakım => 3. yıl
#     4. Bakım => 4. yıl
#     5. Bakım => 5. yıl
#     ** Süre hesabına alınan gün, ay, yıl bilgisine göre bazlı hesaplayınız
#     *** datetime modülünü kullanmanız gerekiyor
#     (simdi) - (2018/8/1) => gün

# BİRİNCİ YOL 
days = int(input("aracınız kaç gündür trafikte: "))

if days <= 365:
    print("1.servis aralığı")
elif days > 365 and days <= 365*2:
    print("2.servis aralığı")
elif days > 365*2 and days <= 365*3:
    print("3.servis aralığı")
else:
    print("Hatalı süre")

# II.YOL DATETİME İLE
import datetime
tarih = input("Aracınız hangi tarihte trafiğe çıktı (2019/8/9) : ")     #Tarihi 2019/8/9 şeklinde yazdık
tarih=tarih.split("/")                                                  #Burada da /'tan sonrasını ayırmasını istedik

print(tarih[0])                                                         #Liste halinde sayıları gördük
print(tarih[1])
print(tarih[2])

trafigeCıkıs = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi = datetime.datetime.now()         #datetime kullanım şekli bu
fark= simdi - trafigeCıkıs
days = fark.days               # .days ile days bilgisini aldık. Normalde 1309 days yazıyordu. Şiödi sadece 1309 yazıyor

if days <= 365:
    print("1.servis aralığı")
elif days > 365 and days <= 365*2:
    print("2.servis aralığı")
elif days > 365*2 and days <= 365*3:
    print("3.servis aralığı")
else:
    print("Hatalı süre")





