#Pide suma resta mult y division de 2 numeros

a = float(input("Número 1: "))
b = float(input("Número 2: "))
operacion = input("Ingresa un operacion (+, -, *, /): ")

if operacion == "+":
    resultado = a + b
    print(f"Resultado de Suma: {a} + {b} = {resultado}")
elif operacion == "-":
    resultado = a - b
    print(f"Resultado de Resta: {a} - {b} = {resultado}")
elif operacion == "*":
    resultado = a * b
    print(f"Resultado de Mult: {a} * {b} = {resultado}")
elif operacion == "/":
    if b == 0:
        print("Error: No se puede dividir entre cero.")
    else:
        resultado = a / b
        print(f"Resultado: {a} / {b} = {resultado}")
else:
    print("Operador no válido. Por favor, usa +, -, * o /.")

        
