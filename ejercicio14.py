def media_aritmetica(lista):
    """
    Calcula la media aritmética de una lista de números.

    Parámetros:
        lista (list): La lista de números.

    Retorna:
        float: La media aritmética de la lista de números.
    """
    suma_total = sum(lista)
    cantidad_elementos = len(lista)
    if cantidad_elementos > 0:
        return suma_total / cantidad_elementos
    else:
        return 0  # Devolver 0 si la lista está vacía

# Ejemplo de uso de la función
numeros = [4, 6, 8, 10, 12]  # Puedes cambiar esta lista por cualquier otra lista de números
resultado = media_aritmetica(numeros)
print("La media aritmética de la lista es:", resultado)
