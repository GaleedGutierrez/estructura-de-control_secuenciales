"""Actividad 8: Conversión de unidades de medida.

Consigna:
Generar un algoritmo para desplegar el peso dado en kilos de una persona en
gramos, libras y toneladas. Teniendo en cuenta que:
1 Kg equivale a 1000 g
1 Kg equivale a 2.20462 lb
1 Kg equivale a 0.001 t

Lote de prueba N° 1:
    Entrada:
        Ingrese su peso en kilos: 96.8

    Salida:
        96.8 Kg equivalen a:
        ->  96800.0 gramos
        ->  212.96 libras
        ->  0.0968 toneladas

Lote de prueba N° 2:
    Entrada:
    Ingrese su peso en kilos: 63

Salida:
    63.0 Kg equivalen a:
    ->  63000.0 gramos
    ->  138.60 libras
    ->  0.063 toneladas

Lote de prueba N° 3:
    Entrada:
    Ingrese su peso en kilos: 1563.5

Salida:
    1563.5 Kg equivalen a:
    ->  1563500.0 gramos
    ->  3439.7000000000003 libras
    ->  1.5635000000000001 toneladas
"""

import logging

logger = logging.getLogger(__name__)

GRAMS_IN_KILOS: int = 1000
POUNDS_IN_KILOS: float = 2.20462
TONS_IN_KILOS: float = 0.001


def main() -> None:
    """Main function."""
    weight_in_kilos: float = float(
        input("Ingrese su peso en kilos: "),
    )
    weight_in_grams = weight_in_kilos * GRAMS_IN_KILOS
    weight_in_pounds = weight_in_kilos * POUNDS_IN_KILOS
    weight_in_tons = weight_in_kilos * TONS_IN_KILOS
    logger.info("%fKG equivalen a:", weight_in_kilos)
    logger.info("-> %f gramos", weight_in_grams)
    logger.info("-> %f libras", weight_in_pounds)
    logger.info("-> %f toneladas", weight_in_tons)


if __name__ == "__main__":
    logging.basicConfig(format="%(message)s", level=logging.INFO)
    main()
