"""Módulo que define la clase RopaNormal para el sistema Lavanderia-ExpressClean."""

from model.prenda import Prenda


class RopaNormal(Prenda):
    """Representa una prenda de tipo ropa normal en la lavandería."""

    def __init__(self, estado_inicial: str, lavado_seco: bool = False):
        """Inicializa una prenda de ropa normal."""
        super().__init__(estado_inicial, lavado_seco)

    def calcular_costo(self):
        """Calcula el costo del servicio para ropa normal."""
        return 5000

    def calcular_tiempo_lavado(self):
        """Calcula el tiempo de lavado en minutos para ropa normal."""
        return 30
