# Ejercicio 1 – Control de velocidad vehicular
# Una empresa de transporte realiza controles de velocidad a sus vehículos.
# Se solicita desarrollar un programa que permita ingresar la velocidad registrada de un vehículo y la velocidad
# máxima permitida para la ruta.
# Mediante una función determinar si el conductor circulaba dentro de los límites permitidos.
# Mostrar:
# • Velocidad registrada
# • Velocidad permitida
# • Diferencia entre ambas
# • Mensaje indicando si existe infracción
# El alumno debe identificar
# Datos
# • Velocidad registrada
# • Velocidad máxima
# Condición vinculante
# • Existe infracción si la velocidad registrada supera la permitida.
# Resultados
# • Diferencia
# • Estado de la infracción 

# Funciones 

def diferenciaVeloc(velocidadReg, velocidadPerm):
    diferencia = velocidadPerm - velocidadReg
    return diferencia

def determinarInfraccion(velocidadReg, velocidadPerm):
    if velocidadReg > velocidadPerm:
        estado = "Existe infraccion"
    else:
        estado = "No existe infraccion"
    return estado

# Programa principal

velocidadRegistrada = float(input("Ingrese la velocidad registrada: "))
velocidadPermitida = float(input("Ingrese la velocidad permitida: "))

diferencia = diferenciaVeloc(velocidadRegistrada, velocidadPermitida)
estado = determinarInfraccion(velocidadRegistrada, velocidadPermitida)

print(f"Velocidad Registrada: {velocidadRegistrada} km/h")
print(f"Velocidad Permitida: {velocidadPermitida} km/h")
print(f"Diferencia: {diferencia} km/h")
print(f"Estado: {estado}")