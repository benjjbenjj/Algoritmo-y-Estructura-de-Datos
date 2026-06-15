# Ejercicio 9 – Monitoreo meteorológico
# Un aeropuerto registra observaciones meteorológicas cada hora.
# Ingresar:
# • Hora
# • Velocidad del viento
# • Visibilidad
# Finalizar con hora = -1.
# Crear funciones para determinar:
# Alertas
# • Viento fuerte si supera 60 km/h 
# • Baja visibilidad si es menor a 1000 metros
# Mostrar
# • Cantidad de alertas por viento
# • Cantidad de alertas por visibilidad
# • Promedio de visibilidad
# • Hora de mayor viento
# Este ejercicio obliga al alumno a combinar:
# • Ciclos
# • Acumuladores
# • Máximos
# • Funciones 

# Funcion/es

def alerta_viento(viento):
        return viento > 60
    
def alerta_visibilidad(visibilidad):
    return visibilidad < 1000

# Programa Principal

cantidadAlertasViento = 0
cantidadAlertasVisibilidad = 0

horaMayorViento = 'Ninguna'
mayorViento = 0

i = 0 # Contador de veces que se ingresaron los registros

sumadorVisibilidad = 0

horaRegistro = input("Ingrese la hora del registro (HH:MM) / (-1 para Finalizar): ")

if horaRegistro != '-1':
    
    while horaRegistro != '-1':
        
        velocidadVientoRegistro = float(input("Ingrese la velocidad registrada (km/h): "))
        visibilidadRegistro = float(input("Ingrese la distancia de la visibilidad (m): "))
        
        if alerta_viento(velocidadVientoRegistro):
            cantidadAlertasViento = cantidadAlertasViento + 1
        
        if alerta_visibilidad(visibilidadRegistro):
            cantidadAlertasVisibilidad = cantidadAlertasVisibilidad + 1
        
        if i == 0 or velocidadVientoRegistro > mayorViento:
            mayorViento = velocidadVientoRegistro
            horaMayorViento = horaRegistro
            
        i = i + 1
        sumadorVisibilidad = sumadorVisibilidad + visibilidadRegistro
        
        horaRegistro = input("Ingrese la hora del registro (HH:MM) / (-1 para Finalizar): ")
    
    promedio = sumadorVisibilidad / i
    
    print(f"\nCantidad de alertas por viento: {cantidadAlertasViento}")
    print(f"Cantidad de alertas por baja visibilidad: {cantidadAlertasVisibilidad}")
    print(f"Promedio de visibilidad: {promedio} m")
    print()
    print("Hora de Mayor velocidad de Viento Registrada:")
    print(f"Hora: {horaMayorViento}")
    print(f"Velocidad: {mayorViento}km/h")
else:
    print("No ha ingresado ningun registro")