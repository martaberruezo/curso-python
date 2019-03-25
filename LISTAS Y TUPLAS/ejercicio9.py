#Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces 
#que contiene cada vocal.

palabra = input("introduzca una palabra: ")
vocales =["a", "e", "i", "o", "u"]
for i in vocales:
    veces=0
    for a in palabra:
        if a==i:
            veces += 1
    print("La vocal " + i + " aparece " + str(veces) + " veces")
    
  