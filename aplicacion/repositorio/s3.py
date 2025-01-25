from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios
from aplicacion.modelos.usuario import Usuario

#======================================
# S3 es hijo de RepositorioDeUsuarios
#======================================
class S3(RepositorioDeUsuarios):
    def __init__(self, clientId: str, secretKey: str, bucket: str):
        self.clientId = clientId
        self.secretKey = secretKey
        self.bucket = bucket

    def abrir(self) -> None:
        print(f"Estableciendo conexión a AWS S3 {self.clientId}:{self.secretKey}")
    
    def guardar(self, usuario: Usuario) -> None:
        userData = {
            "nombre": usuario.getNombre(),
            "apellido": usuario.getApellido(),
            "edad": usuario.getEdad()
        }
        print(f"Guardando usuario en la bandeja: {self.bucket}: {userData}")

    def cerrar(self) -> None:
        print("Cerrando conexión AWS S3")

