#Solicita dos números enteros al usuario y
#determina cuál es el mayor. Si son iguales,
#indica que son iguales. Usa estructuras
#condicionales.

#solicitamos el valor de los dos números
n1=int(input("Colocar el primer número : "))
n2=int(input("Colocar el segundo número : "))
#COLOCO LA CONDICIONALES PARA OBTENER EL RESULTADO REQUERIDO
if n1>n2 :
 print ("EL PRIMER NÚMERO ES MAYOR")
elif n2>n1 :
   print("EL SEGUNDO NÚMERO ES MAYOR")
else :
  print ("LOS NÚMEROS TIENEN EL MISMO VALOR" )
  