#Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
      #Renta	    Tipo impositivo
    #Menos de 10000€	        5%
    #Entre 10000€ y 20000€	 15%
    #Entre 200000€ y 35000€	 20%
    #Entre 350000€ y 60000€	 30%
    #Más de 60000€	         45%
#Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo 
#impositivo que le corresponde.
income = float(input("¿cual es tu renta anual?: ")) 
if income < 10000:
  print("5%")
elif 10000 < income < 20000:
  print("15%")
elif 20000 < income < 35000:
  print("20%")
elif 35000 < income < 60000:
  print("30%")
elif income > 60000:
  print("45%")

#el 7,8,9 y 10 son los mismos ejercicios que en "TIPOS DE DATOS SIMPLES"