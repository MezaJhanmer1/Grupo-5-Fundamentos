par = 0
total = 0


for numero in range(1,21):
    if numero % 2 == 0:
        par = par + 1
        total = total + numero

print(f"Cantidad de numeros pares: {par}")
print(f"Suma total de los numeros pares: {total}")



