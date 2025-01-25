#==================================
#   Jimenez Gallegos Ivan
#==================================
#   Paradigmas de Programacion
#   Matemática Algoritmica
#   ESFM-IPN    Oct-2025
#==================================

#===========================================
#   Curvas Z-splines en n dimensiones
#===========================================
#   Jimenez Gallegos Ivan ESFM IPN 2024
#===========================================
import numpy as np
import matplotlib.pyplot as plt

#===========================================
#   Función zspline
#   Genera una curva Z-spline en 2D
#===========================================
def zspline(p, d, n, m):
    """
    Genera una curva Z-spline en 2D.
    Parámetros:
        p: np.array - Puntos de control (1D, concatenados por coordenadas).
        d: int - Dimensión de los puntos.
        n: int - Número de segmentos en la curva.
        m: int - Continuidad (0: lineal, 1: suavidad C1, 2: suavidad C2).
    Retorna:
        x, y: Coordenadas interpoladas de la curva.
    """
    num_puntos = len(p) // d
    t = np.linspace(0, 1, n)
    x = np.interp(t, np.linspace(0, 1, num_puntos), p[:num_puntos])
    y = np.interp(t, np.linspace(0, 1, num_puntos), p[num_puntos:])
    return x, y

#=======================
#   Conjunto de puntos
#=======================
# Número de puntos
nump: np.int32 = 8
# Dimensión
dim: np.int32 = 2
# Memoria para puntos
puntos = np.zeros(dim * nump, dtype=np.float64)
# Parametrización
X = np.linspace(0.0, 2 * np.pi, nump + 1)
# Coordenada x
puntos[0:nump] = np.cos(X[0:nump]) + 0.0 * np.sin(2 * X[0:nump])
# Coordenada y
puntos[nump:2 * nump] = np.sin(X[0:nump]) + 0.0 * np.sin(2 * X[0:nump])

#==================================================================
#   Curva Z-spline de n puntos zspline(p, d, n, m)
#   p: puntos, d: dimensión, n: segmentos de curva, m: continuidad
#==================================================================
n: np.int32 = 1000
x1, y1 = zspline(puntos, dim, n, 2)  # Continuidad C2
x2, y2 = zspline(puntos, dim, n, 1)  # Continuidad C1
x3, y3 = zspline(puntos, dim, n, 0)  # Continuidad C0

#=======================
#   Graficar resultados
#=======================
plt.plot(x3, y3, lw=3, color="orange", label="C0 (lineal)")
plt.plot(x2, y2, lw=3, color="red", label="C1 (suave)")
plt.plot(x1, y1, lw=3, color="blue", label="C2 (muy suave)")
plt.scatter(puntos[0:nump], puntos[nump:2 * nump], marker='o', color='black', label="Puntos de control")
plt.xlabel("Coordenada x")
plt.ylabel("Coordenada y")
plt.title("Curva cerrada Z-spline en 2D")
plt.legend()
plt.show()

