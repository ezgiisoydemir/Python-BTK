website = "http://www.ezgisoydemir.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz"

# 1. " Hello World " karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
message = " Hello World "
message = message.strip()
message = message.lstrip() #sadece soldan siler
message = message.rstrip() #sadece sağdan siler

message = message.lstrip(":/pth") #Soldan parantez içine yazılan kısımları siler
print(message)                    #Sonuc www.ezgisoydemir.com

# 2. "www.ezgisoydemir.com" içindeki ezgisoydemir bilgisi haricindeki her karakteri silin
message = "www.ezgisoydemir.com".strip("w.moc")

# 3. "course" karakter dizisinin tüm karakterlerini küçük harf yapın
message = course.lower()
print(message)

# 4. "website" içinde kaç tane a karakteri vardır? (count'a')
message = website.count("a")

message = website.count("www",0,10) #0 ile 10 arasında www var mı
print(message)

# 5. "website" www ile başlayıp com ile bitiyor mu?
isFound = website.startswith("www")
print(isFound) #false

isFound = website.endswith("com")
print(isFound) #True

# 6. "website" içinde '.com' ifadesi var mı?
index = website.find(".com") #22
index = website.find(".com", 0 , 10) #-1

index = course.find("Python") #1
index = course.rfind("Python") #26 Sagdan sola sayar
print(index)

# 7. "course" içindeki karakterlerin hepsi alfabetik mi?(isalpha, isdigit)
isFound = course.isalpha() #False - alpha = Alfabedik
isFound = course.isdigit() #False Gelen degerler bir rakam mi diye baktik - digit = Digital?
print(isFound)

# 8. "Contents" ifadesini satırda 50 karakter içine yerleştirip sağ soluna * ekleyin.
message ="Contents"
message = message.center(50,"*")
message = message.ljust(50,"*") #Yildzlar sadece solda olur
message = message.rjust(50,"*") # yildizlar sadece sagda olur
print(message)

# 9. "course" karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin
message = course.split()
message = "-".join(message)
print(message)

message=course.replace(" ","-")
message=course.replace(" ","-",5) #Sadece 5 karakteri degistirir. Yani son cizgi python ve programlama arasinda olur
message=course.replace(" ","") # Butun bosluk karakterlerini siler

# 10. "Hello World" karakter dizisinin 'World' ifadesini 'There' olarak değiştirin
message = "Hello World"
message = message.replace("World","There")
print(message)

# 11. "course" karakter dizisini boşluk karakterlerinden ayırın.
message = course.split(' ')
print(message)
