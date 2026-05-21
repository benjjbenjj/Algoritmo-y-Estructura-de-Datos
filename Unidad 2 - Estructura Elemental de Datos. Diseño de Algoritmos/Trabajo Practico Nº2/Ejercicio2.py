# Ejercicio 2: Sueldo de un empleado
#
# Ingresar el nombre de un empleado, las horas trabajadas y el valor por hora. Calcular
# el sueldo final.

# Ingresamos el nombre del empleado
nombreEmpleado = input("Ingrese su nombre por favor:")

# Solicitamos al empleado las horas que ha trabajado y el valor de cada hora
horasTrabajadas = int(input("Ingrese las horas que ha trabajado:"))
valorHora = float(input("Ingrese el valor de cada hora:"))

# Calculamos el sueldo del empleado
sueldo = horasTrabajadas * valorHora

# Mostramos el sueldo del empleado
print("El sueldo de", nombreEmpleado, "es de $", sueldo)