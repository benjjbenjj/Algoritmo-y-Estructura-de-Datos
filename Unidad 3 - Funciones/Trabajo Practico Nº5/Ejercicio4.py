# Ejercicio 4 – Selección de la mejor oferta
# Una empresa recibe tres presupuestos para la compra de equipamiento.
# Desarrollar una función que determine cuál es la oferta más económica.
# Luego otra función deberá calcular cuánto dinero se ahorra respecto de la oferta más costosa.
# Mostrar
# • Oferta menor
# • Oferta mayor
# • Diferencia económica 

def ofertaEconomica(p1, p2, p3):
    if p1 <= p2 and p1 <= p3:
        econom = p1
    elif p2 <= p1 and p2 <= p3:
        econom = p2
    else:
        econom = p3
        
    if p1 >= p2 and p1 >= p3:
        caro = p1
    elif p2 >= p1 and p2 >= p3:
        caro = p2
    else:
        caro = p3
        
    return econom, caro

def ahorroPresupuesto(econom, caro):
    ahorro = caro - econom
    return ahorro
    
# Programa principal

presu1 = float(input("Ingrese el presupuesto 1: "))
presu2 = float(input("Ingrese el presupuesto 2: "))
presu3 = float(input("Ingrese el presupuesto 3: "))

menor, mayor = ofertaEconomica(presu1, presu2, presu3)
ahorro = ahorroPresupuesto(menor,mayor)

print(f"\nOferta Mayor: ${mayor}")
print(f"Oferta Menor: ${menor}")
print(f"Ahorro/Diferencia economica: ${ahorro}")