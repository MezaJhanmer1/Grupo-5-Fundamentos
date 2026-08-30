n = int(input("Cantidad de notas: "))
notas = [float(input("Nota: ")) for _ in range(n)]

print("Promedio:", sum(notas) / n)
print("Mayor:", max(notas))
print("Menor:", min(notas))
print("Aprobados:", sum(1 for n in notas if n >= 11))