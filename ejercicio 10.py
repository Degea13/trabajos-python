def factorial(numero):
    """
    Calcula el factorial de un número dado.

    Parámetros:
        numero (int): El número del cual se calculará el factorial.

    Retorna:
        int: El factorial del número dado.
    """
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

# Ejemplo de uso de la función
numero = int(input("Ingrese un número para calcular su factorial: "))
resultado_factorial = factorial(numero)
print(f"El factorial de {numero} es: {resultado_factorial}")
def factorial(numero):
    """
    Calcula el factorial de un número dado.

    Parámetros:
        numero (int): El número del cual se calculará el factorial.

    Retorna:
        int: El factorial del número dado.
    """
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

# Ejemplo de uso de la función
numero = int(input("Ingrese un número para calcular su factorial: "))
resultado_factorial = factorial(numero)
print(f"El factorial de {numero} es: {resultado_factorial}")
