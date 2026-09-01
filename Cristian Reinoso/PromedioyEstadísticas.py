n = int(input("Ingrese la cantidad de estudiantes: "))

suma = 0
nota_alta = 0
nota_baja = 20
aprobados = 0

for i in range(1, n + 1):
    nota = float(input(f"Ingrese la nota del estudiante {i}: "))

    suma += nota

    if nota > nota_alta:
        nota_alta = nota

    if nota < nota_baja:
        nota_baja = nota

    if nota >= 11:
        aprobados += 1

promedio = suma / n

print("\n--- RESULTADOS ---")
print(f"Promedio: {promedio:.2f}")
print(f"Nota mas alta: {nota_alta:.2f}")
print(f"Nota mas baja: {nota_baja:.2f}")
print(f"Estudiantes aprobados: {aprobados}")