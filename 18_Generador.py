#==================================
#   Jimenez Gallegos Ivan 
#==================================
#   Paradigmas de Programacion
#   Matemática Algoritmica
#   ESFM-IPN    Nov-2024
#==================================

#=========================================
#   yield transforma la función a iterador
#=========================================
def migenerador():
    print("Primero")
    yield 10
    print("Segundo")
    yield "20"
    print("Tercero")
    yield "hola"

#=======================
#   gen es un iterador
#=======================
gen = migenerador()
val1 = next(gen)
print(val1)
val2 = next(gen)
print(val2)
val3 = next(gen)
print(val3)
