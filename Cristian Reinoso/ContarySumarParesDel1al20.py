contador = 0
suma = 0

for numero in range(1, 21):
    if numero % 2 == 0:
        contador += 1
        suma += numero

print("Cantidad de numeros pares:", contador)
print("Suma total de los numeros pares:", suma)