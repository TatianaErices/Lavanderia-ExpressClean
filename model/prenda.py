"""Módulo que define la clase base Prenda para el sistema Lavanderia-ExpressClean."""


class Prenda:
    """Clase base que representa una prenda."""

    def __init__(self, estado_inicial: str, lavado_seco: bool = False):
        """
        Inicializa una prenda asignando mediante sus setters.
        """
        self.__estado_inicial = None
        self.__lavado_seco = False
        self.estado_inicial = estado_inicial
        self.lavado_seco = lavado_seco

    @property
    def estado_inicial(self) -> str:
        """Obtiene el estado inicial de la prenda."""
        return self.__estado_inicial

    @estado_inicial.setter
    def estado_inicial(self, valor: str):
        """Establece el estado inicial de la prenda."""
        self.__estado_inicial = valor

    @property
    def lavado_seco(self) -> bool:
        """Obtiene si la prenda requiere lavado en seco."""
        return self.__lavado_seco

    @lavado_seco.setter
    def lavado_seco(self, valor: bool):
        """Establece si la prenda requiere lavado en seco."""
        self.__lavado_seco = valor

    def validar_estado(self) -> bool:
        """
        Valida el estado inicial de la prenda según las reglas del UML.
        Si self.__lavado_seco es True, retorna True solo si existe un estado inicial no vacío.
        Si no es lavado en seco, retorna True.
        """
        if self.__lavado_seco:
            return bool(self.__estado_inicial and str(self.__estado_inicial).strip())
        return True

    def calcular_costo(self):
        """Método base preparado para ser sobrescrito por los subtipos."""
        raise NotImplementedError("Método preparado para ser sobrescrito por los subtipos.")

    def calcular_tiempo_lavado(self):
        """Método base preparado para ser sobrescrito por los subtipos."""
        raise NotImplementedError("Método preparado para ser sobrescrito por los subtipos.")
