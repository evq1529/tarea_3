# Ejercicio de listas 3

# Método para crear la lista
def crear():
    n=int(input("Digite la cantidad de palabras de la lista: "))
    lista=[]
    for i in range(n):
        lista.append(input("Digite la palabra número {}: ".format(i+1)))
    return lista

#Método de reemplazo
def reemplazar(lista, m, n):
    return [n if x==m else x for x in lista]


# Ejecución
lista=crear()
m=input("Digite la palabra que se desea sustituir: ")
n=input("Digite la palabra de sustitución: ")
print(reemplazar(lista, m, n))