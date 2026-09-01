#Pide contar y sumar pares
contar_pares = 0
sumar_pares = 0

for i in range(1,21):
    if i % 2 == 0:
        contar_pares = contar_pares + 1
        sumar_pares = sumar_pares + i

print(f"Cantidad de Núm. pares encontrados: {contar_pares}")
print(f"La suma total de los Núm. pares es: {sumar_pares}")
