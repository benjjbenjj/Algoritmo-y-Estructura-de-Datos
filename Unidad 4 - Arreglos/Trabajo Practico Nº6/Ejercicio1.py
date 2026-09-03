# Ejercicio 1 – Registro de temperaturas
# Nivel: Inicial
# Una estación meteorológica registra la temperatura máxima correspondiente a 7 días consecutivos.
# Desarrollar un programa en Python que permita:
# 1.	Crear un arreglo inicialmente vacío.
# 2.	Ingresar las 7 temperaturas y almacenarlas en el arreglo.
# 3.	Mostrar el arreglo completo.
# 4.	Mostrar cada temperatura indicando el número de día correspondiente.
# 5.	Calcular y mostrar la temperatura promedio de la semana.

temperaturas_max = []

sumaProm = 0

n = 7

for i in range(n):
    
    temperatura_registrada = int(input(f"Ingrese la temperatura registrada del dia {i + 1}: "))
    
    temperaturas_max.append(temperatura_registrada)
    
    sumaProm = sumaProm + temperatura_registrada
    
long_arreglo = len(temperaturas_max)

print(f"Temperaturas Registradas: {temperaturas_max}", end=" ")

for i in range(n):
    
    print()
    print(f"Temperatura del Dia {i + 1}: {temperaturas_max[i]}")
    
promedio = sumaProm / n

print(f"Promedio de temperatura de la semana: {promedio:.2f} ºC")