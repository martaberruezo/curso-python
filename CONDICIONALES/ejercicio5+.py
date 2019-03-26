#otra forma de hacer el 5

nombre = input("nombre: ")
sexo = input("sexo: ")
if (nombre[0] <= "M" and sexo == "mujer") or (nombre[0] >= "N" and sexo == "hombre"):
    print("A")
else:
    print("B")

#cuando pones marta, hay problema porque pilla la m y la a, 
# entonces te lo mete en grupo B... hay que poner nombre[0]

#ESTA MAALLLL