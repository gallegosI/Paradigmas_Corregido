#=================================
# Jimenez Gallegos Ivan
#=================================
#  Matemática Algorítmica
#  Paradigmas de Programación
#  ESFM IPN Diciembre 2024
#=================================
import ray
ray.init()

#==========
#  Función 
#==========
@ray.remote
def f(x):
    return x * x

#==========
#  Objeto
#==========
@ray.remote
class Contador(object):
    def __init__(self):
        self.n = 0

    def incremento(self):
        self.n += 1

    def leer(self):
        return self.n

#=====================
#  Programa principal
#=====================
if __name__ == "__main__":
  #=============================================
  #  Correr una función en paralelo-distribuído
  #=============================================
  resultados = [f.remote(i) for i in range(16)]
  print("Resultado (funciones) = ", ray.get(resultados)) # resultado = [0, 1, 4, 9, ...]

  #========================================================
  #  Instanciar múltiples objetos en paralelo-distribuído
  #========================================================
  contadores = [Contador.remote() for i in range(16)]
  for i in range(100):
    [c.incremento.remote() for c in contadores]
  resultados = [c.leer.remote() for c in contadores]
  print("Resultado (objetos) = ", ray.get(resultados)) # resultado = [1, 1, 1, 1, ...]


