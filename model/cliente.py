"""Módulo que define la clase Cliente para el sistema Lavanderia-ExpressClean."""

import re


class Cliente:
    """Clase que representa un cliente en el sistema de lavandería."""

    def __init__(self, rut: str):
        """
        Inicializa un cliente asignando su RUT mediante el setter.

        :param rut: RUT del cliente (ej. '12.345.678-5' o '12345678-5').
        """
        self.__rut = None
        self.rut = rut

    @property
    def rut(self) -> str:
        """Obtiene el RUT del cliente."""
        return self.__rut

    @rut.setter
    def rut(self, valor: str):
        """
        Establece y valida el RUT del cliente.
        Lanza ValueError si el RUT no tiene formato válido o dígito verificador correcto.
        """
        anterior = self.__rut
        self.__rut = valor
        if not self.validar_rut():
            self.__rut = anterior
            raise ValueError(
                f"RUT inválido: '{valor}'. Debe tener formato válido y dígito verificador correcto."
            )

    def validar_rut(self) -> bool:
        """
        Valida que el RUT actual tenga formato válido y dígito verificador correcto (Módulo 11).

        :return: True si el RUT es válido, False en caso contrario.
        """
        if not self.__rut or not isinstance(self.__rut, str):
            return False

        valor = self.__rut.strip()
        patron = r"^(?:\d{1,2}(?:\.\d{3}){2}-[\dkK]|\d{7,8}-[\dkK]|\d{7,8}[\dkK])$"
        if not re.match(patron, valor):
            return False

        rut_limpio = valor.replace(".", "").replace("-", "").upper()
        cuerpo = rut_limpio[:-1]
        dv = rut_limpio[-1]

        if not cuerpo.isdigit():
            return False

        # Algoritmo Módulo 11
        multiplicadores = [2, 3, 4, 5, 6, 7]
        suma = sum(
            int(digito) * multiplicadores[i % 6]
            for i, digito in enumerate(reversed(cuerpo))
        )
        resto = suma % 11
        resultado = 11 - resto

        if resultado == 11:
            dv_esperado = "0"
        elif resultado == 10:
            dv_esperado = "K"
        else:
            dv_esperado = str(resultado)

        return dv == dv_esperado
