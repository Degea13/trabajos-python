# Solicitar al usuario que ingrese dos números
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Calcular la suma, resta, multiplicación y división
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
# Manejar la división por cero
if numero2 != 0:
    division = numero1 / numero2
else:
    division = "No se puede dividir por cero"

# Imprimir los resultados
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
