website = "http://www.ezgisoydemir.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz"

# 1. " Hello World " karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
message = " Hello World "
message = message.strip()
message = message.lstrip() #sadece soldan siler
message = message.rstrip() #sadece sağdan siler

message = message.lstrip(":/pth") #Soldan parantez içine yazılan kısımları siler
print(message)

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
print(isFound)

isFound = website.endswith("com")
print(isFound)

# 6. "website" içinde '.com' ifadesi var mı?
index = website.find(".com")
index = website.index(".com")
print(index)

# 7. "course" içindeki karakterlerin hepsi alfabetik mi?(isalpha, isdigit)
isFound = course.isalpha()
print(isFound)

# 8. "Contents" ifadesini satırda 50 karakter içine yerleştirip sağ soluna * ekleyin.
message ="Contents"
message = message.center(50,"*")
message = message.ljust(50,"*")
message = message.rjust(50,"*")
print(message)

# 9. "course" karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin
message = course.split()
message = "-".join(message)
print(message)

message=course.replace(" ","-")

# 10. "Hello World" karakter dizisinin 'World' ifadesini 'There' olarak değiştirin
message = "Hello World"
message = message.replace("World","There")
print(message)

# 11. "course" karakter dizisini boşluk karakterlerinden ayırın.
message = course.split()
print(message)
