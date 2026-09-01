#Solicita un número y muestra su tabla de multiplicar del 1 al 10 usando una estructura repetitiva Para.

n = int(input("Número para Multiplicar: "))
print(f"---Tabla del {n} ---")
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")