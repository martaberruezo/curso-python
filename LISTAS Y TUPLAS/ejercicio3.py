#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, 
#Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada 
#asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> 
#donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las 
#correspondientes notas introducidas por el usuario.

asignaturas = ["Matemáticas","Física", "Química", "Historia", "Lengua"]
notas = []
for a in asignaturas:
    c =input("¿Qué has sacado en " + a + "?:")        
    notas.append(c)                                  #cuando haces append añade dato a notas
for i in range(len(asignaturas)):                    #te calcula longitud de asignaturas, y te imprime
    print("En " + asignaturas[i] + " has sacado " + notas[i])
