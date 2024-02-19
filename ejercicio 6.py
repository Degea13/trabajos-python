#!/usr/bin/env python
# coding: utf-8

# In[1]:


def suma_lista(lista):
    """
    Calcula la suma de los números en una lista dada.

    Parámetros:
        lista (list): La lista de números.

    Retorna:
        float: La suma de los números en la lista.
    """
    suma = 0
    for numero in lista:
        suma += numero
    return suma

# Ejemplo de uso del programa
lista_numeros = [1, 2, 3, 4, 5]  # Puedes cambiar esta lista por cualquier otra lista de números
resultado = suma_lista(lista_numeros)
print("La suma de los números en la lista es:", resultado)


# In[ ]:




