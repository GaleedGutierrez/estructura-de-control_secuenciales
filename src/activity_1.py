"""Actividad 1: Área de un círculo.

Consigna:
Generar un algoritmo que permita calcular el área de un círculo utilizando la
siguiente fórmula:
area = PI * r2
Siendo PI la constante igual a 3.14159 y r el radio del círculo para el cual se
desea calcular el área.
    1. Crear una variable para guardar el radio ingresado por el usuario utilizando
input() y la conversión a número con int().
    2. Crear una constante para guardar el valor de PI.
    3. Calcular el área del círculo aplicando la fórmula.
    4. Mostrar el resultado del área calculada.

Lote de prueba N° 1:
Entrada:
    PI = 3.1416
    r = 10

Salida:
    Área del círculo = 314.159265359

Lote de prueba N° 2:
Entrada:
    PI = 3.1416
r = 2

Salida:
    Área del circulo = 12.5663706144

    Lote de prueba N° 3:
Entrada:
    PI = 3.1416
    r = 7

Salida:
    Área del circulo = 153.9380400259
"""

import logging
import math

logger = logging.getLogger(__name__)


def area_circle() -> float:
    """Calculate the area of a circle.

    Returns:
        Area of a circle in units squared (u^2).
    """
    radio: float = float(input("Ingrese el radio del círculo: "))
    return math.pi * radio**2


def main() -> None:
    """The main function."""
    logger.info("Área del círculo: %f", area_circle())


if __name__ == "__main__":
    logging.basicConfig(format="%(message)s", level=logging.INFO)
    main()
