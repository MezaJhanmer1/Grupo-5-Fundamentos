num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
operador = input("Ingrese el operador (+, -, *, /): ")

match operador:
    case "+":
        resultado = num1 + num2
        print(f"Resultado: {resultado}")
    case "-":
        resultado = num1 - num2
        print(f"Resultado: {resultado}")
    case "*":
        resultado = num1 * num2
        print(f"Resultado: {resultado}")
    case "/":
        if num2 != 0:
            resultado = num1 / num2
            print(f"Resultado: {resultado}")
        else:
            print("Error: no se puede dividir entre cero.")
    case _:
        print("Operador no válido.")