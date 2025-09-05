def generar_reporte(nombres, notas):
    """
    Combina listas de nombres y notas para crear un diccionario
    y luego imprime un reporte de las notas de los estudiantes.
    """
    estudiantes_notas = dict(zip(nombres, notas))

    print("\nReporte de Notas de Estudiantes ")

    for nombre, nota in estudiantes_notas.items():
        print(f"El estudiante {nombre} tiene una nota de {nota}.")

while True:
    try:
        cantidad_estudiantes_str = input("¿Cuántos estudiantes vas a registrar? ")
        cantidad_estudiantes = int(cantidad_estudiantes_str)
        break
    except ValueError:
        print("Error, La cantidad de estudiantes debe ser un número entero. Inténtalo de nuevo.")

nombres_estudiantes = []
notas_finales = []

for i in range(cantidad_estudiantes):
    nombre = input(f"Ingresa el nombre del estudiante {i + 1}: ")
    nombres_estudiantes.append(nombre)
    while True:
        nota_str = input(f"Ingresa la nota de {nombre}: ")
        try:
            nota = float(nota_str)
            notas_finales.append(nota)
            break
        except ValueError:
            print("¡Ups! La nota debe ser un número. Inténtalo de nuevo.")


def main():
    generar_reporte(nombres_estudiantes, notas_finales)


if __name__ == '__main__':
    main()

