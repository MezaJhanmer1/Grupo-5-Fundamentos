#Solicita dos números y un operador (+, -, *, /). Usa una estructura
#Según para determinar la operación. Maneja el caso de división por
#cero con una condicional
print("CALCULADORA")
#COLOCAR VARIABLES
n1=float(input("Colocar el primer Número :"))
print("----------------------------------")
n2=float(input("Colocar el segundo Número : "))
print ("---------------------------")
v1=input(" Que operacion desea + ,-,*,/ : ")
print ("---------------------------")
#COLOCAR LA CONDICIONAL
if v1 == "+" :
#USAR LA VARIABLE "OPERCACION" PARA QUE GUARDE EL VALOR OBTENIDO DE LAS OPERACIONES
    operacion= n1+n2
elif v1== "-":
  operacion= n1-n2
elif v1=="*" :
   operacion= n1*n2
elif v1== "/" :
# COLOCAR UN != -> NO ES IGUAL A 0 PARA EVITAR EL ERROR DE DIVISION ENTRE 0
 if n2!=0:
   operacion =n1/n2
 else:
      print("no se puede dividir entre 0")
else:
   print("operacion no valida")
print(F"el RESULTADO DE SU OPERACION ES : {operacion}")
   
      
      


  

    
