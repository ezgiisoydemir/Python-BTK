def greeting(name):
    print("hello", name)

print(greeting("ali"))
print(greeting)

sayHello = greeting

print(sayHello)
print(greeting)                             # İkisinin de adres bilgisi aynı yerde      

del sayHello                                # sayHello tanımını sildik adres hala yerinde duruyor

# encapsulation == kapsülleme
def outer(num1):
    def inner_increment(num1):
        print("inner")
        return num1 + 1
    num2 = inner_increment(num1)
    print(num1 , num2)

outer(10)

def factorial(number):
    if not isinstance(number ,int):
        raise TypeError("number must be an integer")

    if not number >=0:
        raise ValueError("number must be zero or positive")

    def inner_factorial(number):
        if number <= 1:
            return 1
        
        return number*inner_factorial(number - 1)
    return inner_factorial(number)
try:
    print(factorial(5))
except Exception as ex:
    print(ex)
