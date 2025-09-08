def definir_precio(edad):
    """
    Esta función define el precio de la boleta, validando la entrada de la edad.

    :param edad: recibe la edad del usuario (puede ser un string).
    :return: retorna el precio si la edad es válida.
    :raises ValueError: si la edad no es un número entero positivo.
    """
    try:
        # Se verifica si la edad es un número de tipo float
        if isinstance(edad, float):
            # Se convierte a un string para ver si tiene decimales.
            if str(edad).endswith('.0'):
                edad_num = int(edad)
            else:
                # Si tiene decimales, lanza un ValueError.
                raise ValueError("La edad debe ser un número entero.")
        else:
            # Si no es un float, se intenta convertir a entero.
            edad_num = int(edad)
    except (ValueError, TypeError):
        # Si la entrada no puede ser convertida a un número entero
        # (por ejemplo, es texto o está vacía), se lanza el error.
        raise ValueError("La edad debe ser un número entero.")

    # 2. Validar si el número es positivo
    # Se corrige la condición para que incluya el 0 como edad válida de niño
    if edad_num < 0:
        raise ValueError("La edad debe ser un número entero positivo.")

    # 3. Validar los límites de edad
    if 0 <= edad_num <= 12:
        precio = 10000
    elif 12 < edad_num <= 18:
        precio = 15000
    else:
        precio = 20000

    return precio


def definir_descuento(es_estudiante, precio):
    """
    define si la persona tiene o no descuento
    :param es_estudiante:recibe si es estudiante o no
    :param precio: guarda el precio de la boleta dependiendo la edad
    """

    if es_estudiante == 1:
        descuento = precio * 0.1
        precio_total = precio - descuento
        print(f"El costo de tu entrada es de ${precio},")
        print(f"con el descuento de estudiante queda en ${precio_total}.")
    elif es_estudiante == 0:
        print(f"El costo de tu entrada es de ${precio}.")
        print("Ten en cuenta que no se aplicó el descuento de estudiante.")
    else:
        raise ValueError("La opcion debe ser numero 1 o 0.")
def main():
    """
    depura el codigo
    """
    while True:
        edad_str = input("Escribe en números ¿cuál es tu edad? ")
        try:
            edad = float(edad_str)
            precio = definir_precio(edad)
            while True:
                if precio is not None:
                    es_estudiante_str = input("Escribe el número 1 si eres estudiante\nescribe el número 0 si no eres estudiante:\n")
                    try:
                        es_estudiante = int(es_estudiante_str)
                        definir_descuento(es_estudiante, precio)
                    except ValueError:
                        raise ValueError("La opcion debe ser numero 1 o 0.")
        except ValueError:
            raise ValueError("La opcion debe ser numero 1 o 0.")

if __name__ == "__main__":
    main()