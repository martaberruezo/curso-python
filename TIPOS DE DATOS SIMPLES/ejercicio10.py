#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte 
#al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario 
#coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

     #AQUI NO HACE FALTA [], SOLO SE NECESITA 4 ESPACIOS

contraseña = input("introduzca contraseña: ")
if contraseña.lower() == "pepito":                 #lower es para ignorar si es mayuscula o minuscula
    print("contraseña correcta")                       
else:
    print("contraseña incorrecta")
 