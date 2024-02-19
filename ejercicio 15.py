def es_palindromo(cadena):
    """
    Determina si una cadena de texto es un palíndromo o no.

    Parámetros:
        cadena (str): La cadena de texto a verificar.

    Retorna:
        bool: True si la cadena es un palíndromo, False en caso contrario.
    """
    # Convertir la cadena a minúsculas y eliminar los espacios en blanco
    cadena = cadena.lower().replace(" ", "")
    # Verificar si la cadena es igual a su inversa
    return cadena == cadena[::-1]

# Solicitar al usuario que ingrese una cadena de texto
texto = input("Ingrese una cadena de texto: ")

# Determinar si la cadena ingresada es un palíndromo o no
if es_palindromo(texto):
    print("La cadena ingresada es un palíndromo.")
else:
    print("La cadena ingresada no es un palíndromo.")
