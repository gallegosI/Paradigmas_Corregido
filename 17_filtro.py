#==================================
#   Jimenez Gallegos Ivan 
#==================================
#   Paradigmas de Programacion
#   Matemática Algoritmica
#   ESFM-IPN    Oct-2025
#==================================

#==================
#   Uso de filtros
#==================

#========================================================
# Hacer una lista de los números por arriba del promedio
#========================================================

# Módulo de estadística
import statistics

bigdata = [1.3,2.7,0.8,4.1,4.3,-0.1]
promedio = statistics.mean(bigdata)
print(promedio)

#====================================================================
# Hazme una lista de elementos que cumplan la condición x > promedio
# filter( condición, datos )
#====================================================================
print(list(filter (lambda x: x> promedio, bigdata)))

#===================
# Limpiar los datos
#===================
paises = ["", "Argentina", "", "Brasil", "", "Chile", "Mexico", "", "Colombia", "", "", "Cuba", "Venezuela"]

#===================================
#   Filtra lo que no contienen nada
#===================================
print(list(filter(None, paises)))
