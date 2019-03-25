#igual que el de 10 de TIPOS DE DATOS SIMPLES

#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de 
#años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

amount = float(input("¿cantidad a invertir: "))
interest = float(input("interés (porcentual) anual: "))
years = int(input("número de años: "))
print("El capital obtenido es " + str(amount*(interest/100+1)*years))