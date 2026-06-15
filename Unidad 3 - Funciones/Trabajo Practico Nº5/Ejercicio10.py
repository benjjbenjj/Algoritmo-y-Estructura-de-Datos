# Ejercicio 10 – Sistema Integrador de Operaciones Aeroportuarias
# Durante una jornada operativa se registran movimientos de aeronaves.
# Por cada operación ingresar:
# • Matrícula
# • Tipo de aeronave
# • Cantidad de pasajeros
# • Tiempo de permanencia en plataforma
# Finalizar con matrícula = "FIN".
# Desarrollar funciones que permitan:
# Subproblema 1
# Clasificar la ocupación:
# • Baja (< 50 pasajeros)
# • Media (50 a 150)
# • Alta (>150)
# Subproblema 2
# Determinar la aeronave con mayor permanencia.
# Subproblema 3
# Calcular el promedio de pasajeros por operación.
# Mostrar
# • Total de operaciones
# • Total de pasajeros
# • Promedio general
# • Aeronave con mayor permanencia
# • Cantidad de operaciones bajas
# • Cantidad de operaciones medias
# • Cantidad de operaciones altas

def ocupacion_clasificacion(pasajeros):
    
    if pasajeros < 50:
        clasif = 'Baja'
    elif 50 <= pasajeros <= 150:
        clasif = 'Media'
    elif pasajeros > 150:
        clasif = 'Alta'
    
    return clasif

def aeronave_permanencia(matricula, tiempo, i, mayorPermanencia, matriculaMayorPermanencia, tipo, tipoMayorPermanencia):
    if i == 0 or tiempo > mayorPermanencia:
        mayorPermanencia = tiempo
        matriculaMayorPermanencia = matricula
        tipoMayorPermanencia = tipo
        return mayorPermanencia, matriculaMayorPermanencia, tipoMayorPermanencia
    else:
        return mayorPermanencia, matriculaMayorPermanencia, tipoMayorPermanencia
    
def promedio_pasajeros(operaciones, pasajeros):
    promedio = pasajeros / operaciones
    return promedio

# Programa principal

# Contador de operaciones con ocupacion Baja, Media y
contadorBajas = 0
contadorMedias = 0
contadorAltas = 0

# Se usa para mostrar la cantidad de operaciones, pasajeros y por ultimo para promediar los pasajeros
totalOperaciones = 0
totalPasajeros = 0

# Variables para mostrar las aeronaves con mayor permanencia en la plataforma
mayorPermanencia = 0
matriculaMayorPermanencia = 'Ninguna'
tipoMayorPermanencia = 'Ninguno'

matricula = input("Ingrese la matricula de la aeronave ('FIN' para terminar): ")

if matricula.lower() != 'fin':
    
    while matricula.lower() != 'fin':
        
        tipoAeronave = input("Ingrese el tipo de aeronave: ")
        pasajeros = int(input("Ingrese la cantidad de pasajeros a bordo: "))
        tiempoPermanencia = int(input("Ingrese el tiempo de permanencia de la aeronave (ingrese los minutos / por ejemplo: 2 horas y media = 150 minutos):"))

        ocupacion = ocupacion_clasificacion(pasajeros)
        
        if ocupacion.lower() == 'baja':
            contadorBajas = contadorBajas + 1
        elif ocupacion.lower() == 'media':
            contadorMedias = contadorMedias + 1
        elif ocupacion.lower() == 'alta':
            contadorAltas = contadorAltas + 1
        
        mayorPermanencia, matriculaMayorPermanencia, tipoMayorPermanencia = aeronave_permanencia(matricula, tiempoPermanencia, totalOperaciones, mayorPermanencia, matriculaMayorPermanencia, tipoAeronave, tipoMayorPermanencia)        

        totalPasajeros = totalPasajeros + pasajeros
        totalOperaciones = totalOperaciones + 1

        matricula = input("Ingrese la matricula de la aeronave ('FIN' para terminar): ")
        
    promedio = promedio_pasajeros(totalOperaciones, totalPasajeros)
    
    print()
    print(f"Total de Operaciones Registradas: {totalOperaciones}")
    print(f"Total de Pasajeros: {totalPasajeros}")
    print(f"Promedio de pasajeros: {promedio}")
    print()
    print("----- Aeronave con mayor permanencia -----")
    print(f"Matricula: {matriculaMayorPermanencia}")
    print(f"Tipo de Aeronave: {tipoMayorPermanencia}")
    print(f"Tiempo de Permanencia: {mayorPermanencia}")
    print()
    print("--- Cantidada de Operaciones (Bajas, Medias y Altas) ---")
    print(f"Bajas: {contadorBajas}")
    print(f"Medias: {contadorMedias}")
    print(f"Altas: {contadorAltas}")
    
else:
    print("No se han registrado movimientos de aeronaves.")