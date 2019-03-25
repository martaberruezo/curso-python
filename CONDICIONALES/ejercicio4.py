#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
numero = int(input("introduce numero entero: "))
if numero % 2 == 0:
    print(" par")
else:
    print("impar")

#Para acceder tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos 
#iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus 
#ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

age = int(input ("¿cual es tu edad?: "))
income= float(input ("¿cuales son tus ingresos?: "))
if age>16 and income>1000:                                  #si quieres poner dos condiciones pones AND
    print("tienes que cotizar")
else:
    print("no tienes que cotizar")

