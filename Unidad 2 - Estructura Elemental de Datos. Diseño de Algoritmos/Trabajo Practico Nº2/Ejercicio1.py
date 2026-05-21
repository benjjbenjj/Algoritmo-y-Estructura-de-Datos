# Ejercicio 1: Perímetro de un triángulo
# Ingresar los tres lados de un triángulo y calcular su perímetro.

print("A continuacion ingrese los valores de cada lado del triángulo para calcular su perímetro")

# Pedimos al usuario que ingrese el valor de cada lado del triángulo
lado1 = float(input("Ingrese el lado 1:"))
lado2 = float(input("Ingrese el lado 2:"))
lado3 = float(input("Ingrese el lado 3:"))

# Calculamos el valor del perímetro
perimetro = lado1 + lado2 + lado3

# Mostramos el valor calculado del perímetro del triángulo
print("El perímetro del triángulo es:", perimetro)