"""Actividad 2: Descomposición de un número natural en forma aditiva.

Consigna:
Generar un algoritmo que permita cargar tres números enteros de una cifra en
tres variables distintas para formar un único número natural de tres cifras
donde la centena será ocupada por el primer número ingresado, la decena por el
segundo número ingresado y la unidad por el tercer número ingresado Por ejemplo
si las cifras ingresadas son a=5, b=6 y c=2, entonces el número resultante será
x=562. Mostrar cada valor posicional y el número final.

Crear tres variables para guardar tres números de una cifra ingresados por el
usuario utilizando input() y la conversión a número con int().
    1. Calcular el valor posicional de las centenas
    2. Calcular el valor posicional de las decenas
    3. Calcular el valor posicional de las unidades.
    4. Calcular el número resultante de tres cifras.
    5. Mostrar los valores posicionales de cada número.
    6. Mostrar el número de tres cifras formado.

Lote de prueba N° 1:
Entrada:
        Ingrese un número de una cifra: 5
        Ingrese otro número de una cifra: 6
        Ingrese otro número de una cifra: 2
Salida:
        Valores posicionales
        Centenas: 500
        Decenas: 60
        Unidades: 2
        Número formado: 562

Lote de prueba N° 2:
Entrada:
        Ingrese un número de una cifra: 0
        Ingrese otro número de una cifra: 6
        Ingrese otro número de una cifra: 4
Salida:
        Valores posicionales
        Centenas: 0
        Decenas: 60
        Unidades: 4
        Número formado: 64
"""

import logging

logger = logging.getLogger(__name__)


def decompose() -> dict[str, int]:
    """Decomposition of a natural number into additive form."""
    hundreds: int = int(input("Ingrese un número de una cifra: "))
    tens: int = int(input("Ingrese otro número de una cifra: "))
    units: int = int(input("Ingrese otro número de una cifra: "))

    return {
        "hundreds": hundreds * 100,
        "tens": tens * 10,
        "units": units,
    }


def main() -> None:
    """Main function."""
    decomposition: dict[str, int] = decompose()
    logger.info("Valores posicionales")
    logger.info("Centenas: %d", decomposition["hundreds"])
    logger.info("Decenas: %d", decomposition["tens"])
    logger.info("Unidades: %d", decomposition["units"])
    logger.info("Número formado: %d", sum(decomposition.values()))


if __name__ == "__main__":
    logging.basicConfig(format="%(message)s", level=logging.INFO)
    main()
