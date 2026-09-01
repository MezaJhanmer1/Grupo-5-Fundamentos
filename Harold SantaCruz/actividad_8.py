#Solicita N notas al usuario. Calcula el promedio, la
#nota más alta, la más baja y cuántos estudiantes
#aprobaron (nota >= 11). Muestra estadísticas
#completas.
n=int(input("Colocar el número de notas : "))
while n<=0:
    print("El número de notas debe ser mayor que cero.")
    n=int(input("Colocar el número de notas : "))
suma_notas=0
contador_aprobados=0
nota_mas_=0
#colocamos un bucle para obtener las notas y realizar los calculos requeridos
#nota_mas_baja=20 por que es la nota mas alta que se puede obtener
nota_mas_baja=20
#aca se coloca el bucle for para obtener las notas y realizar los calculos requeridos
for i  in range(1,n+1):
    #realizamos la condicion para que la nota sea mayor a 0 y menor a 20
    nota=float(input(f"Colocar la nota {i} : "))
    #colocamos un if para que la nota sea mayor a 0 y menor a 20
    if nota>nota_mas_:
        nota_mas_=nota
    if nota<nota_mas_baja:
        nota_mas_baja=nota
    suma_notas+=nota
    if nota>=11:
        contador_aprobados+=1
promedio=suma_notas/n
print(f"Promedio: {promedio}")
print(f"Nota más alta: {nota_mas_}")
print(f"Nota más baja: {nota_mas_baja}")
print(f"Estudiantes aprobados: {contador_aprobados}")

