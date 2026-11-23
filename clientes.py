
from entidades import Persona
from excepciones import ErrorCliente


class Cliente(Persona):

    def __init__(self, nombre, documento, telefono):
        if not nombre.strip():
            raise ErrorCliente("El nombre no puede estar vacío")

        if not documento.strip():
            raise ErrorCliente("El documento es obligatorio")

        super().__init__(nombre, documento, telefono)

    def mostrar_informacion(self):
        return (
            f"Nombre: {self.nombre} | "
            f"Documento: {self.documento} | "
            f"Teléfono: {self.telefono}"
        )
