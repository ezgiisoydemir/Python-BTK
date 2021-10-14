# file = open("newfile.txt", "r" ,encoding="utf-8")
# content = file.read()
# print(content)
# file.close()

# with komutu kullanımı
#   *** Dosya otomatik olarak kapanır

with open("newfile.txt", "r" ,encoding="utf-8") as file:
    content=file.read()
    print(content)
    file.seek(10)                       # Klasörü onuncu yere götürür                        
    print(file.tell())                  # tell fonksiyonu o andaki klasörün konumunu verir
    content2 = file.read()
    print(content2)
