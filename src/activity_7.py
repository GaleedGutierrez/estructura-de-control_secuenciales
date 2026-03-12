"""Actividad 7: Calificación final de alumno.

Consigna:
Generar un algoritmo que permita calcular la calificación final de un alumno en
la materia de Algoritmos. Dicha calificación se compone de tres exámenes
parciales. Al final se deberá mostrar nombre y apellido del alumno, la
cantidad de notas procesadas y la calificación final.

Lote de prueba N° 1:
    Entrada:
        Nombre: Luis
        Apellido: Diaz
        Primer parcial: 5
        Segundo parcial: 6
        Tercer parcial: 4

    Salida:
        Cantidad de notas: 3
        La calificación final de Luis Diaz es: 5.0

Lote de prueba N° 2:
    Entrada:
        Nombre: Ornela
        Apellido: Santos
        Primer parcial: 8
        Segundo parcial: 6.5
        Tercer parcial: 7

    Salida:
        Cantidad de notas: 3
        La calificación final de Ornela Santos es: 7.17

Lote de prueba N° 3:
    Entrada:
        Nombre: Maria
        Apellido: Perez
        Primer parcial: 10
        Segundo parcial: 7
        Tercer parcial: 8.5

    Salida:
        Cantidad de notas: 3
        La calificación final de Ornela Santos es: 8.5
"""

import logging

logger = logging.getLogger(__name__)


def main() -> None:
    """Main function."""
    student: dict[str, str | dict[str, float]] = {
        "name": input("Nombre: "),
        "last_name": input("Apellido: "),
    }
    exams: dict[str, float] = {
        "first_exam": float(input("Primer parcial: ")),
        "second_exam": float(input("Segundo parcial: ")),
        "third_exam": float(input("Tercer parcial: ")),
    }
    student["exams"] = exams

    logger.info("Cantidad de notas: %d", len(student["exams"]))
    average_grade = sum(student["exams"].values()) / len(student["exams"])
    logger.info(
        "La calificación final de %s %s es: %.2f",
        student["name"],
        student["last_name"],
        average_grade,
    )


if __name__ == "__main__":
    logging.basicConfig(format="%(message)s", level=logging.INFO)
    main()
