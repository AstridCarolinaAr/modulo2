def transponer_con_bucles(matriz):
    """
    Recibe una matriz y devuelve su transpuesta usando bucles for anidados.
    """
    if not matriz:
     num_filas_original = len(matriz)
     num_columnas_original = len(matriz[0])
     matriz_transpuesta = []
    for i in range(num_columnas_original):
        nueva_fila = []
        for j in range(num_filas_original):
            nueva_fila.append(matriz[j][i])
        matriz_transpuesta.append(nueva_fila)
    return matriz_transpuesta