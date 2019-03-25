#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al 
# usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario 
# coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

      #IGUAL QUE EL 10 DE "TIPOS DE DATOS SIMPLES"



x = "pepito"
contraseña = input("introduce la contraseña: ")
if contraseña.lower() == x:                       #lower es par mayusculas
    print("contraseña correcta")
else:
    print("contraseña incorrecta")



