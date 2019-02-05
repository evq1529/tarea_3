# Ejercicio de listas 4

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


# Ejecución
lista=crear()
m=input("Digite la palabra que se desea eliminar: ")
print(eliminate(lista, m))