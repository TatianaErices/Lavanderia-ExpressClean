"""Módulo que define la clase EdredonCobertor para el sistema Lavanderia-ExpressClean."""

from model.prenda import Prenda


class EdredonCobertor(Prenda):
    """Representa una prenda de tipo edredón o cobertor en la lavandería."""

    def __init__(self, estado_inicial: str, lavado_seco: bool = False):
        """Inicializa un edredón o cobertor."""
        super().__init__(estado_inicial, lavado_seco)

    def calcular_costo(self):
        """Calcula el costo del servicio para edredones y cobertores."""
        return 12000

    def calcular_tiempo_lavado(self):
        """Calcula el tiempo de lavado en minutos para edredones y cobertores."""
        return 90
