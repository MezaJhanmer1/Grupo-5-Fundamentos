base = float(input("Ingrese la base del rectangulo: "))
altura = float(input("Ingrese la altura del rectangulo: "))

area = base * altura
perimetro = 2 * (base + altura)

print("\n--- RESULTADOS ---")
print(f"Base: {base:.2f}")
print(f"Altura: {altura:.2f}")
print(f"Area: {area:.2f}")
print(f"Perimetro: {perimetro:.2f}")