#Solicita dos números enteros al usuario y determina cuál es el mayor. 
#Si son iguales, indica que son iguales. Usa estructuras condicionales.

n1 = int(input("Ingresa Dato 01 : "))
n2 = int(input("Ingresa Dato 02 : "))

if n1>n2:
    print("El Dato Mayor es: ", n1)
elif n2>n1:
    print("El Dato Mayor es: ", n2)
else:    
    print("Ambos datos son iguales. ")
    