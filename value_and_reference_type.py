#value type
x = 5
y = 25

x = y

y = 10

print(x,y) #25 10 
#Burada y yi x e eşdeğer yaptıktan sonra y deki herhangi bir değişiklik x i etkilemedi. Fakat 

#reference type => list
a = ["apple","banana"]
b = ["apple","banana"]

a=b

b[0] = "grape"

print(a,b) #['grape', 'banana'] ['grape', 'banana']
#List halinde değerlerde değişiklik yapıldığında b deki değişiklik a yı etkiledi

