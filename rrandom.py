
import random

# result = dir(random)
# result = help(random)

result = random.random()                # 0.0 - 1.0 arasında rastgele sayı üretir 
result = random.random()*100            # 0.0 - 100.0
result = random.uniform(10,100)         # 10.0 - 100.0 arası yazıldı
result = int(random.uniform(10,100))    # Ondalıklı sayıları tam sayı haline getirir
result = random.randint(1,100)          # 1 - 100 arası tam sayı üret

names = ["ali" , "yagmur" , "deniz" , "cenk"]
result = names[random.randint(0,len(names)-1)]
result = random.choice(names)

greeting = "Hello There"
result = random.choice(greeting)

liste = list(range(10))
random.shuffle(liste)
result = liste

liste = range(100)
result = random.sample(liste,3)         # 0 - 100 arası 3 rastgele sayı
result = random.sample(names,3)         # Listedeki isimleri rastgele bir şekilde yazar

print(result)