# Ejercicio 3 – Sistema de ventas de un kiosco
# Enunciado
# Un kiosco registra las ventas del día hasta que el operador ingrese 0.
# Solicitar:
# • Importe de venta
# Mostrar:
# • Total vendido
# • Cantidad de ventas realizadas 

totalVendido = 0
cantidadVentas = 0

venta = float(input("Ingrese el importe de la venta (o 0 para finalizar): "))

print(f"Venta: ${venta}")

while venta != 0:
    
    venta = float(input("Ingrese el importe de la venta (o 0 para finalizar): "))
    print(f"Venta: ${venta}")
    
    cantidadVentas = cantidadVentas + 1
    totalVendido = totalVendido + venta

print()
print(f"Total Vendido: ${totalVendido}")
print(f"Cantidad de ventas: {cantidadVentas}")
    