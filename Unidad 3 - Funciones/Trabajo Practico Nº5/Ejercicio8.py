# Ejercicio 8 – Operaciones de vuelo
# Un aeropuerto registra operaciones aéreas.
# Por cada vuelo ingresar:
# • Número de vuelo
# • Cantidad de pasajeros
# Finalizar con número de vuelo igual a 0.
# Utilizar funciones para determinar:
# • Total de pasajeros transportados
# • Promedio de pasajeros por vuelo
# • Vuelo con mayor cantidad de pasajeros
# Mostrar
# Todos los resultados obtenidos.
# El alumno deberá decidir qué información debe mantenerse durante todo el proceso.

def total_pasajeros(cantidadPasajeros, sumaPasajeros):
    sumaPasajeros = sumaPasajeros + cantidadPasajeros
    return sumaPasajeros

def promedio_pasajeros(totalPasajeros, cantidadVuelos):
    promedio = totalPasajeros / cantidadVuelos
    return promedio

def mayorVuelos(numeroVuelo, cantidadPasajeros, i, mayorCantidad, vueloMayor):
    if i == 0 or cantidadPasajeros > mayorCantidad:
        vueloMayor = numeroVuelo
        mayorCantidad = cantidadPasajeros
        return vueloMayor, mayorCantidad
    else:
        return vueloMayor, mayorCantidad

# Programa principal

sumaPasajeros = 0
vueloMayor = "Ninguno"
vueloMayorNumero = 0
cantidadVuelos = 0

numeroVuelo = int(input("Ingrese el Nro. de vuelo (0 para Finalizar): "))

if numeroVuelo != 0:
 
    while numeroVuelo != 0:
        cantidadPasajeros = int(input("Ingrese la cantidad de pasajeros: "))
        
        sumaPasajeros = total_pasajeros(cantidadPasajeros, sumaPasajeros)
        
        vueloMayor, vueloMayorNumero = mayorVuelos(numeroVuelo, cantidadPasajeros, cantidadVuelos, vueloMayorNumero, vueloMayor)
        
        cantidadVuelos = cantidadVuelos + 1
        
        numeroVuelo = int(input("Ingrese el Nro. de vuelo (0 para Finalizar): "))
        
    promedio = promedio_pasajeros(sumaPasajeros, cantidadVuelos)
        
    print()
    print(f"Total de pasajeros transportados: {sumaPasajeros}")
    print(f"Promedio de pasajeros por vuelo: {promedio}")
    print()
    print(f"Vuelo con mayor cantidad de pasajeros:\nNro: {vueloMayor}\nCantidad: {vueloMayorNumero}")
    
else:
    print(f"No ha registrado ninguna operacion aerea.")