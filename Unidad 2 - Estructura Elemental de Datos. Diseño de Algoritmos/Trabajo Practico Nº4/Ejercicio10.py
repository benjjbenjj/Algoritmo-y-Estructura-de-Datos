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

cantidadAuto = 0
cantidadMoto = 0
cantidadCamion = 0

vehiculoMayor = 0

tipoVehic = input("Ingrese el tipo de vehiculo:\n0 - Para finalizar\n1 - Auto\n2 - Camion\n3 - Moto\n Tipo: ")

while tipoVehic != "0":
    print