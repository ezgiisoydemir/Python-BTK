# FOR İLE BREAK E CONTİNUE ANLATIMI
name = "Ezgi Soydemir"

for letter in name:
    print(letter)

for letter in name:
    if letter == "z":       # z harfini görünce döngü durur. Sadece E yazar ekranda
        break
    print(letter)

for letter in name:
    if letter == "z":       # z harfini görünce döngü durmaz. Sadece z ekrana yazılmaz. Diğer tüm harfler yazılır
        continue
    print(letter)

# WHİLE İLE BREAK E CONTİNUE ANLATIMI
x = 0

while x < 5:
    print(x)
    x += 1

while x < 5:
    if x == 2:          # Eğer x 2'ye eşit ise döngüden çıkar. Sadece 0 ve 1  ekrana yazılır
        break
    print(x)
    x += 1

while x < 5:
    x += 1
    if x == 2:          # Eğer x 2'ye eşit ise 2 hariç diğerlerini ekrana yazar. Çünkü 2 den sonra devam et denilir
        continue
    print(x)
  
# 1'DEN 100'E KADAR TEK SAYILARIN TOPLAMI

x = 1
result = 0
while x <= 100:
    result += x
    x +=1
print( f"toplam: {result}")
    
x=0
result = 0    
while x <= 100:
    x += 1
    if x%2 == 0:
        continue
    result += x
print(f"toplam: {result}")
    
