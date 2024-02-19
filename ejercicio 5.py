#!/usr/bin/env python
# coding: utf-8

# In[1]:


def fahrenheit_a_celsius(fahrenheit):
    """
    Convierte grados Fahrenheit a grados Celsius.

    Parámetros:
        fahrenheit (float): Los grados Fahrenheit a convertir.

    Retorna:
        float: Los grados Celsius resultantes.
    """
    celsius = (fahrenheit - 32) * (5/9)
    return celsius

fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
celsius = fahrenheit_a_celsius(fahrenheit)
print(f"{fahrenheit} grados Fahrenheit son equivalentes a {celsius} grados Celsius.")


# In[ ]:




