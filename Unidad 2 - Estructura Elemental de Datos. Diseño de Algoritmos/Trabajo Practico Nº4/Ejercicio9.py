# Ejercicio 9 – Sistema de monitoreo meteorológico aeroportuario

# Enunciado
# Un aeropuerto registra condiciones meteorológicas cada hora.

# Solicitar:
# • Hora
# • Velocidad del viento
# • Visibilidad
# Finalizar al ingresar hora = -1.

# Mostrar:
# • Cantidad de alertas por viento fuerte (> 60 km/h)
# • Cantidad de alertas por baja visibilidad (< 1000 m)
# • Promedio de visibilidad

# Conceptos aplicados
# • Condiciones múltiples
# • Acumuladores
# • Variables de control 

alertaVientoFuerte = 0
alertaBajaVisib = 0

visibilidadSuma = 0
visibilidadCont = 0

hora = input("Ingresar la hora (-1 para finalizar): ")

while hora != "-1":
    
    velocidadViento = float(input("Ingrese la velocidad del viento (km/h): "))
    visibilidad = float(input("Ingrese la visibilidad (m): "))
    
    visibilidadSuma = visibilidadSuma + visibilidad
    visibilidadCont = visibilidadCont + 1
    
    if velocidadViento > 60:
        alertaVientoFuerte = alertaVientoFuerte + 1
    if visibilidad < 1000:
        alertaBajaVisib = alertaBajaVisib + 1
    
    hora = input("Ingresar la hora (-1 para finalizar): ")
    
if (visibilidadCont == 0):
    promedioVisibilidad = 0
else:
    promedioVisibilidad = visibilidadSuma / visibilidadCont
    
print()
print(f"Cantidad de alertas por viento fuerte (> 60 km/h): {alertaVientoFuerte}")
print()
print(f"Cantidad de alertas por baja visibilidad ( < 1000 m): {alertaBajaVisib}")
print()
print(f"Promedio de visibilidad: {promedioVisibilidad:.2f} m")