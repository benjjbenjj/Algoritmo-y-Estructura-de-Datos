# Ejercicio 1 – Control de acceso a un edificio
# Enunciado
# Una empresa desea registrar el ingreso de empleados durante 5 turnos.
# Solicitar:
# • Nombre del empleado
# • Hora de ingreso
# Mostrar todos los ingresos registrados.

print("-- Control de Acceso al Edificio --")
print()

for i in range(5):
    
    print(f"Empleado numero {i+1}")
    
    nombre = input("Ingrese su nombre: ")
    hora = input("Ingrese el horario de ingreso (HH:MM): ")
    
    print(f"El empleado {nombre} ingresó a las horas {hora}")
    
print()