#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.

    Parámetros:
        radio (float): El radio del círculo.

    Retorna:
        float: El área del círculo.
    """
    area = math.pi * radio ** 2
    return area

# Ejemplo de uso de la función
radio = float(input("Ingresa el radio del círculo: "))
area_del_circulo = calcular_area_circulo(radio)
print("El área del círculo con radio", radio, "es:", area_del_circulo)


# In[ ]:




