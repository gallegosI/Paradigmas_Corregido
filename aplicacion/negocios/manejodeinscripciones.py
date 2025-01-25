from aplicacion.modelos.usuario import Usuario
from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios

# =================================
#   Clase ManejoDeInscripciones
#   NO TIENE VARIABLES !!!
# =================================
class ManejoDeInscripciones:
    # =====================================================================
    #   Decorador staticmethod
    #   El objeto solo tiene la función inscribirUsuario
    #   ENVUELVE LA FUNCIÓN SIN LLAMAR VARIABLES LOCALES
    #   El objeto ManejoDeInscripciones es la interface intercambiable
    # =====================================================================
    @staticmethod
    def inscribirUsuario(usuario: Usuario, repositorioDeUsuarios: RepositorioDeUsuarios) -> None:
        """
        Inscribe un usuario en el repositorio especificado.
        
        :param usuario: Objeto Usuario que contiene la información del usuario.
        :param repositorioDeUsuarios: Objeto RepositorioDeUsuarios donde se guardará el usuario.
        """
        print(" -----> Guardando usuario ... \n")
        repositorioDeUsuarios.abrir()
        repositorioDeUsuarios.guardar(usuario)
        repositorioDeUsuarios.cerrar()

