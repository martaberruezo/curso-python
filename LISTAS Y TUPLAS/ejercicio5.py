#Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por 
#pantalla en orden inverso separados por comas.

numbers = [1,2,3,4,5,6,7,8,9,10]
numbers.reverse()
#numbers                          #si pongo solo eso hasta ahi me sale la lista con los numeros al reves
for i in numbers:
    print(i, end=",")