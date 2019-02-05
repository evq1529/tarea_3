# Ejercicio de listas 7

# Método para crear la lista
def crear():
    n=int(input("Digite la cantidad de palabras de la lista: "))
    lista=[]
    for i in range(n):
        lista.append(input("Digite la palabra número {}: ".format(i+1)))
    return lista

#Método de eliminación por componente
def eliminateComp(lista, m):
    lista=[x if x!=m else None for x in lista]
    lista[lista.index(None)]=m
    while(lista.count(None)!=0):
        lista.pop(lista.index(None))
    return lista

#Método DeleteDuplicates
def DeleteDuplicates(lista):
    list=lista
    for i in range(len(lista)):
        list=eliminateComp(list,lista[i])
    return list

# Ejecución
lista=crear()
print(DeleteDuplicates(lista))