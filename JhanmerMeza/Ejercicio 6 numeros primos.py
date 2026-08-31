import math
numero1 = int(input("Ingresa un numero: "))
for i in range(2,numero1 + 1):
    numeroprimo = True

    for divisor in range(2, int(math.sqrt(i))+1):
        if i % divisor == 0 :
            numeroprimo = False

    if numeroprimo:
        print(f"Los numeros primos son : {i}")