# Ejercicio 6 – Liquidación de haberes
# Una empresa necesita calcular el sueldo final de sus empleados.
# Ingresar:
# • Horas trabajadas
# • Valor por hora
# Utilizar funciones para calcular:
# • Sueldo bruto
# • Descuento jubilatorio (11%)
# • Obra social (3%)
# • Sueldo neto
# Mostrar
# Todos los importes calculados.
# El alumno deberá modularizar el problema utilizando varias funciones.

# Funcion/es

def _sueldoBruto_(__horasTrabajadas, __valorHora):
    __sueldoBruto = __horasTrabajadas * __valorHora
    return __sueldoBruto

def _descuentoJubilatorio_(__sueldo):
    __descuentoJubilatorio = __sueldo * 0.11
    return __descuentoJubilatorio

def _obraSocial_(__sueldo):
    __obraSocial = __sueldo * 0.03  
    return __obraSocial

def _sueldoNeto_(__sueldo, __jubilacion, __obrasocial):
    __sueldoNeto = __sueldo - __jubilacion - __obrasocial  
    return __sueldoNeto

# Programa principal

horasTrabajadas = int(input("Ingrese las horas trabajadas: "))
precioHora = float(input("Ingrese el valor por hora trabajadas: "))

sueldoBruto = _sueldoBruto_(horasTrabajadas, precioHora)
jubilacion = _descuentoJubilatorio_(sueldoBruto)
obraSocial = _obraSocial_(sueldoBruto)
sueldoNeto = _sueldoNeto_(sueldoBruto, jubilacion, obraSocial)

print()
print(f"Sueldo Bruto: ${sueldoBruto}")
print(f"Descuento Jubilatorio: ${jubilacion}")
print(f"Descuento de Obra Social: ${obraSocial}")
print(f"Sueldo Neto/Final: ${sueldoNeto}")