# Ejercicio 9: Promedio entero y promedio real
# Ingresar tres temperaturas y calcular el promedio entero y el promedio real.

temperatura1 = float(input("Ingrese el valor de la temperatura 1:"))
temperatura2 = float(input("Ingrese el valor de la temperatura 2:"))
temperatura3 = float(input("Ingrese el valor de la temperatura 3:"))

promedioReal = (temperatura1 + temperatura2 + temperatura3) / 3
promedioEntero = round(promedioReal)

print("El promedio entero es", promedioEntero, "y el promedio real es", promedioReal)