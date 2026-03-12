"""Actividad 3: Distribución de Presupuesto anual.

Consigna:
Los directivos de un hospital local desean saber rápidamente de qué manera
repartir el presupuesto anual entre las distintas áreas que la  componen.
El hospital se encuentra dividido en cuatro grandes áreas: Urgencias, Guardias,
Pediatría y Traumatología y el presupuesto anual con el que cuentan se reparte
de la siguiente manera:

| Área          | Presupuesto  |
| ------------  | ------------ |
| Urgencias     | 26%          |
| Guardias      | 32%          |
| Pediatría     | 25%          |
| Traumatología | 17%          |

Se solicita generar un algoritmo que permita calcular la cantidad de dinero que
recibirá cada área dependiendo del monto presupuestal ingresado.

    1. Crear una variable para guardar el monto del presupuesto anual ingresado
    por el usuario utilizando input() y la conversión a número con float().
    2. Calcular el dinero destinado a urgencias.
    3. Calcular el dinero destinado a guardias.
    4. Calcular el dinero destinado a pediatría.
    5. Calcular el dinero destinado a traumatología.
    6. Mostrar el dinero destinado a cara área.

Lote de prueba N° 1:
    Entrada:
            Ingresar el monto del presupuesto anual ($): 15350600

    Salida:
            Dinero destinado para Urgencias: $ 3991156.0
            Dinero destinado para Guardias: $ 4912192.0
            Dinero destinado para Pediatría: $ 3837650.0
            Dinero destinado para Traumatología: $ 2609602.0

Lote de prueba N° 2:
    Entrada:
        Ingresar el monto del presupuesto anual ($): 26300830
    Salida:
        Dinero destinado para Urgencias: $ 6838215.8
        Dinero destinado para Guardias: $ 8416265.6
        Dinero destinado para Pediatria: $ 6575207.5
        Dinero destinado para Traumatologia: $ 4471141.10

Lote de prueba N° 3:
    Entrada:
        Ingresar el monto del presupuesto anual ($): 22545890

    Salida:
        Dinero destinado para Urgencias: $ 5861931.4
        Dinero destinado para Guardias: $ 7214684.8
        Dinero destinado para Pediatria: $ 5636472.5
        Dinero destinado para Traumatologia: $ 3832801.30
"""

import logging

logger = logging.getLogger(__name__)


PERCENTAGE_BUDGET: dict[str, float] = {
    "urgency": 0.26,
    "guards": 0.32,
    "pediatrics": 0.25,
    "traumatology": 0.17,
}


def main() -> None:
    """Main function."""
    allocated_budget: float = float(
        input("Ingresar el monto del presupuesto anual ($): "),
    )
    for area, percentage in PERCENTAGE_BUDGET.items():
        logger.info(
            "Dinero destinado para %s: $%.2f",
            area,
            allocated_budget * percentage,
        )


if __name__ == "__main__":
    logging.basicConfig(format="%(message)s", level=logging.INFO)
    main()
