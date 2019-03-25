#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte 
#al usuario por la contraseña hasta que introduzca la contraseña correcta.


password = "pepito"
c =""
while  c != password:                                   
    c= input("Introduzca la contraseña: ")            #hay que poner c = input ....
print("contraseña correcta")