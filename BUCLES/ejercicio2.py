#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha
#cumplido (desde 1 hasta su edad).


age = int(input ("¿Qué edad tienes: "))
for i in range(age):
    print("Cumpliste " + str(i) + " años")