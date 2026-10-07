"""Módulo que define la clase Operario para el sistema Lavanderia-ExpressClean."""

from model.empleado import Empleado


class Operario(Empleado):
    """Clase que representa un operario en la lavandería."""

    def __init__(self, id_empleado):
        """
        Inicializa un operario con su identificador de empleado.

        :param id_empleado: Identificador del empleado.
        """
        super().__init__(id_empleado)

    def procesar_prenda(self, prenda):
        """
        Procesa una prenda para el lavado (void).

        :param prenda: Instancia de Prenda a procesar.
        """
        pass

    def operar_maquina(self, maquina):
        """
        Opera una máquina iniciando su ciclo de lavado (void).

        :param maquina: Instancia de Maquina a operar.
        """
        if maquina and hasattr(maquina, "iniciar_lavado"):
            maquina.iniciar_lavado()
