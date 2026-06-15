# Ejercicio 7 – Estadística de ventas
# Una sucursal registra las ventas realizadas durante una jornada.
# Ingresar la cantidad de ventas y luego cada importe vendido.
# Desarrollar funciones que permitan obtener:
# • Venta promedio
# • Venta mayor
# • Venta menor
# Mostrar además
# • Cantidad de ventas superiores al promedio
# • Cantidad de ventas inferiores al promedio 

def venta_prom(importeVentas, n):
    promedio = importeVentas / n
    return promedio

def venta_Mayor(importeVenta, i, mayorActual):
    
    if i == 0 or importeVenta > mayorActual:
        mayorActual = importeVenta
    
    return mayorActual

def venta_Menor(importeVenta, i, menorActual):
    
    if i == 0 or importeVenta < menorActual:
        menorActual = importeVenta
    
    return menorActual

# Programa Principal

sumaVentas = 0
ventaMayor = 0
ventaMenor = 0

contadorVentasMayor = 0
contadorVentasMenor = 0

ventas = []

n = int(input("Ingrese la cantidad de ventas: "))

for i in range(n):
    
    importeVenta = float(input(f"Ingrese el importe de la venta Nro {i + 1}: $"))
    
    sumaVentas = sumaVentas + importeVenta
    
    ventaMayor = venta_Mayor(importeVenta, i, ventaMayor)
    ventaMenor = venta_Menor(importeVenta, i, ventaMenor)
    
    ventas.append(importeVenta)
    
promedioVentas = venta_prom(sumaVentas, n)

for i in range(n):
    
    if ventas[i] > promedioVentas:
        contadorVentasMayor = contadorVentasMayor + 1
    elif ventas[i] < promedioVentas:
        contadorVentasMenor = contadorVentasMenor + 1
        
print()
print(f"Venta Promedio: ${promedioVentas}")
print(f"Venta Mayor: ${ventaMayor}")
print(f"Venta Menor: ${ventaMenor}")
print()
print(f"Cantidad de Ventas superiores al promedio: {contadorVentasMayor}")
print(f"Cantidad de Ventas inferiores al promedio: {contadorVentasMenor}")