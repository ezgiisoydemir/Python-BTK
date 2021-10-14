# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır
# Kullanımı: open(dosya_adı , dosya_erişme_modu) 
# dosya_erişme_modu => dosyayı hangi amaçla açtığımızı belirtir
# encoding="utf-8" => Türkçe karakterler text içinde sorun çıkarmaz. ş gibi harfleri dosya içine yazabilirsin

# "w" : (Write) yazma modu. Dosyayı konumda oluşturur
#   ** Dosyayı konumda oluşturur
#   ** Dosya içeriğini siler ve yeniden ekleme yapar

file = open("newfile.txt","w")
file.close()
print(file)

""" İkinci Yol """
file = open("C:/Users/ezgis/desktop/nexfile.txt" , "w")
print(file)

""" Örnek Vermek İstersek """
file = open("newfile.txt", "w" ,encoding="utf-8")
file.write("Ezgi Soydemir")
file.close()

# "a" : (Append) ekleme. Dosya konumda yoksa oluşturur
#   ** Her çalıştığında dosya konumuna eklemeler yapar

file = open("newfile.txt", "a" ,encoding="utf-8")
file.write("\nEzgi Soydemir")
file.close()

# "x" : (Create) oluşturma. Dosya zaten varsa hata verir

file = open("newfile2.txt", "x" ,encoding="utf-8")

# "r" : (Read) okuma. Varsayılan. Dosya yoksa hata verir


