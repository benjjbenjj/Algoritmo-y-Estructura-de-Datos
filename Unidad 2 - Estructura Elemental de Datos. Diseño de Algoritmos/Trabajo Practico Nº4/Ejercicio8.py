# Ejercicio 8 – Control de stock de supermercado

# Enunciado
# Un supermercado registra productos hasta ingresar código 0.

# Solicitar:
# • Código
# • Nombre
# • Cantidad en stock

# Mostrar:
# • Productos con stock menor a 5
# • Cantidad total de productos
# • Producto con mayor stock

# Conceptos aplicados
# • Comparaciones
# • Máximos
# • Control de inventario

# Variables para trabajar y mostrar
menorStock = 0 # Muestra la cantidad de productos con un stock menor a 5
totalProductos = 0 # Muestra el total de los productos ingresados
mayorStock = 0 # Muestra el producto con mayor stock

nombreMayor = 'Ninguno'

codigoProducto = int(input("Ingrese el código del producto: "))

while codigoProducto > 0:
    
    totalProductos = totalProductos + 1
    
    nombre = input("Ingrese el nombre del producto: ")
    stock = int(input("Ingrese la cantidad de stock del producto: "))
    
    if totalProductos == 1 or stock > mayorStock:
        mayorStock = stock
        nombreMayor = nombre
    
    if stock < 5:
        menorStock = menorStock + 1

    codigoProducto = int(input("Ingrese el código del producto: "))
    
print()
print(f"Productos con stock menor a 5 unidades: {menorStock}")
print()
print(f"Cantidad total de productos: {totalProductos}")
print()
print(f"Producto con mayor stock:")
print(f"Nombre: {nombreMayor}")
print(f"Cantidad: {mayorStock}")