x = 5
result = 5 < x < 10
print(result) #False

x = 6
result = 5 < x < 10
print(result) #True

hak = 5 
devam = "e"

#and

# True , True => True
# True , False=> True
# False , False => False

result = (x > 5 and x < 10)  # x 5'ten küçük 10'dan büyük mü?
result = (hak > 0) and (devam == "e")

#or

# True , False => True
# True , True => True
# False , False => False

result = (x > 0) or (x % 2 == 0)

#not

result = not(x > 0)

# x , 5 ile 10 arasında olan bir çift sayı mı?

result = ((x > 5 and x < 10)) and (x % 2 == 0)

print(result)
