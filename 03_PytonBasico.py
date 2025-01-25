#==================================
#   Jimenez Gallegos Ivan 
#==================================
#   Paradigmas dee Prpgramacion
#   Matemática Algoritmica
#   ESFM-IPN    sept-2025
#==================================

#===================================================          
#	Listas 
#	Las listas pueden ser de objetos diferentes
#===================================================          
miprimeralista = []	# Lista vacìa
print(miprimeralista)

#=======================                        
#	LLenado de lista
#=======================                        
miprimeralista = [1,"Javier",1.34,"Bosco","Angel","Abigai",True]
print(miprimeralista)

#=============================================       
#	List: hacer una lista
#	range(i,j): secuencia de i hasta j-1
#=============================================
nums = list(range(1,61))

for i in nums:
	print(i)

#=====================================       
#	Incluir elementos de la lista
#=====================================
nums.append(61)
nums.append(62)
nums.append(61)
print(nums)
 
#=====================================
#       Quitar  elementos de la lista
#=====================================
nums.remove(61)
print(nums)

#=====================================
#       Quitar elementos con indice i
#=====================================
i = 61
del nums[i]
print(nums)

#==========================
#	Borrar la lista
#==========================
del nums

#==========================
#	Sumar la lista
#==========================
L1 = [1,2,3]
L2 = [4,5,6]
print(L1+L2)

#==========================
#	Llenado a mano
#==========================
potencial = []
for i in range(0,10000):
	potencial.append(float(i))
print(potencial[100])
