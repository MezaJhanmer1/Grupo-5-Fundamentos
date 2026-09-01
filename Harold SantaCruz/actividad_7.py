#Genera un número aleatorio entre 1 y 100. El usuario
#debe adivinarlo. En cada intento, indica si el número
#secreto es mayor o menor. Cuenta los intentos.


#imporar random para generar el numero aleatorio
import random

numero_secreto = random.randint(1, 100)
intentos = 0

print("Adivina el número secreto entre 1 y 100.")
#colocar un bucle while para que el usuario pueda seguir intentando hasta adivinar el numero
while intentos < 100:
    intento = int(input("Ingresa tu número: "))
    intentos += 1
#colocar las condiciones para saber si el numero es mayor o menor
    if intento < numero_secreto:
        print("El número secreto es mayor.")
    elif intento > numero_secreto:
        print("El número secreto es menor.")
    else:
        print(f"¡Correcto! Has adivinado el número en {intentos} intentos.")
        break