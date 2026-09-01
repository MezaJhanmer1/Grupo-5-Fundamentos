num1 = int(input("Ingrese el primer numero entero: "))
num2 = int(input("Ingrese el segundo numero entero: "))

if num1 > num2:
    print(f"El numero mayor es: {num1}")
elif num2 > num1:
    print(f"El numero mayor es: {num2}")
else:
    print("Ambos numeros son iguales.")