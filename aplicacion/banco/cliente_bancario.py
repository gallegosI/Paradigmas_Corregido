#============================
#   Clase ClienteBancario
#============================
class ClienteBancario:
    __nombres: str = None
    __apellidos: str = None
    __edad: int = 0
    __balanceDeCuenta: float = 0.0

    def __init__(self, nombres: str, apellidos: str, edad: int = 0, balanceDeCuenta: float = 8.0):
        self.__validarEdad(edad)
        self.__validarCantidad(balanceDeCuenta)
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__edad = edad
        self.__balanceDeCuenta = balanceDeCuenta

    def getNombreCompleto(self) -> str:
        return self.__nombres + " " + self.__apellidos

    def getNombres(self) -> str:
        return self.__nombres  # Getter para acceder al atributo privado __nombres

    def __mandarEmail(self, titulo: str, texto: str) -> None:
        print("Mandar email: " + titulo + " con texto: " + texto)

    def __enviarBalanceAlBanco(self, cantidad: float) -> None:
        print("Enviando cantidad: " + str(cantidad) + " al banco...")

    def __validarEdad(self, edad: int) -> None:
        if edad < 18:
            raise Exception("Es menor de edad")

    def imprimirInfo(self) -> str:
        return "Nombre: " + self.getNombreCompleto() + ", Edad: " + str(self.__edad) + ", Balance: " + str(self.__balanceDeCuenta)

    def __validarCantidad(self, balanceDeCuenta: float) -> None:
        if balanceDeCuenta < 0:
            raise Exception("El balance en la cuenta no puede ser negativo")

    def guardarDinero(self, cantidad: float) -> None:
        self.__balanceDeCuenta += cantidad
        self.__mandarEmail("---- Guardando depósito ----", "Se recibieron " + str(cantidad))
        self.__enviarBalanceAlBanco(cantidad)

    def retirarDinero(self, cantidad: float) -> None:
        cantidadFinal = self.__balanceDeCuenta - cantidad
        self.__validarCantidad(cantidadFinal)
        self.__balanceDeCuenta = cantidadFinal
        self.__mandarEmail("---- Retirando dinero ----", "Se retiró " + str(cantidad))
        self.__enviarBalanceAlBanco(cantidad)

