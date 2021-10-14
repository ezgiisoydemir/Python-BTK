def my_decorator(func):
    def wrapper(name):
        print("fonksiyondan önceki işlemler")
        func(name)
        print("fonksiyondan sonraki işlemler")
    return wrapper

# def sayHello():
#     print("hello")

# def sayGreeting():
#     print("greeting")

# sayHello = my_decorator(sayHello)
# sayGreeting = my_decorator(sayGreeting)
# sayHello()
# sayGreeting()

@my_decorator
def sayHello(name):
    print("Hello" , name)

sayHello("Ali")

## ------------------------------------------------
import math
import time

def calculate_time(func):
    def inner(*arg,**kwargs):

        start = time.time()
        time.sleep(1)

        func(*arg,**kwargs)

        finish = time.time()
        print("fonksiyon" + func.__name__  +str(finish-start) + "saniye sürdü")
    return inner

@calculate_time
def usalma(a,b):
    print(math.pow(a,b))

@calculate_time
def faktoriyel(num):
    print(math.factorial(num))

usalma(2,3)
faktoriyel(4)