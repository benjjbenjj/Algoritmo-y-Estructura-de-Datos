# Ejercicio 3: Promedio de tres notas
# Ingresar tres notas y calcular el promedio.

############# Version 2 #############

# Solicitamos al usuario que ingrese las notas
nota1 = float(input("Ingrese el valor de la Nota 1:"))
nota2 = float(input("Ingrese el valor de la Nota 2:"))
nota3 = float(input("Ingrese el valor de la Nota 3:"))

# Calculamos el promedio de las notas
notas = nota1 + nota2 + nota3
promedio = notas / 3

print("El promedio de las notas es", promedio)