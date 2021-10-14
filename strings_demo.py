website = "http://www.ezgisoydemir.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"

# 1- "course" karakter dizisinde kaç karakter bulunmaktadır?
lenght=len(course)
print(lenght)
lenghtWebsite = len(website)

# 2- "website" içinden www karakterlerini alın
result = website[7:10]

# 3- "website" içinden com karakterlerini alın
result = website[22:25]
result = website[lenghtWebsite-3:lenghtWebsite]

# 4- "course" içinden ilk 15 ve son 15 karakterlerini alın
result = course[0:15]
result = course[:15]
result = course[-15:]

# 5- "course" ifadesindeki karakterleri tersten yazdırın
result = course [::] #course ifadesindeki bütün elemanları almaka için 
result = course [::2] #course ifadesinde 2 atlayarak ilerler
result = course [::-1] #course tersten yazarız

s = "12345" * 5
print(s[::5]) #sonuçta her seferinde 5 adım atlayarak yazdığı için ekranda 11111 okunur

name, surname, age, job = "Ezgi","Soydemir",22,"mühendis"

# 6- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeleri yazdırın.
#    "Benim adım Ezgi Soydemir, Yasım 22 ve mesleğim mühendis"
result = "Benim adım " + name + " " + surname + ", yasım " + str(age) + " ve mesleğim " + job
result = "Benim adım {} {}, yaşım {} ve mesleğim {}.".format(name,surname,age,job)
result = "Benim adım {name} {surname}, Yasım {age} ve mesleğim {job}."

# 7- "Hello World" ifadesindeki w harfini "W" ile değiştirin
s = "Hello World"
s = s[0:6] + "W" + s[-4:]
s.replace("w","W")

# 8- "abc" ifadesini yan yana 3 defa yazın
result = "abc" * 3