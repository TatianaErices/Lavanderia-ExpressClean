"""Módulo que define la clase Cajero para el sistema Lavanderia-ExpressClean."""

from model.empleado import Empleado


class Cajero(Empleado):
    """Clase que representa un cajero en la lavandería."""

    def __init__(self, id_empleado):
        """
        Inicializa un cajero con su identificador de empleado.

        :param id_empleado: Identificador del empleado.
        """
        super().__init__(id_empleado)

    def recibir_prendas(self):
        """Recibe las prendas del cliente para el servicio (void)."""
        pass

    def registrar_orden(self):
        """Registra una nueva orden en el sistema (void)."""
        pass

    def cobrar_orden(self):
        """Gestiona el cobro de una orden (void)."""
        pass

    def entregar_prendas(self) -> bool:
        """
        Entrega las prendas al cliente (Boolean).

        :return: True indicando la entrega.
        """
        return True
