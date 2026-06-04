# Ejercicio 7 – Sistema de calificaciones universitarias

# Enunciado
# Ingresar las notas de alumnos hasta ingresar -1.

# Mostrar:
# • Cantidad de aprobados
# • Cantidad de desaprobados
# • Promedio general
# • Nota más alta

# Condición:
# • Aprueba con nota ≥ 6

# Conceptos aplicados
# • Validaciones
# • Estadísticas
# • Procesamiento masivo 

alumAprob = 0 # Contador de alumnos aprobados
alumDesaprob = 0 # Contador de alumnos desaprobados

cantidadAlumnos = 0 # Contador de notas de alumnos ingresados
sumaNotas = 0 # Sumador de Notas de alumnos

notaAlta = 0 # Guarda la nota más alta

notaAlumno = float(input("Ingrese la nota del alumno (Ingrese -1 para finalizar): "))

while notaAlumno >= 0:
    
    cantidadAlumnos = cantidadAlumnos + 1
    sumaNotas = sumaNotas + notaAlumno
    
    if notaAlumno >= 6:
        alumAprob = alumAprob + 1
    else:
        alumDesaprob = alumDesaprob + 1

    if notaAlumno > notaAlta:
        notaAlta = notaAlumno
    
    notaAlumno = float(input("Ingrese la nota del alumno (Ingrese -1 para finalizar): "))        

if cantidadAlumnos == 0:
    promedioAlum = 0
else:
    promedioAlum = sumaNotas / cantidadAlumnos
    
print()
print(f"Cantidad de alumnos aprobados: {alumAprob}")
print(f"Cantidad de alumnos desaprobados: {alumDesaprob}")
print(f"Promedio general de las notas: {promedioAlum:.2f}")
print(f"Nota mas alta: {notaAlta}")
print()