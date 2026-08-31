import random

aleatorio =  random.randint(1,100)

intentos = 0

print("Vamos a comenzar el juego de adivinar un numero secreto")
print("He pensado un numero desde el 1 al 100")
print("Intenta adivirnar el numero secreto")


while True:
    numero = int(input("ingresa tu numero: "))
    intentos += 1

    if numero < aleatorio :
        print("El numero secreto es mayor sigue intentando: ")

    elif numero > aleatorio:
        print("El numero secreto es menor sigue intentando: ")

    else:
        print("Acertaste el numero secreto: ")
        print(f"Numero de intentos: {intentos}")
        break
    