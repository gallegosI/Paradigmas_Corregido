#=========================================
#   Jimènez Gallegos Ivan
#=========================================
#  Paradigmas de Programación
#  Matemática Algorítmica
#  ESFM IPN  Diciembre 2024
#=========================================
import numpy as np 
from pylab import imshow, show
from timeit import default_timer as timer
from numba import jit
from numba import cuda
from numba import *

#=============================
#  Función mandel en el CPU 
#=============================
@jit
def mandel(x, y, max_iters):
    c = complex(x,y)
    z = 0.0j
    for i in range(max_iters):
        z = z*z + c
        if (z.real*z.real + z.imag*z.imag) >= 4:
            return i
    return max_iters

#===========================
#  Función mandel en el GPU
#===========================
mandel_gpu = cuda.jit(device=True)(mandel)

#==================
#  Kernel de cuda 
#==================
@cuda.jit
def mandel_kernel(min_x, max_x, min_y, max_y, image, iters):
    width = image.shape[0]
    height = image.shape[1]

    pixel_size_x = (max_x-min_x)/width
    pixel_size_y = (max_y-min_y)/height

    startX, startY = cuda.grid(2)
    gridX = cuda.gridDim.x*cuda.blockDim.x
    gridY = cuda.gridDim.y*cuda.blockDim.y

    for x in range(startX,width,gridX):
        real = min_x + x*pixel_size_x
        for y in range(startY,height,gridY):
            imag = min_y + y*pixel_size_y
            color = mandel(real, imag, iters)
            image[x,y] = mandel_gpu(real,imag,iters)

#======================
#  Programa principal
#======================
if __name__ == "__main__":

  gimage = np.zeros((1024,1536), dtype = np.uint8)
  blockdim = (32,32)
  griddim = (32,64)

  start = timer()
  d_image = cuda.to_device(gimage)
  mandel_kernel[griddim, blockdim](-2.0,1.0,-1.0,1.0,d_image,20)
  gimage = d_image.copy_to_host()
  dt = timer()-start

  print("Fractal Mandelbrot creado en el GPU en %f s" % dt)
  imshow(gimage)
  show()
