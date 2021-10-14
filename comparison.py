# username, pasword => database

# "ezgisoydemir" , "123456"

a , b , c , d = 5 , 5 , 10 , 4

password = "1234"
username = "ezgisoydemir"

result = ("ezgisydmr" == username) #False
result = ("ezgisoydemir" == username) #True

result = (a ==b ) # True (a b'ye eşit mi?)
result = (a == c) # False (a c'ye eşit mi?)

result ( a != b) # False (a b'ye eşit değil mi?)
result ( a != b) # True (a c'ye eşit değil mi?)

result = (a > c) # False
result = (a < c) # True

result = (a >= b) # True (a b'den büyük eşit mi?)
result = (a <= b) # True (a b'den küçük eşit mi?)
result = (c <= b) # False (a b'den küçük eşit mi?)

result = (True == 1) # True
result = (False == 0) # True
result = False + True + 40 # 41

print(result)