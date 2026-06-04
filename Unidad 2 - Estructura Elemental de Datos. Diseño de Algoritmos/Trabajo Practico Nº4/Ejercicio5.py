# Ejercicio 5 – Registro de pasajeros en aeropuerto
# Enunciado
# Un aeropuerto desea registrar pasajeros hasta que se ingrese el nombre “FIN”.
# Solicitar:
# • Nombre
# • Destino
# • Peso del equipaje
# Mostrar:
# • Cantidad total de pasajeros
# • Promedio de equipaje
# • Cantidad de pasajeros con equipaje mayor a 20 kg 

cantidadPasajeros = 0 # Contador de pasajeros
pasajerosEquipaje = 0 # Contador de pasajeros con equipaje mayor a 20kg
pesoTotalEquipaje = 0 # Acumulador del peso total de los equipajes

nombrePasajero = input("Ingrese el nombre del pasajero (Ponga FIN si desea finalizar el registro): ")

while nombrePasajero != "FIN":
    
    destino = input("Ingrese el destino del pasajero: ")
    pesoEquipaje = float(input("Ingrese el peso del equipaje: "))
    
    cantidadPasajeros = cantidadPasajeros + 1
    pesoTotalEquipaje = pesoTotalEquipaje + pesoEquipaje
    
    if pesoEquipaje > 20:
        pasajerosEquipaje = pasajerosEquipaje + 1
        
    nombrePasajero = input("Ingrese el nombre del pasajero (Ponga FIN si desea finalizar el registro): ")

if cantidadPasajeros > 0:
    promedioPeso = pesoTotalEquipaje / cantidadPasajeros
else:
    promedioPeso = 0

print()
print(f"Cantidad total de pasajeros: {cantidadPasajeros}")
print(f"Promedio de peso de equipaje: {promedioPeso} kg")
print(f"Cantidad de pasajeros con equipaje mayor a 20kg: {pasajerosEquipaje}")