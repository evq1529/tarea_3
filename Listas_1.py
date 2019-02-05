# Ejercicio de listas 1

#Método para crear la lista
def crear():
    n=int(input("Digite la cantidad de palabras de la lista: "))
    lista=[]
    for i in range(n):
        lista.append(input("Digite la palabra número {}: ".format(i+1)))
    return lista

# Ejecución
lista=crear()
print(lista)