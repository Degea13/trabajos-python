def invertir_lista(lista):
    """
    Invierte el orden de los elementos en una lista dada.

    Parámetros:
        lista (list): La lista de elementos a invertir.

    Retorna:
        list: La lista con el orden de sus elementos invertido.
    """
    lista.reverse()
    return lista

# Ejemplo de uso de la función
lista_original = [1, 2, 3, 4, 5]  # Puedes cambiar esta lista por cualquier otra lista de elementos
lista_invertida = invertir_lista(lista_original)
print("La lista original invertida es:", lista_invertida)
