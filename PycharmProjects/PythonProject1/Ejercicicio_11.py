def validar_cedula(cedula_str):
    """
    Valida una cédula (string) según la regla: la suma de sus dígitos debe ser par.

    Args:
      cedula_str: El número de cédula como una cadena de texto.

    Returns:
      True si la suma de los dígitos es par, False en caso contrario.
    """
    suma_digitos = 0
    for caracter in cedula_str:
        suma_digitos += int(caracter)
    if suma_digitos % 2 == 0:
        return True
    else:
        return False
while True:
    cedula_usuario = input("Por favor, ingresa tu número de cédula: ")
    if validar_cedula(cedula_usuario):
        print("✅ ¡Cédula válida! Gracias.")
        break
    else:
        print("❌ Cédula inválida. La suma de los dígitos debe ser un número par. Inténtalo de nuevo.")