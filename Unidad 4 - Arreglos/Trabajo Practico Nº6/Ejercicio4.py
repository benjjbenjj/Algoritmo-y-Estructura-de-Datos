# Ejercicio 4 – Búsqueda y modificación de stock
# Nivel: Intermedio/Avanzado
# Un depósito almacena las cantidades disponibles de 12 productos.
# Cada posición del arreglo representa un producto:
# Posición 0 → Producto 1
# Posición 1 → Producto 2
# Posición 2 → Producto 3
# ...
# Desarrollar un programa que permita:
# 1.	Cargar el stock de los 12 productos.
# 2.	Mostrar el stock completo.
# 3.	Solicitar al usuario un número de producto.
# 4.	Informar el stock actual del producto solicitado.
# 5.	Solicitar una cantidad retirada del depósito.
# 6.	Verificar que exista stock suficiente.
# 7.	Si existe stock suficiente, descontar la cantidad directamente del arreglo.
# 8.	Si no existe stock suficiente, mostrar un mensaje indicando que la operación no puede realizarse.
# 9.	Mostrar el arreglo actualizado.
# 10.	Informar cuántos productos quedaron con stock inferior a 5 unidades.

n = 12 # Cantidad de productos

productos = []

stock_inferior = 0

print("-- Cargado de stock de los 12 productos --")

for i in range(n):
    
    stock_carga = int(input(f"Ingrese el stock del producto {i+1}: "))
    
    productos.append(stock_carga)
    
print()
print("-- Stock de los 12 productos --")

for i, stock in enumerate(productos):
    
    print(f"Producto {i+1}: {stock}")
    
print()
numeroProducto = int(input("Ingrese el numero del producto que desea ver stock (1 a 12): "))

print(f"Producto {numeroProducto}: {productos[numeroProducto - 1]}")
cantidadRetiro = int(input("Ingrese la cantidad a retirar del producto:"))

if cantidadRetiro > productos[numeroProducto - 1]:
    print("No se puede retirar un stock mayor al existente.")
else:
    productos[numeroProducto - 1] = productos[numeroProducto - 1] - cantidadRetiro
    
print()
print("-- Stock Actualizado --")

for i, stock in enumerate(productos):
    
    print(f"Producto: {i+1} - Stock: {stock}")

for i, stock in enumerate(productos):
    
    if stock < 5:
        stock_inferior = stock_inferior + 1

print()
print(f"Productos con Stock inferior a 5 unidades: {stock_inferior}")