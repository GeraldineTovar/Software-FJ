
class ErrorSistema(Exception):
    """Excepcion general del sistema Software FJ."""
    pass


class ErrorCliente(ErrorSistema):
    """Errores relacionados con los clientes."""
    pass


class ErrorServicio(ErrorSistema):
    """Errores relacionados con los servicios."""
    pass


class ServicioNoDisponibleError(ErrorServicio):
    """Se presenta cuando un servicio no esta disponible."""
    pass


class ErrorReserva(ErrorSistema):
    """Errores relacionados con las reservas."""
    pass


class ReservaNoPermitidaError(ErrorReserva):
    """Operaciones no permitidas en una reserva."""
    pass


class ErrorOperacion(ErrorSistema):
    """Errores generales de funcionamiento."""
    pass


class DatosInvalidosError(ErrorSistema):
    """Datos ingresados incorrectamente."""
    pass

