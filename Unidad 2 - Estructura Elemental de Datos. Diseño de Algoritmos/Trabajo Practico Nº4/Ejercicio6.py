# Ejercicio 6 – Monitoreo de lluvias
# Enunciado
# Durante 30 días se registran los milímetros de lluvia caídos.
# Mostrar:
# • Día con mayor lluvia
# • Día con menor lluvia
# • Promedio mensual
# Conceptos aplicados
# • Máximos y mínimos
# • Acumuladores
# • Análisis de datos 

n = 30 # Dias con registros de lluvias

diaMayor = 0 # Variable que registra el dia con mayor cantidad de lluvia caida
numeroDiaMayor = 0

diaMenor = 0 # Variable que registra el dia con menor cantidad de lluvia caida
numeroDiaMenor = 0

cantidadLluvia = 0

### <<<<<<<<<<<       >>>>>>>>>>>>>>>>

for i in range(n):
    
    lluviaCaida = float(input(f"DIA Nº { i + 1 } - Ingrese la cantidad en mm de lluvia caida: "))
    
    if i == 0:
        diaMayor = lluviaCaida
        diaMenor = lluviaCaida

        numeroDiaMayor = i + 1
        numeroDiaMenor = i + 1

    else:
        if lluviaCaida > diaMayor:
            diaMayor = lluviaCaida
            numeroDiaMayor = i + 1
        elif lluviaCaida < diaMenor:
            diaMenor = lluviaCaida
            numeroDiaMenor = i + 1

    cantidadLluvia = cantidadLluvia + lluviaCaida
    
promedioLluvia = cantidadLluvia / n

print()
print(f"El dia {numeroDiaMayor} tuvo mayor cantidad de lluvia y fue de {diaMayor}mm")
print(f"El dia {numeroDiaMenor} tuvo menor cantidad de lluvia y fue de {diaMenor}mm")
print(f"Promedio de lluvia en el mes: {promedioLluvia} mm")