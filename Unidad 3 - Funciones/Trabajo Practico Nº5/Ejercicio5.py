# Ejercicio 5 – Control de temperatura operativa
# Durante una inspección técnica se registran temperaturas de equipos electrónicos.
# Ingresar:
# • Temperatura mínima permitida
# • Temperatura máxima permitida
# • Temperatura actual
# Desarrollar una función que determine el estado del equipo.
# Estados
# • Bajo rango
# • Normal
# • Sobrecalentado
# Mostrar
# • Estado
# • Diferencia respecto del límite excedido 

# Funcion/es

def estadoTemperatura(temp, max, min):
    if temp < min:
        estado = "Bajo Rango"
    elif temp > max:
        estado = "Sobrecalentado"
    elif min <= temp <= max:
        estado = "Normal"
    return estado


# Programa principal

temperaturaMin = float(input("Ingrese la temperatura minima permitida: "))
temperaturaMax = float(input("Ingrese la temperatura maxima permitida: "))
temperaturaAct = float(input("Ingrese la temperatura registrada: "))

while temperaturaMax <= temperaturaMin:
    
    print("\nLa temperatura maxima no debe ser menor o igual que la temperatura minima, por favor ingrese nuevamente el maximo y minimo permitido\n")
    temperaturaMin = float(input("Ingrese la temperatura minima permitida: "))
    temperaturaMax = float(input("Ingrese la temperatura maxima permitida: "))
    
estadoResultado = estadoTemperatura(temperaturaAct, temperaturaMax, temperaturaMin)

print(f"\nEstado: {estadoResultado}")

if estadoResultado.lower() == "sobrecalentado":
    print(f"Diferencia respecto del limite excedido: {temperaturaAct - temperaturaMax}°C")
elif estadoResultado.lower() == "bajo rango":
    print(f"Diferencia respecto del limite excedido: {temperaturaMin - temperaturaAct}°C")