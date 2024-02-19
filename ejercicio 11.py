def generar_lista_pares():
    """
    Genera una lista de números pares entre 1 y 100.

    Retorna:
        list: La lista de números pares.
    """
    lista_pares = []
    for numero in range(2, 101, 2):
        lista_pares.append(numero)
    return lista_pares

# Ejemplo de uso del programa
lista_pares = generar_lista_pares()
print("La lista de números pares entre 1 y 100 es:", lista_pares)
