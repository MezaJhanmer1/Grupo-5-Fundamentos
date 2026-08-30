num1 = float(input("Número 1: "))
num2 = float(input("Número 2: "))
op = input("Operador (+, -, *, /): ")

if op == '+':
    print("Resultado:", num1 + num2)
elif op == '-':
    print("Resultado:", num1 - num2)
elif op == '*':
    print("Resultado:", num1 * num2)
elif op == '/' and num2 != 0:
    print("Resultado:", num1 / num2)
else:
    print("Error o división entre cero")