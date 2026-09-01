import math
n1 = int(input("Ingresa un numero mayor a 2: "))
for i in range(2,n1 + 1):
    num_primo = True

    for raiz in range(2, int(math.sqrt(i))+1):
        if i % raiz == 0 :
            num_primo = False
            
    if num_primo:
        print(f"Los núm. primos son : {i}")