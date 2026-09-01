
# Pide base x altura de un rectangulo
altura = float(input("Ingresa la altura del rectángulo: "))
base = float(input("Ingresa la base del rectángulo: "))

# Formulas: área (A = base × altura) y su perímetro (P = 2×(base+altura)).
area= base * altura
perimetro= 2 * (base+altura)

#Print Resultados
print("Resultados del Ejercicio: ")
print(f"Área del Rectangulo: {area}")
print(f"Perímetro del Rectangulo: {perimetro}")