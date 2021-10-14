# Identity Operator: is
# Adres karşılaştırması yapılır.

x = y = [1 , 2 , 3]
z= [1 , 2 , 3]

print(x==y)     #True
print(x==z)     #True
print(x is y)   #True (x ile y aynı yerde bulunuyor)
print(x is z)   #False (x ile z farklı yerlerde bulunuyor. Bu yüzden False. Değerler önemli değil önemli olan konumu)

x = [1 , 2 , 3]
y = [2 , 4]

del x[2]
y[1] = 1
y.reverse()

print(x==y)         #True
print(x is y)       #False
print(x is not y)   #True

#Membership Operator: 

x = ["apple" , "banana"] 
print("banana" in x)        #True

name = "Sevgi"
print("e" in name)          #True
print("e" not in name)      #False



