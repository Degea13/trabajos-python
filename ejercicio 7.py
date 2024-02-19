def encontrar_maximo_minimo(lista):
    """
    Encuentra el número más grande y el más pequeño en una lista dada.

    Parámetros:
        lista (list): La lista de números.

    Retorna:
        tuple: Una tupla que contiene el número más grande y el más pequeño.
    """
    maximo = max(lista)
    minimo = min(lista)
    return maximo, minimo

# Ejemplo de uso del programa
lista_numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]  # Puedes cambiar esta lista por cualquier otra lista de números
numero_maximo, numero_minimo = encontrar_maximo_minimo(lista_numeros)
print("El número más grande en la lista es:", numero_maximo)
print("El número más pequeño en la lista es:", numero_minimo)
