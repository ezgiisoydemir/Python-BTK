
if 3>2:
    print("Hoş Geldiniz")       # Hoş Geldin yazar eşitlik doğru

if 3>3:
    print("Hoş Geldiniz")       # Hoş Geldin yazmaz eşitilk yanlış

if 3==3:
    print("Hoş Geldiniz")       # Hoş Geldin yazar eşitlik doğru

isLoggedin = True
if isLoggedin:
    print("Hoş Geldin")             # Hoş Geldin yazar

isLoggedin = False
if isLoggedin:
    print("Hoş Geldin")             # Hoş Geldin yazmaz

username = "ezgisoydemir"
password = "1234"

isLoggedin = (username == "ezgisoydemir") and (password == "1234")
if isLoggedin:
    print("Hoş Geldin")             # Hoş Geldin yazar



if (username == "ezgisoydemir") and (password == "1234"):
    print("Hoş Geldin ")

else:
    print("username ya da parola yanlış")



if (username == "ezgiisoydemir"):        #username ve parola doğru olmalı. ikisi arasındaki farka dikkat et
    if(password=="1234"):
        print("Hoş Geldin ")
    else:
        print("Parola Yanlış")

else:
    print("username yanlış")
