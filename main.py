
from clientes import Cliente
from servicios import servicios_disponibles
from reservas import Reserva
from excepciones import (
    ErrorCliente,
    ErrorReserva,
    ErrorOperacion
)
from registros import registrar_evento, registrar_error


clientes = []
reservas = []


def registrar_cliente():
    try:
        print("\n--- REGISTRO DE CLIENTE ---")

        nombre = input("Nombre: ")
        documento = input("Documento: ")
        telefono = input("Teléfono: ")

        for cliente in clientes:
            if cliente.documento == documento:
                raise ErrorCliente("El cliente ya está registrado")

        nuevo_cliente = Cliente(nombre, documento, telefono)
        clientes.append(nuevo_cliente)

        registrar_evento("Cliente registrado: " + documento)
        print("Cliente registrado correctamente.")

    except ErrorCliente as error:
        registrar_error(str(error))
        print("Error:", error)


def listar_clientes():
    print("\n--- LISTA DE CLIENTES ---")

    if not clientes:
        print("No hay clientes registrados.")
        return

    for cliente in clientes:
        print(cliente.mostrar_informacion())


def buscar_cliente():
    documento = input("Ingrese el documento del cliente: ")

    for cliente in clientes:
        if cliente.documento == documento:
            print(cliente.mostrar_informacion())
            return

    print("Cliente no encontrado.")


def listar_servicios():
    print("\n--- SERVICIOS DISPONIBLES ---")

    for numero, servicio in enumerate(servicios_disponibles, 1):
        print(numero, servicio.mostrar_servicio())


def crear_reserva():
    try:
        print("\n--- CREAR RESERVA ---")

        documento = input("Documento del cliente: ")

        cliente_encontrado = None

        for cliente in clientes:
            if cliente.documento == documento:
                cliente_encontrado = cliente
                break

        if cliente_encontrado is None:
            raise ErrorReserva("El cliente no existe")

        listar_servicios()

        opcion = int(input("Seleccione el servicio: "))

        if opcion < 1 or opcion > len(servicios_disponibles):
            raise ErrorReserva("Servicio no válido")

        servicio = servicios_disponibles[opcion - 1]

        nueva_reserva = Reserva(cliente_encontrado, servicio)
        reservas.append(nueva_reserva)

        registrar_evento(
            f"Reserva creada: {nueva_reserva.codigo}"
        )

        print("Reserva creada correctamente.")
        print(nueva_reserva.mostrar_reserva())

    except (ErrorReserva, ValueError) as error:
        registrar_error(str(error))
        print("Error:", error)


def listar_reservas():
    print("\n--- LISTA DE RESERVAS ---")

    if not reservas:
        print("No hay reservas registradas.")
        return

    for reserva in reservas:
        print(reserva.mostrar_reserva())


def buscar_reserva():
    try:
        codigo = int(input("Código de la reserva: "))

        for reserva in reservas:
            if reserva.codigo == codigo:
                print(reserva.mostrar_reserva())
                return

        print("Reserva no encontrada.")

    except ValueError:
        print("Debe ingresar un número válido.")


def cancelar_reserva():
    try:
        codigo = int(input("Código de la reserva: "))

        for reserva in reservas:
            if reserva.codigo == codigo:
                reserva.cancelar()
                registrar_evento(f"Reserva cancelada: {codigo}")
                print("Reserva cancelada correctamente.")
                return

        raise ErrorReserva("Reserva no encontrada")

    except (ValueError, ErrorReserva) as error:
        registrar_error(str(error))
        print("Error:", error)


def completar_reserva():
    try:
        codigo = int(input("Código de la reserva: "))

        for reserva in reservas:
            if reserva.codigo == codigo:
                reserva.completar()
                registrar_evento(f"Reserva completada: {codigo}")
                print("Reserva completada correctamente.")
                return

        raise ErrorReserva("Reserva no encontrada")

    except (ValueError, ErrorReserva) as error:
        registrar_error(str(error))
        print("Error:", error)


def mostrar_estadisticas():
    activas = sum(1 for r in reservas if r.estado == "Activa")
    canceladas = sum(1 for r in reservas if r.estado == "Cancelada")
    completadas = sum(1 for r in reservas if r.estado == "Completada")

    print("\n--- ESTADÍSTICAS DEL SISTEMA ---")
    print("Clientes registrados:", len(clientes))
    print("Total de reservas:", len(reservas))
    print("Reservas activas:", activas)
    print("Reservas canceladas:", canceladas)
    print("Reservas completadas:", completadas)

    registrar_evento("Consulta de estadísticas")


def menu():

    while True:

        print("\n================================")
        print("       SISTEMA SOFTWARE FJ")
        print("================================")
        print("1. Registrar cliente")
        print("2. Listar clientes")
        print("3. Buscar cliente")
        print("4. Mostrar servicios")
        print("5. Crear reserva")
        print("6. Listar reservas")
        print("7. Buscar reserva")
        print("8. Cancelar reserva")
        print("9. Completar reserva")
        print("10. Mostrar estadísticas")
        print("0. Salir")
        print("================================")

        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                registrar_cliente()

            elif opcion == 2:
                listar_clientes()

            elif opcion == 3:
                buscar_cliente()

            elif opcion == 4:
                listar_servicios()

            elif opcion == 5:
                crear_reserva()

            elif opcion == 6:
                listar_reservas()

            elif opcion == 7:
                buscar_reserva()

            elif opcion == 8:
                cancelar_reserva()

            elif opcion == 9:
                completar_reserva()

            elif opcion == 10:
                mostrar_estadisticas()

            elif opcion == 0:
                registrar_evento("Sistema cerrado")
                print("Gracias por utilizar Software FJ.")
                break

            else:
                raise ErrorOperacion("Opción no válida")

        except (ValueError, ErrorOperacion) as error:
            registrar_error(str(error))
            print("Error:", error)


if __name__ == "__main__":
    menu()
