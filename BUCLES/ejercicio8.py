#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo 
#rectángulo como el de más abajo, de altura el número introducido.
#1
#3 1
#5 3 1
#7 5 3 1
#9 7 5 3 1

m= int(input("Introduzca número entero: "))          
for i in range(1,m,2):
    for j in range(i,0,-2):                    # tiene que ir de i a 0 restandole 2 cada vez
        print(j, end=" ")                      #PONER PRINT J
    print(" ")

