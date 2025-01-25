
#==================================
#   Jimenez Gallegos Ivan 
#==================================
#   Paradigmas dee Prpgramacion
#   Matemática Algoritmica
#   ESFM-IPN    sept-2025
#==================================

" ESTE ES UN SUB COMENTARIO DE INICIO A NUESTRO RESUMEN"

#====================
# Operaciones básicas
#====================
print (2+3)
print (2*3)
print (2/3)
print (2**10)
print (2**0.5)  #raíz cuadrada
print (10%2)
print (10%0.1)  #exclusivo en python

#=========================================
#Para saber el tipo de objeto se usa type
#=========================================
t=0
print(type(t))  #entero
t=3.6
print(type(t))  #real (flotante)
t=True
print(type(t))  #booleano (bool)

#=================================================
#   Continuar una instrucción en varios renglones
#=================================================
if 100 > 99 and \
   200 <= 300 and \
   True != False:
       print("!Hola a todos!")

#=========================================
#   Comandos diferentes en la misma linea
#=========================================
print("Hola"); print("tú")  #Se considera mala práctica

#==================================================
#   Usando paréntesis redondos, cuadrados o llaves
#   se puede escribir en varios renglones 
#==================================================
lista = [1, 2, 3, 4,
         5, 6, 7, 8,
         9, 10, 11, 12]

matriz = [ [1,2,3,4],[5,6,7,8],[9,10,11,12] ]

print(lista)
print(matriz)

#====================================================================
#   Identación estricta para procesos dependiented de : (dos puntos)
#====================================================================
if 10>5:
    print ("Diez es mayor que cinco")
    print ("otra iterción")
for i in lista: 
    print (i)
    print ("ok")
if 10>5:
    print ("Verdadero")
    if 10<20:
        print ("Verdadero")
elif 5>3:   #Comienxa segunda condicional 
    print ("Esto no se imprimira")
else :
    print /("Aquí nunca llega")

#=============
#   Funciones
#=============
def saludar (nombre):
    print ("Hola", nombre)
    print ("BIenvenido al tutorial de python")

saludar ("Iván")

