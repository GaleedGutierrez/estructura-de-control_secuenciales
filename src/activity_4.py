"""Actividad 4: Préstamo de banco.

Consigna:
Una persona desea sacar un préstamo en un banco a devolver en 1 año y quiere
saber cuánto pagará por mes, cuánto pagará de interés en total y cuánto pagará
por el préstamo en total si el banco le cobra una tasa de interés del 9%
mensual. Tener en cuenta que el monto del préstamo debe dividirse en los doce
meses y aplicar la tasa de interés sobre este importe.

1. Crear una variable para guardar el importe del préstamo otorgado por el banco
ingresado por el usuario utilizando input() y la conversión a número con float().
2. Calcular el monto del préstamo mensual sin interés
3. Calcular el interés mensual.
4. Calcular la cuota mensual.
5. Calcular el monto total del interés.
6. Calcular el monto total del préstamo.
7. Mostrar el monto de la cuota mensual, el monto total del interés y el monto
total del préstamo.

Lote de prueba N° 1:
    Entrada:
        Préstamo Bco = 150000

    Salida:
        Cuota Mensual = $ 13625.00
        Total Interés = $ 13500.00
        Total Préstamo = $ 163500.00

Lote de prueba N° 2:
    Entrada:
        Préstamo Bco = 279000

    Salida:
        Cuota Mensual = $ 25342.50
        Total interés = $ 25110.00
        Total préstamo = $ 304110.00

Lote de prueba N° 3:
    Entrada:
        Préstamo Bco = 50000

    Salida:
        Cuota Mensual: $ 4541.67
        Total interés: $ 4500.00
        Total préstamo: $ 54500.00
"""

import logging

logger = logging.getLogger(__name__)

MONTH_INTEREST_RATE: float = 0.09
PERIODS_IN_YEAR: int = 12


def main() -> None:
    """Main function."""
    loan_amount: float = float(
        input("Préstamo Bco = $"),
    )

    twelve_monthly_payment: float = loan_amount / PERIODS_IN_YEAR
    monthly_interest: float = twelve_monthly_payment * MONTH_INTEREST_RATE
    monthly_payment: float = twelve_monthly_payment + monthly_interest
    total_interest: float = monthly_interest * PERIODS_IN_YEAR
    total_loan: float = loan_amount + total_interest

    logger.info("Cuota Mensual = $%.2f", monthly_payment)
    logger.info("Total Interés = $%.2f", total_interest)
    logger.info("Total Préstamo = $%.2f", total_loan)


if __name__ == "__main__":
    logging.basicConfig(format="%(message)s", level=logging.INFO)
    main()
