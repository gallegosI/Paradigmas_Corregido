#==================================
#   Jiménez Gallegos Iván
#==================================
#   Paradigmas de Programación
#   Matemática Algorítmica
#   ESFM-IPN    Sept-2025
#===================================

#===================================
#   Importación de módulos  
#   Contienen objetos y funciones
#===================================
import matplotlib.pyplot as grafica
import math

#===================================
#   Función exponencial
#   Serie de Taylor
#   Polinomio en orden
#===================================
def exponencial(n: int = 1500, x: float = 0.5):
    """
    Calcula la exponencial de x usando la serie de Taylor.
    n: Número de términos de la serie.
    x: Valor para el cual se calcula la exponencial.
    """
    factorial = 1.0
    exponencial_de_x = 1.0
    x_a_la_n = 1.0
    for i in range(1, n):
        x_a_la_n *= x
        factorial *= float(i)
        termino = x_a_la_n / factorial
        exponencial_de_x += termino
    return exponencial_de_x

def exponencial_pro(n: int = 1500, x: float = 0.5):
    """
    Calcula la exponencial de x usando una optimización de la serie.
    n: Número de términos de la serie.
    x: Valor para el cual se calcula la exponencial.
    """
    flag = False
    if x < 0:
        flag = True
        x = -x
    resultado = 1.0
    for i in range(n, 0, -1):
        resultado *= x / float(i)
        resultado += 1.0
    if flag:
        resultado = 1 / resultado
    return resultado

#===================================
#   Configuración de la gráfica
#===================================
m = 400  # Número de puntos
serie = 250  # Número de términos en la serie
error1 = []
error2 = []
x0 = 0.0
x = [x0 + n * 0.1 for n in range(m)]  # Genera valores de x en un rango

# Calcula los errores para cada valor de x
for i in range(m):
    y = x0 + 0.1 * i
    error1.append(exponencial(serie, y) - math.exp(y))
    error2.append(exponencial_pro(serie, y) - math.exp(y))

#===================================
#   Graficar los resultados
#===================================
grafica.subplot(211)
grafica.plot(x, error1, label="Error exponencial (Taylor)")
grafica.xlabel("x")
grafica.ylabel("Error")
grafica.title("Error de la serie de Taylor")
grafica.legend()

grafica.subplot(212)
grafica.plot(x, error2, label="Error exponencial (Optimizado)", color="orange")
grafica.xlabel("x")
grafica.ylabel("Error")
grafica.title("Error de la serie optimizada")
grafica.legend()

grafica.tight_layout()
grafica.show()

