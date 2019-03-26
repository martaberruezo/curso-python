#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo 
#rectángulo como el de más abajo, de altura el número introducido.
#*
#**
#***
#****
#*****

x = int(input("numero:"))
for i in range(0,x):
    for j in range(i+1):
        print("*", end=" ")
    print(" ")








#n= int(input("Inserte número entero para hacer triangulo: "))
#for i in range (0, n):
   # for j in range(i+1):
   #     print("*", end=" ")                              #puedes poner número(en vez de * poner j)
   # print(" ")
