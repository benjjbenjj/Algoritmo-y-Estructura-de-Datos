# Ejercicio 5: Conversión de pesos a dólares
# Ingresar una cantidad de pesos argentinos y el valor del dólar. Calcular cuántos
# dólares se pueden comprar

pesosArgentinos = int(input("Ingrese la cantidad de pesos argentinos:"))
precioDolar = float(input("Ingrese el valor del dolar:"))

compraDolares = pesosArgentinos / precioDolar

print("Usted puede comprar $", compraDolares, "dólares.")
