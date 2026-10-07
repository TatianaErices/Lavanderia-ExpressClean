"""Módulo que define la clase base Empleado para el sistema Lavanderia-ExpressClean."""

from abc import ABC


class Empleado(ABC):
    """Clase base abstracta que representa un empleado de la lavandería."""

    def __init__(self, id_empleado):
        """
        Inicializa un empleado con su identificador.

        :param id_empleado: Identificador del empleado.
        """
        self.__id_empleado = id_empleado

    @property
    def id_empleado(self):
        """Obtiene el identificador del empleado."""
        return self.__id_empleado

    @id_empleado.setter
    def id_empleado(self, valor):
        """Establece el identificador del empleado."""
        self.__id_empleado = valor
