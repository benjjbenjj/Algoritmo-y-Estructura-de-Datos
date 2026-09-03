# Ejercicio 2 – Análisis de calificaciones
# Nivel: Básico
# Un profesor necesita analizar las calificaciones obtenidas por 10 alumnos en un examen.
# Desarrollar un programa que permita ingresar las 10 notas en un arreglo.
# Una vez realizada la carga, recorrer nuevamente el arreglo y determinar:
# 1.	Todas las notas ingresadas.
# 2.	El promedio general.
# 3.	Cantidad de alumnos aprobados, considerando aprobado una nota mayor o igual a 6.
# 4.	Cantidad de alumnos desaprobados.
# 5.	Cantidad de alumnos que obtuvieron una nota superior al promedio general.
# 6.	Porcentaje de alumnos aprobados.


n = 10 # Cantidad de alumnos

notas_alumnos = [] # Lista de las notas de los alumnos

suma_notas = 0 # Para el promedio

alumnos_aprobados = 0
alumnos_desaprobados = 0
alumnos_superiores = 0

for i in range(n): # Registra las notas de los alumnos y los guarda en la lista
    
    nota_registrada = float(input(f"Ingrese la nota del alumno nº{i+1}: "))
    
    suma_notas = suma_notas + nota_registrada
    
    notas_alumnos.append(nota_registrada)

print()
print(f"Notas totales: {notas_alumnos}")
print()

promedio = suma_notas / n

for i in range(n): # Procesamiento de datos
    
    if notas_alumnos[i] >= 6:
        alumnos_aprobados = alumnos_aprobados + 1
            
    elif notas_alumnos[i] < 6:
        alumnos_desaprobados = alumnos_desaprobados + 1
        
    if notas_alumnos[i] > promedio:
        alumnos_superiores = alumnos_superiores + 1
        
porcentaje_aprobados = (alumnos_aprobados / n) * 100

print()
print(f"Promedio de nota: {promedio:.2f}")

print()
print(f"Cantidad de alumnos aprobados: {alumnos_aprobados}")
print()

print()
print(f"Cantidad de alumnos desaprobados: {alumnos_desaprobados}")
print()
 
print()
print(f"Cantidad de alumnos que obtuvieron una nota mayor al promedio general: {alumnos_superiores}")
print() 

print(f"Porcentaje de alumnos aprobados: {porcentaje_aprobados}%")