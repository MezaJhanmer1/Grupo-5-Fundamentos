numero = int(input("Coloca un numero para realizar su tabla de multiplicar del 1 al 10: "))

for i in range(1,11):
    print(f"{numero} x {i} =  {i * numero}")