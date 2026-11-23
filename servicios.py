
from abc import ABC, abstractmethod


class Servicio(ABC):

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def mostrar_servicio(self):
        pass


class Instalacion(Servicio):

    def mostrar_servicio(self):
        return f"{self.nombre} - ${self.precio:,.0f}"


class Mantenimiento(Servicio):

    def mostrar_servicio(self):
        return f"{self.nombre} - ${self.precio:,.0f}"


class Reparacion(Servicio):

    def mostrar_servicio(self):
        return f"{self.nombre} - ${self.precio:,.0f}"


servicios_disponibles = [
    Instalacion("Instalación", 80000),
    Mantenimiento("Mantenimiento", 60000),
    Reparacion("Reparación", 100000)
]
