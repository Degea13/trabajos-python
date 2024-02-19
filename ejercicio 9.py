def imprimir_matriz(matriz):
    """
    Imprime una matriz en pantalla.

    Parámetros:
        matriz (list): La matriz a imprimir.
    """
    for fila in matriz:
        for elemento in fila:
            print(elemento, end=" ")
        print()  # Salto de línea al terminar de imprimir cada fila


def generar_matriz(filas, columnas):
    """
    Genera una matriz de números.

    Parámetros:
        filas (int): El número de filas de la matriz.
        columnas (int): El número de columnas de la matriz.

    Retorna:
        list: La matriz de números.
    """
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            # Aquí puedes generar los números de la matriz como desees, por ejemplo, de forma aleatoria
            fila.append(i * j)  # En este ejemplo, se asigna el producto de los índices como valor
        matriz.append(fila)
    return matriz


# Ejemplo de uso del programa
filas = int(input("Ingrese el número de filas de la matriz: "))
columnas = int(input("Ingrese el número de columnas de la matriz: "))

mi_matriz = generar_matriz(filas, columnas)
print("La matriz generada es:")
imprimir_matriz(mi_matriz)
