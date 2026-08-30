import random

secreto = random.randint(1, 100)
intento = 0
intentos = 0

while intento != secreto:
    intento = int(input("Número: "))
    intentos += 1
    if intento < secreto:
        print("Es MAYOR")
    elif intento > secreto:
        print("Es MENOR")

print("¡Adivinaste en", intentos, "intentos!")