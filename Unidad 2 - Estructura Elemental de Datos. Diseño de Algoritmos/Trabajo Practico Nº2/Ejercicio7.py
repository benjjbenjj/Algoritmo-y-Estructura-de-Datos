# Ejercicio 7: Cálculo de combustible consumido
# Un vehículo recorrió cierta cantidad de kilómetros y consumió una cantidad
# determinada de litros. Calcular el consumo por kilómetro.

# Solititamos al usuario que ingrese la cantidad de Km recorridos y de Lt consumidos
cantidadKm = float(input("Ingrese la cantidad de kilómetros recorridos:"))
litrosConsumidos = float(input("Ingrese el consumo de litros por kilómetro:"))

# Calculamos el consumo de litros por kilometro recorrido
consumoLts = litrosConsumidos / cantidadKm

print("El consumo de litro por kilometro es de", consumoLts)