# Calculadora

# Validación de los número (este método no es de mi autoría lo encontré en la Web)
def Numero():
    correcto = False
    num = 0
    while(not correcto):
        try:
            num = float(input("Ingrese un número: "))
            correcto = True
        except ValueError:
            print("Error")
    return num

# Clase
class CalculadoraBasica:
    # Método constructor
    def __init__(self):
        self.a = Numero()
        self.b = Numero()

    # Suma
    def suma(self):
        print("La suma: {} + {} = {}".format(self.a,self.b,self.a+self.b))

    # Resta
    def resta(self):
        print("La resta: {} - {} = {}".format(self.a,self.b,self.a-self.b))

    #Multiplicación
    def multiplicacion(self):
        print("La multiplicación: {} * {} = {}".format(self.a,self.b,self.a*self.b))

    #División
    def division(self):
        if self.b!=0:
            print("La división: {} / {} = {}".format(self.a,self.b,self.a/self.b))
        else:
            print("Indefinido")

#Ejecución
operacion = CalculadoraBasica()
operacion.suma()
operacion.resta()
operacion.multiplicacion()
operacion.division()