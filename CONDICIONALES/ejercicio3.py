#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
#Si el divisor es cero el programa debe mostrar un error.

numero1 = float(input("numero dividendo: "))
numero2 = float(input("numero divisor: "))
if numero2 == 0:                                    #con que haya un 0 ya es 0 la solución
    print("error, no se puede dividir entre 0.")
else:
    print(numero1/numero2)