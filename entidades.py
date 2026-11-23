
from abc import ABC, abstractmethod


class Persona(ABC):

    def __init__(self, nombre, documento, telefono):
        self._nombre = nombre
        self._documento = documento
        self._telefono = telefono

    @property
    def nombre(self):
        return self._nombre

    @property
    def documento(self):
        return self._documento

    @property
    def telefono(self):
        return self._telefono

    @abstractmethod
    def mostrar_informacion(self):
        pass
