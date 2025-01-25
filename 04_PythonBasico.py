#==================================
#   Jimenez Gallegos Ivan 
#==================================
#   Paradigmas dee Prpgramacion
#   Matemática Algoritmica
#   ESFM-IPN    sept-2024
#===================================

#==================================       
#	Conjunto en python
#==================================
even_nums = {2, 4, 6, 8, 10}	#Conjunto de numeros pares     
print(even_nums)

#	El boll no es parte del conjunto
emp = {1, "Steve", 10.5, True}	#Conjunto de diferentes ojetos
print(emp) 

nums = {1, 2, 3, 4, 4, 5, 5}
print(nums)

#===================================================
#	Convertir secuencia a conjunto 
#	No lo genera en orden
#===================================================
s = set("Hola")
print(s)
s = set((1,2,3,4,5))	#Tupla a conjunto
print(s)

#======================================================
#	De diccionario a conjunto: conjunto de llaves
#======================================================
d = {1:"uno",2: "dos"}
s = set(d)
print(s)

s.add(100)
print(s)

s.update(nums)
print(s)

s.remove(100)
print(s)

s1={1,2,3,4,5}
s2={4,5,6,7,8}

su = s1|s2	#Union
print(su)

si = s1&s2	#Interseccion
print(si)

sr = s1-s2	#Diferencia de conjuntos
print(sr)
 
sp = s2-s1
print(sp)

ss = s1^s2	#Diferencia simetrica
print(ss)

#==========================================
#	Uso de deccionarios
#==========================================
capitales = {"USA":"Washington D.C.", "France":"Paris","India":"New Delhi"}
print(capitales)

#==========================================
#	llave:valor
#==========================================
# 	diccionario vacio 
d = {}

#	llave entera, valor string
numeros={1:"uno", 2:"dos",3:"tres"}

#	llave real, valor string
decimales={1.5:"uno y medio", 2.5:"dos y medio", 3.5:"tres punto cinco"}  
 
#	llave tupla, valor string
cosas={("Parker","Reynolds","Camlin"):"pluma",("LG","Whirlpool","Samsumg"):"refrigerador"}

#	llave string, valor int
romanos = {"I":1, "II":2, "III":3, "IV":4, "V":5}     
print(romanos)
print(romanos["I"])

print(capitales.get("India"))
print(capitales.get("india"))

#	Reportar llave y valor
for k in capitales:
	print("key = " + k + ", Value = " + capitales[k])

# 	Nuevo dato para el diccionario
capitales["Mexico"] = "CDMX"
print(capitales)

#	Borrar dato del diccionario
del capitales["Mexico"]
print(capitales)

#	Borrar todo del diccionario
del capitales

#	Reportar llaves
print(romanos.keys())

#	Reportar valores 
print(romanos.values())

#	Juicio de la llave (esta o no esta la llave en el diccionario)
print("I" in romanos)
print("X" in romanos)
print("XX" not in romanos)
