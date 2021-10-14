"""
    Daire Alanı : πr^2
    Daire Çevresi : 2πr

    *Yarıçapı verilen bir dairenin alan ve çevresini hesaplayınız. (r: 3.14)
"""

pi = 3.14

r = float(input ("yarıçap: "))

alan = pi*(r**2)
cevre = 2 * pi * r

print("alan:",alan)
print("Çevre:",cevre)

"""
print("alan: " + alan + " cevre: " + cevre) 
yazamayız çünkü içerisi int değerinde bizim değerimiz ise float.
"""
print("alan: " + str(alan) + " cevre: " + str(cevre)) 
#str olarak tanımlamamız gerekir.