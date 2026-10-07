"""Módulo que define la clase Alfombra para el sistema Lavanderia-ExpressClean."""

from model.prenda import Prenda


class Alfombra(Prenda):
    """Representa una prenda de tipo alfombra en la lavandería."""

    def __init__(self, estado_inicial: str, lavado_seco: bool = False):
        """Inicializa una alfombra."""
        super().__init__(estado_inicial, lavado_seco)

    def calcular_costo(self):
        """Calcula el costo del servicio para alfombras."""
        return 10000

    def calcular_tiempo_lavado(self):
        """Calcula el tiempo de lavado en minutos para alfombras."""
        return 60
