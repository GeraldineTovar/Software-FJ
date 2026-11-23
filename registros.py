
import logging

logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)


def registrar_evento(mensaje):
    logging.info(mensaje)


def registrar_error(mensaje):
    logging.error(mensaje)
