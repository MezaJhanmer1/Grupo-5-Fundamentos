#Usa una estructura Para para recorrer los números del 1 al 20. Por cada
#número par encontrado, incremente un contador y acumule la suma.
#Al finalizar muestra cuántos números pares hay y su suma total.

# Inicializar contador y acumulador
contador_pares = 0
suma_pares = 0

# Recorrer del 1 al 20
for numero in range(1, 21):
    if numero % 2 == 0:   # si es par
        contador_pares = contador_pares +1
        suma_pares = suma_pares + numero

# Mostrar resultados
print("Cantidad de números pares:", contador_pares)
print("Suma total de los números pares:", suma_pares)