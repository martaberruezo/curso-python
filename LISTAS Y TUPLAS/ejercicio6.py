#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, 
#Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada 
#asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por 
#pantalla las asignaturas que el usuario tiene que repetir.

                     #*************************************************

asignaturas = ["Matemáticas","Física", "Química", "Historia", "Lengua"]        #?????????????????
notas =[]
for i in asignaturas:
    resultado = float(input( "¿Qué nota has sacado en " + i + "?: "))
    notas.append(resultado)
    
for a in range(len(notas)-1,0,-1):               #eso es para que no se borre
    if notas[a]>=5:
        asignaturas.pop(a)
print("tienes que repetir " + str(asignaturas))

    

