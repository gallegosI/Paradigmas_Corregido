#==================================
#   Jimenez Gallegos Ivan 
#==================================
#   Paradigmas de Prpgramacion
#   Matemática Algoritmica
#   ESFM-IPN    Oct-2025
#==================================

#===========================================
#   Uso de reducciones (colapsar resultados)
#===========================================

#===================================================
#   Multiplicacion de todos los numeros en la lista
#===================================================

from functools import reduce 

bigdata = [2,3,5,7,11,13,17,19,23,29]

#===============
#   Funcion x*y
#===============
multiplicar = lambda x,y: x*y
suma = lambda x,y: x+y

print(reduce(multiplicar,bigdata))
print(reduce(suma,bigdata))

#=============================================================
#   Reduce le aplica la funcion por partes a los resultados y
#   el siguiente elemento comenzado con los dos primeros 
#   elementos.
#=============================================================
