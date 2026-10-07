"""Módulo que define la clase DetalleOrden para el sistema Lavanderia-ExpressClean."""


class DetalleOrden:
    """Clase que representa el detalle de una orden (asociado a una única prenda)."""

    def __init__(self, prenda):
        """
        Inicializa un detalle de orden con una única prenda.

        :param prenda: Instancia de Prenda asociada.
        """
        self.__prenda = prenda
        self.__subtotal = 0.0
        self.calcular_subtotal()

    @property
    def prenda(self):
        """Obtiene la prenda asociada al detalle."""
        return self.__prenda

    @prenda.setter
    def prenda(self, valor):
        """Establece la prenda asociada y recalcula el subtotal."""
        self.__prenda = valor
        self.calcular_subtotal()

    @property
    def subtotal(self) -> float:
        """Obtiene el subtotal del detalle."""
        return self.__subtotal

    @subtotal.setter
    def subtotal(self, valor: float):
        """Establece manualmente el subtotal del detalle."""
        self.__subtotal = float(valor)

    def calcular_subtotal(self) -> float:
        """
        Calcula el subtotal a partir del costo de la prenda.

        :return: Monto del subtotal como float.
        """
        self.__subtotal = float(self.__prenda.calcular_costo())
        return self.__subtotal
