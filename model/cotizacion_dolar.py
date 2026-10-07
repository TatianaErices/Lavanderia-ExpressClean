"""Módulo que define la clase CotizacionDolar para el sistema Lavanderia-ExpressClean."""


class CotizacionDolar:
    """Clase que almacena la cotización del dólar en una fecha determinada."""

    def __init__(self, fecha, valor_dolar: float):
        """
        Inicializa la cotización del dólar con fecha y valor.

        :param fecha: Fecha de la cotización.
        :param valor_dolar: Valor del dólar en pesos (float).
        """
        self.__fecha = None
        self.__valor_dolar = 0.0
        self.fecha = fecha
        self.valor_dolar = valor_dolar

    @property
    def fecha(self):
        """Obtiene la fecha de la cotización."""
        return self.__fecha

    @fecha.setter
    def fecha(self, valor):
        """Establece la fecha de la cotización."""
        self.__fecha = valor

    @property
    def valor_dolar(self) -> float:
        """Obtiene el valor del dólar almacenado."""
        return self.__valor_dolar

    @valor_dolar.setter
    def valor_dolar(self, valor: float):
        """Establece el valor del dólar."""
        self.__valor_dolar = float(valor)

    def obtener_valor_dolar(self) -> float:
        """
        Retorna el valor actual almacenado del dólar.

        :return: Valor del dólar (float).
        """
        return self.__valor_dolar
