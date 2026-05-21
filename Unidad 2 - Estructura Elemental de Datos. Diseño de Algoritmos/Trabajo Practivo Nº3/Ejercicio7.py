# • Ejercicio 7: Sistema de becas
# Ingresar:
# • el promedio del alumno,
# • la cantidad de clases a las que asistió,
# • el total de clases dictadas,
# • y si tiene materias desaprobadas.
# El alumno podrá recibir una beca si:
# • su promedio es mayor o igual a 8,
# • su asistencia es mayor o igual al 80% del total de clases,
# • y no tiene materias desaprobadas.
# Mostrar por pantalla:
# • “Beca aprobada” o
# • “Beca rechazada”.

promAlum = float(input("Ingrese el promedio del alumno:"))
clasesAsistidas = int(input("Ingrese el total de clases asistidas por el alumno:"))
clasesTotales = int(input("Ingrese el total de clases realizadas:"))
materiasDesaprobadas = input("Tiene materias desaprobadas? - Responda con Si o No")

# Validamos el porcentaje de asistencia
asistencia = (clasesAsistidas / clasesTotales) * 100

if promAlum > 8 and asistencia >= 80 and str.lower(materiasDesaprobadas) == "no":
    print("Beca Aprobada!")
    
else:
    print("Beca Rechazada")