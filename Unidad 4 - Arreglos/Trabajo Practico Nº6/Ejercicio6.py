# Ejercicio 6 – Sistema de análisis de pasajeros de un vuelo
# Nivel: Integrador / Mayor dificultad
# Una compañía aérea necesita analizar la información correspondiente a los pasajeros de un vuelo.
# Se conoce la cantidad N de pasajeros que realizaron el vuelo.
# Se deberán utilizar dos arreglos relacionados:
# edades
# equipajes
# En la misma posición de ambos arreglos se almacenará la información correspondiente al mismo pasajero.
# Por ejemplo:
# edades[3]
# equipajes[3]
# representan la edad y el peso del equipaje del pasajero ubicado en la posición 3.
# Primera etapa – Carga
# Solicitar N.
# Por cada pasajero ingresar:
# •	Edad.
# •	Peso del equipaje en kilogramos.
# Almacenar los datos en los arreglos correspondientes.
# Segunda etapa – Procesamiento
# Una vez finalizada la carga, recorrer los arreglos y determinar:
# 1.	Edad promedio de los pasajeros.
# 2.	Peso promedio de los equipajes.
# 3.	Cantidad de pasajeros menores de 18 años.
# 4.	Cantidad de pasajeros mayores o iguales a 60 años.
# 5.	Pasajero que transporta el equipaje de mayor peso.
# 6.	Edad de ese pasajero.
# 7.	Posición que ocupa en los arreglos.
# 8.	Cantidad de equipajes cuyo peso supera los 23 kg.
# Tercera etapa – Generación de un nuevo arreglo
# Crear un tercer arreglo denominado:
# estado_equipaje
# Para cada pasajero almacenar:
# •	"NORMAL" si el equipaje pesa hasta 23 kg inclusive.
# •	"EXCESO" si supera los 23 kg.
# Luego mostrar un informe:
# Pasajero 1
# Edad: 35
# Equipaje: 18 kg
# Estado: NORMAL

# Pasajero 2
# Edad: 42
# Equipaje: 27 kg
# Estado: EXCESO
# Cuarta etapa – Búsqueda
# Solicitar una edad determinada.
# Recorrer el arreglo edades e informar todos los pasajeros que tengan esa edad.
# Para cada coincidencia mostrar:
# •	Número de pasajero.
# •	Edad.
# •	Peso del equipaje.
# •	Estado del equipaje.
# Si no existe ningún pasajero con esa edad, informar:
# No se encontraron pasajeros con la edad indicada.
# Conceptos a aplicar
# •	Arreglos unidimensionales.
# •	Dos o más arreglos relacionados.
# •	Carga mediante append().
# •	Recorridos mediante índices.
# •	len().
# •	Acumuladores.
# •	Contadores.
# •	Promedios.
# •	Máximos.
# •	Posición de un máximo.
# •	Búsqueda secuencial.
# •	Generación de nuevos arreglos.
# •	Condicionales.
# •	Reprocesamiento de información.
# ________________________________________
# Consigna general para los 6 ejercicios
# Antes de realizar la codificación, para cada ejercicio el alumno deberá efectuar el análisis del problema, identificando:
# Datos de entrada
# ¿Qué información necesita ingresar el programa?
# Resultados
# ¿Qué información deberá producir o mostrar?
# Condiciones vinculantes
# ¿Qué condiciones, restricciones o decisiones deben verificarse durante el procesamiento?
# Arreglos necesarios
# Indicar:
# •	Nombre del arreglo.
# •	Tipo de información almacenada.
# •	Cantidad de componentes.
# •	Significado de cada posición.
# Posteriormente deberá desarrollar el programa correspondiente en Python.

n = int(input("Ingrese la cantidad de pasajeros que realizaron el vuelo: "))

#..........................................

edades = [] # Numero Edad
equipajes = [] # Peso en KG

#..........................................

sumadorEdad = 0 # Para el promedio de edad
sumadorPeso = 0 # Para el promedio de peso del equipaje

#..........................................

cantidadMenores = 0 # Pasajeros menores de 18 a;os
cantidadAdultosMayores = 0 # Pasajeros mayores o iguales a 60 a;os

#..........................................

equipajeMayorPeso = 0.00
edadMayorPeso = 0
posicionMayorPeso = 0

#..........................................

equipaje23kg = 0

#..........................................

for i in range(n): # Carga de datos de los pasajeros (edad y peso de equipaje)
    
    edadReg = int(input(f"Ingrese la edad del pasajero {i + 1}: "))
    pesoReg = float(input(f"Ingrese el peso (en kg) del equipaje: "))
    
    edades.append(edadReg)
    equipajes.append(pesoReg)
    
#..........................................

for i in range(n):
    
    sumadorEdad = sumadorEdad + edades[i]
    sumadorPeso = sumadorPeso + equipajes[i]
    
    if edades[i] < 18:
        
        cantidadMenores = cantidadMenores + 1
    
    elif edades[i] >= 60:
        
        cantidadAdultosMayores = cantidadAdultosMayores + 1
        
    if i == 0 or equipajes[i] > equipajeMayorPeso:
        
        equipajeMayorPeso = equipajes[i]
        edadMayorPeso = edades[i]
        posicionMayorPeso = i + 1
        
    if equipajes[i] > 23:
        
        equipaje23kg = equipaje23kg + 1
 
edadPromedio = sumadorEdad / n  
pesoPromedio = sumadorPeso / n
     
print()
print(f"Edad promedio de los pasajeros: {edadPromedio:.2f} años")
print(f"Peso promedio de los equipajes: {pesoPromedio:.2f} kg")
print(f"Cantidad de pasajeros menores a 18 años: {cantidadMenores}")
print(f"Cantidad de pasajeros mayores o iguales a 60 años: {cantidadAdultosMayores}")
print()
print(f"Pasajero que transporta el equipaje con mayor peso: {equipajeMayorPeso} kg")
print(f"Edad del pasajero: {edadMayorPeso}")
print(f"Posicion del pasajero: {posicionMayorPeso}")
print()
print(f"Cantidad de equipajes cuyo peso supera los 23kg: {equipaje23kg}")
print()

#..........................................
        
estadoEquipaje = []

for i in range(n):
    
    if equipajes[i] <= 23:
        
        estadoEquipaje.append("NORMAL")
        
    elif equipajes[i] > 23:
        
        estadoEquipaje.append("EXCESO")
        
for i in range(n):
    
    print(f"Pasajero {i + 1}")
    print(f"Edad: {edades[i]}")
    print(f"Equipaje: {equipajes[i]} kg")
    print(f"Estado: {estadoEquipaje[i]}")
    print()
    
print("---- Busqueda de pasajeros ----")
print()
solicEdad = int(input("Ingrese la edad para buscar pasajeros: "))

edadEncontrada = False

for i in range(n): 
    
    if edades[i] == solicEdad:
        
        edadEncontrada = True
        print(f"Numero del pasajero: {i + 1}")
        print(f"Edad del pasajero: {edades[i]}")
        print(f"Peso del equipaje: {equipajes[i]} kg")
        print(f"Estado del equipaje: {estadoEquipaje[i]}")

if not edadEncontrada:

    print("No se encontraron pasajeros con la edad indicada")
