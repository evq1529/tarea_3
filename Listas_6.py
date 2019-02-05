# Ejercicio de listas 6

# Método para crear la lista
def crear():
    n=int(input("Digite la cantidad de palabras de la lista: "))
    lista=[]
    for i in range(n):
        lista.append(input("Digite la palabra número {}: ".format(i+1)))
    return lista

# Método para darle vuelta a una lista
def crearReverse(lista):
    return lista[::-1]

# Ejecución
lista1=crear()
lista2=crearReverse(lista1)
print(lista2)
print(lista1==lista2)