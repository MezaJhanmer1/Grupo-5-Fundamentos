cantidadnotas = int(input("Ingrese la cantidad de notas que desea promediar: "))
notas = []
aprobados = 0
for i in range(cantidadnotas):
    calificacion = float(input(f"Ingresa la {i+1} nota del estudiante: "))

    notas.append(calificacion)

    if calificacion >= 11:
        aprobados += 1

promedio = sum(notas) / cantidadnotas

nota_mas_alta = max(notas)

nota_mas_baja = min(notas)

print("Estadisticas de tus notas")
print(f"Cantidad de notas colocadas:{cantidadnotas} ")
print(f"Promedio:{promedio} ")
print(f"Nota mas baja: {nota_mas_baja}")
print(f"Nota mas alta: {nota_mas_alta}")
print(f"Cantidad de cursos aprobados:{aprobados}")
print(f"Cantidad de cursos desaprobados: {cantidadnotas - aprobados}")
