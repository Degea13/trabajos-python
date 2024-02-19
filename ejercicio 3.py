#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

def generar_lista_numeros_aleatorios(longitud, limite_inferior, limite_superior):
    """
    Genera una lista de números aleatorios.

    Parámetros:
        longitud (int): La longitud de la lista.
        limite_inferior (int): El límite inferior para generar números aleatorios.
        limite_superior (int): El límite superior para generar números aleatorios.

    Retorna:
        list: La lista de números aleatorios.
    """
    lista_numeros_aleatorios = [random.randint(limite_inferior, limite_superior) for _ in range(longitud)]
    return lista_numeros_aleatorios

# Ejemplo de uso de la función
longitud_lista = int(input("Ingrese la longitud de la lista de números aleatorios: "))
limite_inferior = int(input("Ingrese el límite inferior para generar números aleatorios: "))
limite_superior = int(input("Ingrese el límite superior para generar números aleatorios: "))

lista_aleatoria = generar_lista_numeros_aleatorios(longitud_lista, limite_inferior, limite_superior)
print("La lista de números aleatorios es:", lista_aleatoria)


# In[ ]:




