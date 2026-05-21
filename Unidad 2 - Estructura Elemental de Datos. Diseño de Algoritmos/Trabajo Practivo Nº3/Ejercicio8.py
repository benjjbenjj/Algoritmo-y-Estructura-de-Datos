# Ejercicio 8: Tarifa de estacionamiento
# Calcular el monto a pagar según las horas estacionadas:
# • Hasta 1 hora: $1000.
# • Más de 1 y hasta 3 horas: $2500.
# • Más de 3 y hasta 6 horas: $5000.
# • Más de 6 horas: $8000.
# Si el cliente es frecuente, aplicar 15% de descuento.

horasEstacionadas = int(input("Ingrese las horas estacionadas:"))
clienteFrec = input("Es cliente frecuente? - Responda con Si o No:")

# Validamos si es un cliente frecuente
if str.lower(clienteFrec) == "si":
    descuento = 0.85
else:
    descuento = 1

# Calculamos el monto a pagar
if horasEstacionadas <= 1:
    print("Debe pagar $", 1000 * descuento)
    
elif horasEstacionadas > 1 and horasEstacionadas <= 3:
    print("Debe pagar $", 2500 * descuento)

elif horasEstacionadas > 3 and horasEstacionadas <=6:
    print("Debe pagar $", 5000 * descuento)
    
else:
    print("Debe pagar $", 80000 * descuento)