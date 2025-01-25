class Usuario:
    __nombre: str
    __apellido: str
    __edad: int

    #===============
    #   Constructor
    #===============
    def __init__(self, nombre: str, apellido: str, edad: int):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad

    #=============
    #   Getters
    #=============
    def getNombre(self) -> str:
        return self.__nombre

    def getApellido(self) -> str:
        return self.__apellido  # Corregido: Acceder correctamente al atributo __apellido

    def getEdad(self) -> int:
        return self.__edad

