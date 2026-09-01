import math

N = int(input("Introduce el numero limite N: "))

print(f"\nNumeros primos desde 2 hasta {N}:")

for numero in range(2, N + 1):
    es_primo = True 

    limite = int(math.sqrt(numero))

    for divisor in range(2, limite + 1):
        if numero % divisor == 0:
            es_primo = False 
            break 

    if es_primo:
        print(numero, end=" ")