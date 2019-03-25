#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla
#todos los números impares desde 1 hasta ese número separados por comas.

number = int(input("Escriba un número entero positivo: "))    
for i in range(1, number+1, 2):                               #el +1 es para contar con el último número
    print(i, end=", ")


#  number = int(input("Escriba un número entero positivo: "))
#  for i in number:
   # if i%2 !=0:
    #    print(i)
   # print(i)
    

