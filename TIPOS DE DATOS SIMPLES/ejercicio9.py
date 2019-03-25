#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y
#el número de años, y muestre por pantalla el capital obtenido en la inversión.


amount = float(input("¿cantidad a invertir?: "))
interest = float(input("¿interes porcentual anual?: "))
years = int(input("¿años?: "))
print("capital final: " + str(round(amount*((interest/100)+1)*years,2)))     #no olvidarse de () finales