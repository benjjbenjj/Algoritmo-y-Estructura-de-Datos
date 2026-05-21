# Ejercicio 2: Evaluación de alumno
#
# Ingresar:
# • la nota final de un alumno,
# • la cantidad de clases a las que asistió,
# • y el total de clases dictadas.
# El alumno aprueba si:
# • obtiene una nota mayor o igual a 6,
# • y su asistencia es al menos del 75% del total de clases.
# Mostrar por pantalla si el alumno:
# • APRUEBA o
# • NO APRUEBA.

# Ingresamos los datos del alumno
notaFinal = float(input("Ingrese la nota final del alumno:"))
clasesTotales = int(input("Ingrese el total de clases:"))
clasesAsistidas = int(input("Ingrese el total de clases asistidas por el alumno:"))

# Calculo el porcentaje de asistencia
asistenciaPorcentaje = (clasesAsistidas / clasesTotales) * 100

if notaFinal >= 6 and asistenciaPorcentaje >= 75:
    print("APRUEBA")
else:
    print("NO APRUEBA")