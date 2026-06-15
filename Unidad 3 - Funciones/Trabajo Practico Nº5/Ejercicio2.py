# Ejercicio 2 – Consumo de combustible
# Un operador aeroportuario desea conocer la eficiencia de una unidad móvil.
# Ingresar:
# • Kilómetros recorridos
# • Litros consumidos
# Desarrollar una función que calcule el rendimiento del vehículo expresado en kilómetros por litro.
# Mostrar:
# • Rendimiento obtenido
# • Clasificación
# Clasificación
# • Excelente: más de 15 km/l
# • Bueno: entre 10 y 15 km/l
# • Deficiente: menos de 10 km/l

# Funciones

def rendimientoCombustible(km, lts):
    rendimiento = km / lts
    return rendimiento

# Programa principal

KmRecorridos = float(input("Ingrese los kilometros recorridos: "))
LtsConsumidos = float(input("Ingrese los litrs de combustible consumidos: "))

rendimiento = rendimientoCombustible(KmRecorridos, LtsConsumidos)

if rendimiento > 15:
        clasificacion = "Excelente"
elif rendimiento >= 10 and rendimiento <= 15:
        clasificacion = "Bueno"
elif rendimiento < 10:
        clasificacion = "Deficiente"

print(f"\nRendimiento obtenido: {rendimiento} km/l")
print(f"Clasificacion: {clasificacion}")