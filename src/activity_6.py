"""Actividad 6: Area y perimetro de un rectángulo.

Consigna:
Generar un algoritmo que determine el área y el perímetro de un rectángulo,
sabiendo que:
area = b x h
perimetro = 2 x (b + h)
Siendo b la base y h la altura.

Lote de prueba N° 1:
    Entrada:
        b = 3
        h = 5

    Salida:
        area = 15
        perimetro = 16

    Lote de prueba N° 2:
    Entrada:
        b = 20
        h = 15

    Salida:
        area = 300
        perimetro = 70

    Lote de prueba N° 3:
    Entrada:
        b = 26
        h = 16

    Salida:
        area = 416
        perimetro = 84
"""

import logging

logger = logging.getLogger(__name__)


def calculate_area(base: float, height: float) -> float:
    """Calculate the area of a rectangle."""
    return base * height


def calculate_perimeter(base: float, height: float) -> float:
    """Calculate the perimeter of a rectangle."""
    return 2 * (base + height)


def main() -> None:
    """Main function."""
    base = float(input("Ingrese la base del rectángulo: "))
    height = float(input("Ingrese la altura del rectángulo: "))
    area = calculate_area(base, height)
    perimeter = calculate_perimeter(base, height)

    logger.info("Área: %f", area)
    logger.info("Perímetro: %f", perimeter)


if __name__ == "__main__":
    logging.basicConfig(format="%(message)s", level=logging.INFO)
    main()
