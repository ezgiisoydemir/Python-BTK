message = "Hello there. My name is Ezgi Soydemir"

message = message.upper() #HELLO THERE. MY NAME IS EZGI SOYDEMIR

message = message.lower() #hello there. my name is ezgi soydemir

message = message.title() #Her kelimenin baş harfi büyük harfe çevrilir - Hello There. My Name Is Ezgi Soydemir

message = message.capitalize() #Verilen cümlenin sadece ilk harfi büyük olur - Hello there. my name is ezgi soydemir

message = message.strip() #Verilen cümlenin başında boşluk varsa başında boşluk yokmuş gibi yazar

message = message.split() # Boşluklardan itibaren dizilere ayırma - ['Hello', 'there.', 'My', 'name', 'is', 'Ezgi', 'Soydemir']

message = message.split(".") # Noktadan itibaren dizilere ayırma - ['Hello there', ' My name is Ezgi Soydemir']

message = message.split()
message = " ".join(message) # Ayrilan kelimeleri aralara boşluk koyarak birleştirir

index = message.find("Ezgi")
print(index) # Cümlenin içinden ezgi kelimesini arattık. Bunu da hangi sayıda başladığını öğrendik

index = message.find("Ezgii")
print(index) #Ezgii diye bir kelime yok. Bu yüzden cevap olarak -1 görürüz.

isFound = message.startswith("H")
print(isFound) # Cümlenin H ile başlayıp başlamadığını sorduk. True cevabını aldık.

isFound = message.endswith("n")
print(isFound) #Cümlenin sonu n ile bitip bitmediğini sorduk. 

message = message.replace("Ezgi","Sevgi") # Ezgi ile Sevgi yer değiştirdi - Hello there. My name is Sevgi Soydemir
#art arda.replace yaparak seri şekilde değişim uygulayabiliriz

message = message.center(50,"*") # 50 dizi içinde ortalayarak yazıyı yazar - ******Hello there. My name is Ezgi Soydemir*******


print(message)
