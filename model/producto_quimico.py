"""Módulo que define la clase ProductoQuimico para el sistema Lavanderia-ExpressClean."""


class ProductoQuimico:
    """Clase que representa un producto químico utilizado en la lavandería."""

    def __init__(self, nombre: str, precio_dolar: float):
        """
        Inicializa un producto químico con su nombre y precio en dólares.

        :param nombre: Nombre del producto químico.
        :param precio_dolar: Precio en dólares (float).
        """
        self.__nombre = None
        self.__precio_dolar = 0.0
        self.nombre = nombre
        self.precio_dolar = precio_dolar

    @property
    def nombre(self) -> str:
        """Obtiene el nombre del producto químico."""
        return self.__nombre

    @nombre.setter
    def nombre(self, valor: str):
        """Establece el nombre del producto químico."""
        self.__nombre = valor

    @property
    def precio_dolar(self) -> float:
        """Obtiene el precio en dólares del producto químico."""
        return self.__precio_dolar

    @precio_dolar.setter
    def precio_dolar(self, valor: float):
        """Establece el precio en dólares del producto químico."""
        self.__precio_dolar = float(valor)

    def calcular_precio_pesos(self, valor_dolar: float) -> float:
        """
        Calcula el precio del producto en pesos chilenos según el valor del dólar.

        :param valor_dolar: Tipo de cambio del dólar en pesos (float).
        :return: Precio en pesos (float).
        """
        return float(self.__precio_dolar * valor_dolar)
