# Ejercicio 10 – Sistema inteligente de peaje (Nivel Avanzado)

# Enunciado
# Un peaje registra vehículos durante el día.

# Solicitar:
# • Tipo de vehículo
# o 1 = Auto
# o 2 = Camión
# o 3 = Moto
# • Importe abonado
# Finalizar cuando el importe sea 0.

# Mostrar:
# • Total recaudado
# • Cantidad de vehículos por tipo
# • Promedio recaudado
# • Vehículo que más pagó
# • Porcentaje de camiones 

totalRecaudado = 0
contadorVehic = 0

cantidadAuto = 0
cantidadMoto = 0
cantidadCamion = 0

vehiculoMayor = 0
tipoVehiculoMayor = "Ninguno"

importeVehiculo = 1 # Habilita la entrada al While

while importeVehiculo != 0:
    
    tipoVehic = input("Ingrese el tipo de vehiculo:\n0 - Para finalizar\n1 - Auto\n2 - Camion\n3 - Moto\n Tipo: ")
    
    if tipoVehic == "1" or tipoVehic == "2" or tipoVehic == "3":
        
        importeVehiculo = int(input("Ingrese el importe a pagar (0 Para finalizar): "))
        
        if importeVehiculo != 0:
            
            contadorVehic = contadorVehic + 1
            
            if tipoVehic == "1":
                cantidadAuto =cantidadAuto + 1
                nombreVehiculo = 'Auto'
            elif tipoVehic == "2":
                cantidadCamion = cantidadCamion + 1
                nombreVehiculo = 'Camion'
            elif tipoVehic == "3":
                cantidadMoto = cantidadMoto + 1
                nombreVehiculo = 'Moto'
            
            if contadorVehic == 1 or importeVehiculo > vehiculoMayor:
                vehiculoMayor = importeVehiculo
                tipoVehiculoMayor = nombreVehiculo

            totalRecaudado = totalRecaudado + importeVehiculo
        
    elif tipoVehic == "0":
        importeVehiculo = 0
    else:
        print("ALERTA! - Ingrese un tipo de vehículo válido\n")

# Fin del bucle

if(contadorVehic == 0):
    promedioRecaudado = 0
else:
    promedioRecaudado = totalRecaudado / contadorVehic
    
if(contadorVehic == 0):
    porcentajeCamiones = 0
else:
    porcentajeCamiones = (cantidadCamion / contadorVehic) * 100

print()
print(f"Total Recaudado: ${totalRecaudado}")
print(f"Cantidad de vehiculos por tipo: \n Autos: {cantidadAuto}\nCamiones: {cantidadCamion} \nMotos: {cantidadMoto}")
print(f"Promedio recaudado: ${promedioRecaudado:.2f}")
print(f"Vehiculo que mas pago:\nTipo: {tipoVehiculoMayor}\nMonto Abonado: ${vehiculoMayor}")
print(f"Porcentaje de Camiones: {porcentajeCamiones}%")
print()