#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, 
#Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada 
#asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por 
#pantalla las asignaturas que el usuario tiene que repetir.

                     #*************************************************

asignaturas = ["Matemáticas","Física", "Química", "Historia", "Lengua"]        #?????????????????
notas =[]
for i in asignaturas:
    resultado = float(input( "¿Qué nota has sacado en " + i + "?: "))
    if resultado >=5:
        notas.append(resultado)
for a in notas:
    asignaturas.remove(a)
print("tienes que repetir " + str(asignaturas))

    

