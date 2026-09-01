#Pide el numero random del 01 al 100, poner si es mayor o menor, contar intentos.
import random

num_random =  random.randint(1,100)
num_intento = 0

print("Adivinar un numero secreto")
print("He pensado un número entre 1 y 100. ¿Puedes adivinarlo?")



while True:
    num = int(input("ingresa tu numero: "))
    num_intento = num_intento + 1

    if num < num_random :
        print("El numero secreto es mayor sigue intentando !! ")
        print(f"Numero de intentos: {num_intento}")
    elif num > num_random:
        print("El numero secreto es menor sigue intentando !!  ")
        print(f"Numero de intentos: {num_intento}")

    else:
        print("Acertaste el numero secreto !!! ")
        print(f"Numero de intentos: {num_intento}")
        break