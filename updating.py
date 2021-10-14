with open("newfile.txt", "r+" ,encoding="utf-8") as file:
    file.seek(20)
    file.write("deneme")

with open("newfile.txt", "r+" ,encoding="utf-8") as file:
    print(file.read())

#   **** Sayfa sonunda güncelleme *****

with open("newfile.txt" , "a" , encoding="utf-8") as file:
    file.write("\n Ayfer Soydemir")

#   **** Sayfa başında güncelleme *****

with open("newfile.txt" , "r" , encoding="utf-8") as file:
    print(file.read())

""" Örnek """
with open("newfile.txt", "r+" ,encoding="utf-8") as file:
    content = file.read()
    content = " Atalay Soydemir\n " + content 
    file.seek(0)
    file.write(content)

with open("newfile.txt", "r" ,encoding="utf-8") as file:
    print(file.read())

#   **** Sayfa ortasında güncelleme *****

with open("newfile.txt", "r+" ,encoding="utf-8") as file:
    list = file.readline()
    list.insert(1 , " Atalay Soydemir\n ")
    file.seek(0)
    file.writelines(list)

with open("newfile.txt", "r" ,encoding="utf-8") as file:
    print(file.read())
