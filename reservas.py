
from excepciones import ErrorReserva


class Reserva:

    contador = 1

    def __init__(self, cliente, servicio):
        if cliente is None or servicio is None:
            raise ErrorReserva("Cliente y servicio son obligatorios")

        self._codigo = Reserva.contador
        Reserva.contador += 1

        self._cliente = cliente
        self._servicio = servicio
        self._estado = "Activa"

    @property
    def codigo(self):
        return self._codigo

    @property
    def estado(self):
        return self._estado

    def cancelar(self):
        if self._estado != "Activa":
            raise ErrorReserva("La reserva no está activa")

        self._estado = "Cancelada"

    def completar(self):
        if self._estado != "Activa":
            raise ErrorReserva("La reserva no está activa")

        self._estado = "Completada"

    def mostrar_reserva(self):
        return (
            f"Reserva: {self.codigo} | "
            f"Cliente: {self._cliente.nombre} | "
            f"Servicio: {self._servicio.nombre} | "
            f"Precio: ${self._servicio.precio:,.0f} | "
            f"Estado: {self._estado}"
        )
