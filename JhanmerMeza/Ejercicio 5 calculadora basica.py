numero1 = float(input("Ingresa el primer numero: "))
numero2 = float(input("Ingresa el segundo numero: "))
print("El 1 es suma, el numero 2 es resta, el numero 3 es multiplicar y numero 4 es divir")
operacion = int(input("Ingresa el operador: "))




if operacion == 1 :
    print(f"La suma es {numero1 + numero2}")
elif operacion == 2 :
    print(f"La resta es {numero1 - numero2}")
elif operacion == 3 :
    print(f"La multiplicacion es {numero1 * numero2}")
elif operacion == 4 :
    if numero2 != 0 :
        print(f"La division es {numero1 / numero2}")
    else:
        print("No se puede dividir entre 0")


else:
    print("Valor incorrecto operacion no realizada")