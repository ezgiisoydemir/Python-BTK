message = "Hello There. My name is Ezgi Soydemir".split()
print(message)

my_list = [1,2,3]
my_list = ["bir",2,True,5.6]
print(my_list)

list1 = ["one" , "two" , "three"]
list2 = ["four" , "five" , "six"]

numbers = list1 + list2 #listeleri birleştirme - ['one', 'two', 'three', 'four', 'five', 'six']
print(numbers)
print(len(numbers))

userA = ["Ezgi",22]
userB = ["Sevgi",14]

users = [userA, userB] #liste içinde liste - [['Ezgi', 22], ['Sevgi', 14]]
print(users)
print(users[1]) #['Sevgi', 14]

a= users[1]
print(a[0]) #Sevgi

print(users[1][0]) #Sevgi