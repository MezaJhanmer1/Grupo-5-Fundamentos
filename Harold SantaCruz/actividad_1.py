#Escribe un programa que solicite la base y
#altura de un rectángulo y calcule su área (A =
#base × altura) y su perímetro (P =
#2×(base+altura)). Muestra los resultados
#formateados.
print("AREA y PERIMETRO DEL RECTANGULO")
#Solicitamos los datos necesarios
base =float(input("COLOCAR LA BASE : "))
altura=float(input("COLOCAR LA ALTURA : "))
#Colocamos el valor de la operacion a a la variable area
area = base * altura
perimetro = 2*(base + altura)
print(f" el area del rectangulo es  : {area}")
print("----------------------------------------")
print(f" el perimetro del rectangulo es  : {perimetro}")