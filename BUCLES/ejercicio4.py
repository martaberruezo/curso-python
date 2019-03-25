#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la 
#cuenta atrás desde ese número hasta cero separados por comas.

n = int(input("Escriba un número entero positivo: "))              #??????????????????????????????
for i in range(n+1, 0):
    print(i, end=", ")
