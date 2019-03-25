#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de 
#masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa 
#corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.


peso = float(input("cual es tu peso: "))
estatura = float(input("cual es tu estatura: "))
IMC = peso/(estatura**2)
x = round(IMC, 2)                                   #round es para redondear IMC con 2 decimales
print(x)
