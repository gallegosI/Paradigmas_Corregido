#==================================
#   Jimenez Gallegos Ivan
#==================================
#   Paradigmas de Programacion
#   Matemática Algorítmica
#   ESFM-IPN    sept-2024
#===================================

#====================================
#   Programación orientada a objetos
#====================================

#==================================
#   Una clase para un objeto vacío
#===================================
class ObjetoVacio:
    pass

#====================================================
#   Nada es la instanciación de la clase ObjetoVacio
#====================================================
nada = ObjetoVacio()
print(type(nada))

#==================
#   La clase Llanta
#==================
class Llanta:
    #========================================
    #   Variable cuenta es de toda la clase
    #========================================
    cuenta = 0

    #===========================================
    #   Función constructora de identidad 
    #   __init__ es la función reservada 
    #   comienza con uno mismo: self
    #===========================================
    def __init__(self, radio=50, ancho=30, presion=1.5):
        #   Variable de la estructura completa Llanta
        Llanta.cuenta += 1
        #   Variables exclusivas de cada objeto
        self.radio = radio
        self.ancho = ancho
        self.presion = presion

#==========================
#   Objetos (instanciados)
#==========================
llanta1 = Llanta(50, 30, 1.5)
llanta2 = Llanta(presion=1.2)
llanta3 = Llanta()
llanta4 = Llanta(40, 30, 1.6)

#=====================================
#   Objeto que contiene otros objetos
#=====================================
class Coche:
    def __init__(self, ll1, ll2, ll3, ll4):
        self.llanta1 = ll1
        self.llanta2 = ll2
        self.llanta3 = ll3
        self.llanta4 = ll4

micoche = Coche(llanta1, llanta2, llanta3, llanta4)

print("Total de llantas: ", Llanta.cuenta)  # Variable global de la clase
print("Presión de la llanta 4 = ", llanta4.presion)  # Presión de la llanta 4
print("Radio de la llanta 4 = ", llanta4.radio)
print("Radio de la llanta 3 = ", llanta3.radio)
print("Presión de la llanta 1 de mi coche = ", micoche.llanta1.presion)

#===================
#   Encapsulamiento
#===================

#===================================================
#   Uso de la función de python property y obtener
#   atributos a variables protegidas con __
#===================================================
class Estudiante:
    def __init__(self):
        self.__nombre = ""

    def ponerme_nombre(self, nombre):
        self.__nombre = nombre

    def obtener_nombre(self):
        print("Se llamó al obtener_nombre")
        return self.__nombre

    nombre = property(obtener_nombre, ponerme_nombre)

#======================================
#   Crear objeto estudiante sin nombre
#======================================
estudiante = Estudiante()

#========================================================================
#   Ponerle nombre usando la propiedad nombre y el método ponerme_nombre
#========================================================================
estudiante.nombre = "Ivan"

#========================================================================
#   Obtener el nombre con el método obtener_nombre                      
#========================================================================
print(estudiante.nombre)

#========================
#   Herencia de clases
#========================
class Cuadrilatero:
    def __init__(self, a, b, c, d):
        self.lado1 = a
        self.lado2 = b
        self.lado3 = c
        self.lado4 = d

    def perimetro(self):
        p = self.lado1 + self.lado2 + self.lado3 + self.lado4
        print("Perímetro = ", p)
        return p

#=======================================                                 
#   Su hijo Rectángulo                                                  
#=======================================
class Rectangulo(Cuadrilatero):
    def __init__(self, a, b):
        #===============================
        #   Constructor de su madre
        #===============================
        super().__init__(a, b, a, b)

#============================
#   Su nieto Cuadrado
#============================
class Cuadrado(Rectangulo):
    def __init__(self, a):
        super().__init__(a, a)

    def area(self):
        area = self.lado1 ** 2
        return area

#====================
#   Crear cuadrado
#====================
cuadrado1 = Cuadrado(5)

#=========================================================
#   Llamar al método perímetro de su abuelo Cuadrilatero
#=========================================================
perimetro1 = cuadrado1.perimetro()

#===================================
#   Llamar a su propio método área
#===================================
area1 = cuadrado1.area()

print("Perímetro = ", perimetro1)
print("Área = ", area1)

#=================================================================
#   Sobre-escribir un método de su madre o abuela o tatarabuela...
#   Es volver a definir una función ya existente
#=================================================================

