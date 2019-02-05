# Ejercicio de listas 2

# Método para crear la lista
def crear():
    n=int(input("Digite la cantidad de palabras de la lista: "))
    lista=[]
    for i in range(n):
        lista.append(input("Digite la palabra número {}: ".format(i+1)))
    return lista

# Método para contar los elementos repetidos
def contador(lista, m):
    return lista.count(m)

#Ejecución
lista=crear()
m=input("Digite la palabra a buscar: ")
print("La palabra aparece {} veces".format(contador(lista, m)))