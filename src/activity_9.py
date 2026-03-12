"""Actividad 9: Bingo de amigos.

Consigna:
Un grupo de cuatro amigos compró un bingo, resultando ganadores del primer
premio por un valor de $ 625.000. Acordaron que la repartición del premio se
hace en forma proporcional al porcentaje de lo aportado por cada uno para
comprar el cartón. Además, decidieron destinar un 2% del monto correspondiente
a cada uno para donación a comedores infantiles.
Dado el premio y el porcentaje del valor del cartón aportado por cada uno,
diseñe un algoritmo que determine el monto que le corresponde a cada amigo
(descontando la donación) y el importe total en donaciones.

Lote de prueba N° 1:
    Entrada:
        Premio: 625000
        Ingrese el porcentaje que aportó cada uno para comprar el cartón:
        Amigo 1: 50
        Amigo 2: 20
        Amigo 3: 15
        Amigo 4: 15

    Salida:
        Monto amigo 1: $ 306250.00
        Monto amigo 2: $ 122500.00
        Monto amigo 3: $ 91875.00
        Monto amigo 4: $ 91875.00
        Total para donaciones: $ 12500.00

Lote de prueba N° 2:
    Entrada:
        Premio: 625000
        Ingrese el porcentaje que aportó cada uno para comprar el cartón:
        Amigo 1: 25
        Amigo 2: 35
        Amigo 3: 17
        Amigo 4: 23

    Salida:
        Monto amigo 1: $ 153125.00
        Monto amigo 2: $ 214375.00
        Monto amigo 3: $ 104125.00
        Monto amigo 4: $ 140875.00
        Total para donación: $ 12500.00

Lote de prueba N° 3:
    Entrada:
        Premio: 625000
        Ingrese el porcentaje aportado por cada uno para comprar el cartón:
        Amigo 1: 17
        Amigo 2: 23
        Amigo 3: 35
        Amigo 4: 25
    Salida:
        Monto amigo 1: $ 104125.00
        Monto amigo 2: $ 140875.00
        Monto amigo 3: $ 214375.00
        Monto amigo 4: $ 153125.00
        Total para donación: $ 12500.00
"""

import logging

logger = logging.getLogger(__name__)

DONATION_PERCENTAGE: float = 0.02


def main() -> None:
    """Main function."""
    prize: float = float(input("Premio: "))
    donation_amount: float = prize * DONATION_PERCENTAGE
    prize -= donation_amount
    logger.info("Ingrese el porcentaje aportado por cada uno para comprar el cartón:")
    first_friend: float = float(input("Amigo 1: ")) / 100
    second_friend: float = float(input("Amigo 2: ")) / 100
    third_friend: float = float(input("Amigo 3: ")) / 100
    fourth_friend: float = float(input("Amigo 4: ")) / 100
    logger.info("Monto amigo 1: $%f", prize * first_friend)
    logger.info("Monto amigo 2: $%f", prize * second_friend)
    logger.info("Monto amigo 3: $%f", prize * third_friend)
    logger.info("Monto amigo 4: $%f", prize * fourth_friend)
    logger.info("Total para donación: $%f", donation_amount)


if __name__ == "__main__":
    logging.basicConfig(format="%(message)s", level=logging.INFO)
    main()
