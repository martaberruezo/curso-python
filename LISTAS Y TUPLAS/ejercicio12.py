#Escribir un programa que almacene las matrices 𝐴=(142536)𝑦𝐵=⎛⎝⎜⎜⎜⎜⎜−101011⎞⎠⎟⎟⎟⎟⎟
#en una lista y muestre por pantalla su producto.
#Nota: Para representar matrices mediante listas usar listas anidadas, representando cada 
#vector fila en una lista.


a = [[2,4,3],[5,1,2]]
b = [[2,1],[3,1],[4,3]]
c = [[0,0],[0,0]]
for i in range(2):
    for j in range(2):
        for k in range(3):
            c[i][j] += a[i][k]*b[k][j]
print(c[0])
print(c[1])
