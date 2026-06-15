# Ejercicio 2: Conversor de Monedas de Aeropuerto (Pasaje de Parámetros)
# Enunciado: Creá una función llamada convertir_moneda(monto_pesos, tipo_moneda) que reciba dos parámetros: el monto en pesos argentinos y un string que indique la moneda extranjera ("USD" o "EUR"). La función debe calcular la conversión (asumí valores ficticios, por ejemplo: 1 USD = $1000, 1 EUR = $1100) y retornar el valor convertido.

# Para el programa principal (Script): Registrá transacciones de turistas en una casa de cambio hasta que el monto en pesos ingresado sea 0. Por cada turista, solicitá el monto y la moneda deseada, llamá a la función y mostrá el resultado en consola. Al final, informá cuántos dólares y cuántos euros se vendieron en total.

# VALORES FICTICIOS:
# USD = $1000
# EUR = $1100

cantidadUSD = 0
cantidadEUR = 0

def convertir_moneda(montoPesos, tipoMoneda):
    if str.lower(tipoMoneda) == "usd":
        valor = montoPesos / 1000
        return valor
    elif str.lower(tipoMoneda) == "eur":
        valor = montoPesos / 1100
        return valor

monto = float(input("Ingrese el monto en ARS (pesos argentinos - 0 para finalizar): "))

moneda = input("Ingrese la moneda de cambio (USD o EUR): ")

while monto != 0:
    
    if monto < 0 or (str.lower(moneda) != "usd" and str.lower(moneda) != "eur"):
        print("ERROR - Ingrese nuevamente los siguientes datos: \n")
        
        monto = float(input("Ingrese un monto valido en ARS (pesos argentinos): "))
        moneda = input("Ingrese una moneda de conversion valida (USD o EUR): ")
    else:
        
        valorCambio = convertir_moneda(monto, moneda)
        
        if str.lower(moneda) == "usd":
            cantidadUSD = cantidadUSD + valorCambio
        elif str.lower(moneda) == "eur":
            cantidadEUR = cantidadEUR + valorCambio


        print(f"Se ha cambiado {valorCambio:.2f} {str.upper(moneda)}")
        
        monto = float(input("Ingrese un monto valido en ARS (pesos argentinos): "))
        moneda = input("Ingrese una moneda de conversion valida (USD o EUR): ")

print()
print(f"Cantidad de USD vendidos: {cantidadUSD:.2f} USD")
print(f"Cantidad de EUR vendidos: {cantidadEUR:.2f} EUR")