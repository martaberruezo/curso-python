#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

for i in range(0,11):                  #poner 11 porque le resta 1
    for j in range(0,11):
        print( i*j, end=" ")           #¿como sabes que es end= "\t"    t es tabulación
    print(" ")