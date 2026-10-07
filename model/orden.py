"""Módulo que define la clase Orden para el sistema Lavanderia-ExpressClean."""

from model.detalle_orden import DetalleOrden
from model.excepciones import OrdenNoPagadaError


class Orden:
    """Clase que representa una orden de lavandería."""

    def __init__(self, num_orden: int, num_boleta: str = "", pagada: bool = False):
        """
        Inicializa una orden de servicio.

        :param num_orden: Identificador interno de la orden (int).
        :param num_boleta: Número de boleta de la orden (str).
        :param pagada: Estado de pago de la orden (bool, por defecto False).
        """
        self.__num_orden = num_orden
        self.__num_boleta = num_boleta
        self.__pagada = pagada
        self.__detalles = []

    @property
    def num_orden(self) -> int:
        """Obtiene el número interno de la orden."""
        return self.__num_orden

    @num_orden.setter
    def num_orden(self, valor: int):
        """Establece el número interno de la orden."""
        self.__num_orden = valor

    @property
    def num_boleta(self) -> str:
        """Obtiene el número de boleta."""
        return self.__num_boleta

    @num_boleta.setter
    def num_boleta(self, valor: str):
        """Establece el número de boleta."""
        self.__num_boleta = valor

    @property
    def pagada(self) -> bool:
        """Indica si la orden se encuentra pagada."""
        return self.__pagada

    @pagada.setter
    def pagada(self, valor: bool):
        """Establece el estado de pago de la orden."""
        self.__pagada = bool(valor)

    @property
    def detalles(self) -> list:
        """Obtiene la lista interna de detalles."""
        return self.__detalles

    def agregar_detalle(self, prenda) -> DetalleOrden:
        """
        Crea un DetalleOrden para la prenda y lo agrega a la orden (composición).

        :param prenda: Instancia de Prenda a agregar.
        :return: El objeto DetalleOrden creado.
        """
        detalle = DetalleOrden(prenda)
        self.__detalles.append(detalle)
        return detalle

    def validar_identificacion(self) -> bool:
        """
        Valida que num_boleta esté registrada y no esté vacía.

        :return: True si num_boleta tiene contenido válido, False en caso contrario.
        """
        return bool(self.__num_boleta and str(self.__num_boleta).strip())

    def calcular_total(self) -> float:
        """
        Calcula el total de la orden sumando los subtotales de sus detalles.

        :return: Total acumulado como float.
        """
        return float(sum(detalle.calcular_subtotal() for detalle in self.__detalles))

    def verificar_pago(self) -> bool:
        """
        Verifica si la orden se encuentra pagada.

        :return: True si pagada es True, False en caso contrario.
        """
        return bool(self.__pagada)

    def entregar_orden(self) -> bool:
        """
        Gestiona la entrega de la orden comprobando que esté pagada.

        :return: True si está pagada.
        :raises OrdenNoPagadaError: Si la orden no se encuentra pagada.
        """
        if not self.verificar_pago():
            raise OrdenNoPagadaError("La orden no puede entregarse porque no está pagada.")
        return True
