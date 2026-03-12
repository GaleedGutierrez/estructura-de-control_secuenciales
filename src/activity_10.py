"""Actividad 10: Superliga.

Consigna:
Elaborar un algoritmo que permita ingresar la cantidad de partidos ganados,
perdidos y empatados, por algún equipo en la Superliga, se debe mostrar su
puntaje total teniendo en cuenta que:
- Por cada partido ganado obtendrá 3 puntos.
- Por cada partido empatado obtendrá 1 punto.
- Por cada partido perdido obtendrá 0 puntos.

Lote de prueba N° 1:
    Entrada:
        Ingresar cantidad de partidos ganados: 5
        Ingresar cantidad de partidos empatados: 8
        Ingresar cantidad de partidos perdidos: 4
    Salida:
        Puntaje Total = 23

Lote de prueba N° 2:
    Entrada:
        Ingresar cantidad de partidos ganados: 12
        Ingresar cantidad de partidos empatados: 6
        Ingresar cantidad de partidos perdidos: 4
    Salida:
        Puntaje Total = 42

Lote de prueba N° 3:
    Entrada:
        Ingresar cantidad de partidos ganados: 10
        Ingresar cantidad de partidos empatados: 4
        Ingresar cantidad de partidos perdidos: 8

    Salida:
        Puntaje Total = 34
"""

import logging

logger = logging.getLogger(__name__)


def main() -> None:
    """Main function."""
    win_matches: int = int(input("Ingresar cantidad de partidos ganados: "))
    draw_matches: int = int(input("Ingresar cantidad de partidos empatados: "))
    lost_matches: int = int(input("Ingresar cantidad de partidos perdidos: "))
    total_points: int = win_matches * 3 + draw_matches + lost_matches * 0
    logger.info("Puntaje Total: %.0f", total_points)


if __name__ == "__main__":
    logging.basicConfig(format="%(message)s", level=logging.INFO)
    main()
