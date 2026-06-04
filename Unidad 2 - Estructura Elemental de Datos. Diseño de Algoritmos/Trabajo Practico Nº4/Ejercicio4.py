# Ejercicio 4 – Control de combustible de vehículos
# Enunciado
# Una empresa de transporte registra el combustible cargado por 10 vehículos.
# Solicitar:
# • Patente
# • Litros cargados
# Mostrar:
# • Total cargado
# • Promedio
# • Vehículo con mayor carga 

n = 10 # Cantidad de Autos Registrados

totalCargado = 0
vehiculoMayorCarga = 0
patenteMayorCarga = ''

for i in range(n):
    
    patente = input("Ingrese su patente: ")
    litrosCargados = float(input("Ingrese los litros cargados: "))
    
    totalCargado = totalCargado + litrosCargados
    
    if litrosCargados > vehiculoMayorCarga:
        vehiculoMayorCarga = litrosCargados
        patenteMayorCarga = patente

promedioCarga = totalCargado / n

print()
print(f"Total de combustible cargado: {totalCargado} Lts")
print(f"Promedio de combustible cargado: {promedioCarga} Lts")
print(f"El vehiculo con patente {patenteMayorCarga} tuvo una mayor carga de combustible y fue de {vehiculoMayorCarga} Lts")
