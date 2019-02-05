# Ejercicio de listas 8

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

# Método de intersección
def intersection(lista1, lista2):
    a = set(lista1)
    b = set(lista2)
    return list(b & a)

# Método complemento
def complemento(lista1, lista2):
    a = set(lista1)
    b = set(lista2)
    return list(a - b)

def union(lista1, lista2):
    a = set(lista1)
    b = set(lista2)
    return list(a | b)

# Ejecución
lista1=DeleteDuplicates(crear())
lista2=DeleteDuplicates(crear())
print(intersection(lista1, lista2))
print(complemento(lista1, lista2))
print(complemento(lista2, lista1))
print(union(lista2, lista1))