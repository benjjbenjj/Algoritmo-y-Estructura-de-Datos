# Ejercicio 3: Promedio de tres notas
# Ingresar tres notas y calcular el promedio.

############# Version 2 #############

# Establecemos la cantidad de notas
cantidadNotas = 3

# Solicitamos al usuario que ingrese las notas
nota1 = float(input("Ingrese el valor de la Nota 1:"))
nota2 = float(input("Ingrese el valor de la Nota 2:"))
nota3 = float(input("Ingrese el valor de la Nota 3:"))

# Agregamos las notas a una variable que las suma
notas = nota1 + nota2 + nota3

# Acá calculamos el promedio y lo ajustamos para que solo muestre un solo decimal
promedio = round(notas / cantidadNotas, 1)

print("El promedio de las notas es", promedio)