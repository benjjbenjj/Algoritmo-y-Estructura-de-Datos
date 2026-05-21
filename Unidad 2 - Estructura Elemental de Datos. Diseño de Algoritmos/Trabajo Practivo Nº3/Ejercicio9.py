# Ejercicio 9: Evaluación de vuelo
# Una aeronave puede despegar si:
# • La visibilidad es mayor o igual a 1500 metros.
# • El viento es menor o igual a 35 nudos.
# • No hay tormenta eléctrica.
# • La pista está operativa. 

# Solicitamos los siguientes datos
visibilidad = int(input("Ingrese la distancia de visibilidad:"))
viento = int(input("Ingrese los nudos del viento:"))
tormentasElec = input("Hay tormentas electricas? - Responda con Si o No:")
pistaOper = input("La pista esta operativa? - Responda con Si o No:")

if visibilidad >= 1500 and viento <= 35 and str.lower(tormentasElec) == 'no' and str.lower(pistaOper) == 'si':
    print("Puede despegar.")
else:
    print("No puede despegar.")