#==================================
#   Jimenez Gallegos Ivan 
#==================================
#   Paradigmas de Programacion
#   Matemática Algoritmica
#   ESFM-IPN    Dic-2024
#=================================

from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# Asegúrate de que haya exactamente dos procesos
if comm.Get_size() != 2:
    raise ValueError("Este código debe ejecutarse con exactamente 2 procesos.")

# Ejemplo 1: Usando enteros
if rank == 0:
    # Crear un arreglo de enteros del 0 al 9
    data = numpy.arange(10, dtype='i')
    # Envío bloqueante especificando el tipo de dato
    comm.Send([data, MPI.INT], dest=1, tag=77)

elif rank == 1:
    data = numpy.empty(10, dtype='i')
    # Recibir el arreglo de enteros
    comm.Recv([data, MPI.INT], source=0, tag=77)
    print("Proceso 1 recibió:", data)

# Ejemplo 2: Usando flotantes
if rank == 0:
    data = numpy.arange(10, dtype=numpy.float64)
    # Enviar arreglo de flotantes
    comm.Send(data, dest=1, tag=13)

elif rank == 1:
    data = numpy.empty(10, dtype=numpy.float64)
    # Recibir arreglo de flotantes
    comm.Recv(data, source=0, tag=13)
    print("Proceso 1 recibió flotantes:", data)

