#!/usr/bin/env python
# coding: utf-8

# In[1]:


def determinar_paridad(numero):
    """
    Determina si un número dado es par o impar.

    Parámetros:
        numero (int): El número a verificar.

    Retorna:
        str: "par" si el número es par, "impar" si el número es impar.
    """
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

# Ejemplo de uso del programa
numero = int(input("Por favor, ingresa un número: "))
resultado = determinar_paridad(numero)
print("El número", numero, "es", resultado)


# In[ ]:




