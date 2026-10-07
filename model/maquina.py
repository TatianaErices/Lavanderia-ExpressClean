"""Módulo que define la clase Maquina para el sistema Lavanderia-ExpressClean."""


class Maquina:
    """Clase que representa una máquina de lavado."""

    def __init__(self, id_maquina):
        """
        Inicializa una máquina con su identificador.

        :param id_maquina: Identificador de la máquina.
        """
        self.__id_maquina = id_maquina

    @property
    def id_maquina(self):
        """Obtiene el identificador de la máquina."""
        return self.__id_maquina

    @id_maquina.setter
    def id_maquina(self, valor):
        """Establece el identificador de la máquina."""
        self.__id_maquina = valor

    def iniciar_lavado(self):
        """Inicia el ciclo de lavado de la máquina (void)."""
        pass
