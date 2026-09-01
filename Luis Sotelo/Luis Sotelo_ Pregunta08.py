n = int(input("¿Cuántas notas deseas ingresar?: "))
lista_notas = []
aprobados = 0

for i in range(1, n + 1):
    nota = float(input(f"Ingresa la nota del estudiante {i}: "))
    lista_notas.append(nota)

nota_mas_alta = max(lista_notas)
nota_mas_baja = min(lista_notas)
promedio = sum(lista_notas) / n

for nota in lista_notas:
    if nota >= 11:
        aprobados = aprobados + 1

    print("")
    print("       INFO Y PUNTAJES         ")
    print("")
    print(f" Total de notas Ingresadas : {n}")
    print(f" Promedio Total         : {promedio}")
    print(f" Nota más alta            : {nota_mas_alta}")
    print(f" Nota más baja            : {nota_mas_baja}")
    print(f" Estudiantes Aprobados    : {aprobados}")
    print(f" Estudiantes Desaprobados : {n - aprobados}")
