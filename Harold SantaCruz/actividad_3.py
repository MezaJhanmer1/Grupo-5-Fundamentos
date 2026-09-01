#Solicita un número y muestra su tabla de
#multiplicar del 1 al 10 usando una estructura
#repetitiva Para.
#colocamos el  valor de la variabled
n = int(input("Número: "))
#Usamos for para obtner el valor de su tabla colocando el limite requerido
print(f"--- Tabla del {n} --- ")
for i in range(1, 11):
 print(f"{n} x {i} ={n*i}")