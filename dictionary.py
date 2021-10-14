 #key - value

# 41 = kocaeli  34 = istanbul

sehirler = ["kocaeli","istanbul"]
plakalar = [41,34]

print(plakalar[sehirler.index("kocaeli")])
print(plakalar[sehirler.index("istanbul")])

# print(plakalar["kocaeli"]) = 41
# print(plakalar["istanbul"]) = 34

#plakalar {"key" : "value"}

plakalar =  {"kocaeli" : 41 , "istanbul" : 34}

print(plakalar["kocaeli"])
print(plakalar["istanbul"])

plakalar["ankara"] = 6 #bu şekilde listeye yeni bir key eklenir - {'kocaeli': 41, 'istanbul': 34, 'ankara': 6}
print(plakalar)

users = {
    "ezgisoydemir" : {
        "age" : 22,
        "roles" :["user"],
        "email" : "ezgi@gmail.com",
        "adress" : "istanbul",
        "phone" : 123456

    },
    "sevgisoydemir" :  {
        "age" : 14,
        "roles" :["user","admin"],
        "email" : "sevgi@gmail.com",
        "adress" : "erzincan",
        "phone" : 147258

    }
}

print(users["sevgisoydemir"])
print(users["sevgisoydemir"]["age"])
print(users["sevgisoydemir"]["roles"][0])