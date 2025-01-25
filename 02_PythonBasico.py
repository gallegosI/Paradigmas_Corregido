#==================================
#   Jimenez Gallegos Ivan 
#==================================
#   Paradigmas dee Prpgramacion
#   Matemática Algoritmica
#   ESFM-IPN    sept-2025
#==================================

#=============================================================
#	Input permite obterner datos del usuario en promptner
#=============================================================
nombre = input("Dame tu nombre: ")
print("Hola como estàs,nombre") 

#===============================================
#	Los enteros son de precisiòn ilimitada
#===============================================
y = 5000000000000000000000000000000000000000  
print(y)

#===================================================================
#       Se pueden delimitar nùmeros con guiòn bajo pero no con coma
#===================================================================
y = 5_000_000
print(y)

#==========================================================
#       La funciòn int() cambia strings y floats a enteros
#==========================================================
numero=int(input("Dame tu edad"))
type(numero)

#=========================================================
#       La notaciòn cientìfica de flotantes utiliza e o E
#       1.2 x 10^{-9}  
#=========================================================
y = 1.2E-09
print(y)

#===================================================================
#       La funciòn float() convieerte strings y enteros a flotantes
#===================================================================
y = float("14.3")
print(y)

#==========================================================
#       Los complejos se escriben con la raiz de menos uno
#       j siempre con un nùmero como prefijo 
#	no acepta a la j suelta
#==========================================================
z = 1+1j

# suma +
# resta -
# multiplicacion 
# division /
# modulo %
# exponente **
# // funcion piso
# Funciones para transformal numero int() float() complex()
# Operaciones abs() round() pow()

print(round(3.14159,4))

#================================
#	Strings de varias lìneas
#================================ 
parrafo = """En el bosque de la china
 la chinita se perdio """

#======================================================  
#	La funcion len() obtiene el tamaño del string
#======================================================
n=len(parrafo)
print(n)

#=======================================================================
#	Las letras en un string ocupan como en un arrglo
#	(tambien de atras para adelante comenzando en -1 en el ultimo)
#=======================================================================
palabra = "hola"
print(palabra[0]) 
print(palabra[-4])

