# Ejercicio de listas 5

# Método para crear la lista
def crear():
    n=int(input("Digite la cantidad de palabras de la lista: "))
    lista=[]
    for i in range(n):
        lista.append(input("Digite la palabra número {}: ".format(i+1)))
    return lista

#Método de eliminación
def eliminate(lista, m):
    lista=[x if x!=m else None for x in lista]
    while(lista.count(None)!=0):
        lista.pop(lista.index(None))
    return lista

#Metodo de eliminación listas
def eliminateL(lista1, lista2):
    for i in range(len(lista2)):
        lista1=eliminate(lista1,lista2[i])
    return lista1

# Ejecución
lista1=crear()
lista2=crear()
print(eliminateL(lista1,lista2))