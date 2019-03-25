#Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
#los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

ganadores= []
for i in range(6):                                               #como sabes que es 6???
    c = int(input("¿números ganadores de la loteria primitiva?: "))
    ganadores.append(c)
ganadores.sort()
print("los ganadores son" + str(ganadores))