#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un 
#número primo o no.

             #***********************************************************************

n= int(input("¿Introduzca número entero positivo mayor de 2: ")) 
i = 2  
while n % i != 0:
    i += 1
if i==n:                          # i==n ????????????????????
    print(str(n) + " es primo")
else:
    print(str(n) +" no es primo")


#otra forma:

n= int(input("¿Introduzca número entero positivo mayor de 2: ")) 
for i in range(2,n):
    if n % i ==0:
        break
if(i+1) == n:
    print(str(n) + " es primo")
else:
    print(str(n) +" no es primo")
    