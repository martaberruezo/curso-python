#Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.


palabra= input("Introduzca una palabra: ")                    #?????????????????????????????
palabra = list(palabra)
print(palabra)
reversa = palabra
reversa.reverse()
print(reversa)
if palabra == reversa:
    print("es un palíndromo")
else:
    print("no es un palíndromo")
