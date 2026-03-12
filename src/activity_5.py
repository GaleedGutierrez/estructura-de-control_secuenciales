"""Actividad 5: Promedio de lluvias.

Consigna:
Generar un algoritmo que permita calcular el promedio de lluvias, en mililitros,
registrado en la zona para un trimestre dado. Para ello se debe suministrar
como datos de entrada los nombres de los tres meses y la cantidad de lluvia
en mililitros registrado para cada uno. Antes de finalizar mostrar los nombres
de los meses junto con la cantidad de lluvia registrada para cada uno y el
promedio de lluvia calculado para el trimestre.


1. Crear tres variables para guardar el nombre de los tres meses ingresados por
el usuario utilizando input().
2. Crear tres variables para guardar la cantidad de lluvia registrada en cada
mes ingresada por el usuario utilizando input() y la conversión a número con float().
3. Calcular el promedio de lluvia registrada en los tres meses
4. Mostrar los nombres de los meses junto con la cantidad de lluvia registrada
para cada uno y el promedio de lluvia calculado para el trimestre.

Lote de prueba N° 1:
    Entrada:
        Ingrese el nombre del primer mes: Marzo
        Ingrese la cantidad de lluvia registrada en Marzo (ml): 32

        Ingrese el nombre del segundo mes: Abril
        Ingrese la cantidad de lluvia registrada en Abril (ml): 50

        Ingrese el nombre del tercer mes: Mayo
        Ingrese la cantidad de lluvia registrada en Mayo (ml): 45

    Salida:
        Resumen del Trimestre
        Marzo - Cantidad llovida: 32 ml
        Abril - Cantidad llovida: 50 ml
        Mayo - Cantidad llovida: 45 ml
        Promedio de lluvia del trimestre: 42.3333333333 ml

Lote de prueba N° 2:
    Entrada:
        Ingrese el nombre del primer mes: Junio
        Ingrese la cantidad de lluvia registrada en Junio (ml): 66

        Ingrese el nombre del segundo mes: Julio
        Ingrese la cantidad de lluvia registrada en Julio (ml): 34

        Ingrese el nombre del tercer mes: Agosto
        Ingrese la cantidad de lluvia registrada en Agosto (ml): 37

    Salida:
        Resumen del trimestre
        Junio - Cantidad llovida: 66 ml
        Julio - Cantidad llovida: 34 ml
        Agosto - Cantidad llovida: 37 ml
        Promedio de lluvia del trimestre: 45.6666666667 ml

Lote de prueba N° 3:
    Entrada:
            Ingrese el nombre del primer mes: Septiembre
            Ingrese la cantidad de lluvia registrada en Septiembre (ml): 22

            Ingrese el nombre del segundo mes: Octubre
            Ingrese la cantidad de lluvia registrada en Octubre (ml): 29

            Ingrese el nombre del tercer mes: Noviembre
            Ingrese la cantidad de lluvia registrada en Noviembre (ml): 31

    Salida:
            Resumen del trimestre
            Septiembre - Cantidad llovida: 22 ml
            Octubre - Cantidad llovida: 29 ml
            Noviembre - Cantidad llovida: 31 ml
            Promedio de lluvia del trimestre: 27.3333333333 ml
"""

import logging

logger = logging.getLogger(__name__)

MOUNT_MONTHS: int = 3


def main() -> None:
    """Main function."""
    rains: dict[str, float] = {}

    for i in range(MOUNT_MONTHS):
        month: str = ""
        match i:
            case 0:
                month = input("Ingrese el nombre del primer mes: ")
            case 1:
                month = input("Ingrese el nombre del segundo mes: ")
            case _:
                month = input("Ingrese el nombre del tercer mes: ")

        rain_amount: float = float(
            input(f"Ingrese la cantidad de lluvia registrada en {month} (ml): "),
        )
        rains[month] = rain_amount

    average_rain: float = sum(rains.values()) / MOUNT_MONTHS

    logger.info("Resumen del trimestre")

    for month, rain_amount in rains.items():
        logger.info("%s - Cantidad llovida: %f ml", month, rain_amount)

    logger.info("Promedio de lluvia del trimestre: %f ml", average_rain)


if __name__ == "__main__":
    logging.basicConfig(format="%(message)s", level=logging.INFO)
    main()
