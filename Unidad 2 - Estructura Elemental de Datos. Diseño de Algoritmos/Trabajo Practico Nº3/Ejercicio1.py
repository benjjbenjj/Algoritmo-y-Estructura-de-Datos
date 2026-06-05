# Ejercicio 1: Clasificación de producto
# Una tienda desea clasificar un producto según su precio.
# Ingresar el precio de un producto e indicar:
# • “Económico” si cuesta menos de $10.000.
# • “Intermedio” si cuesta entre $10.000 y $50.000.
# • “Premium” si cuesta más de $50.000. 

# Solicitamos el precio del producto
precioProducto = float(input("Ingrese el precio del producto:"))

if precioProducto < 10000 and precioProducto > 0:
    print("El producto es Economico.")
    
elif precioProducto >= 10000 and precioProducto < 50000:
    print("El prodcuto es Intermedio.")
    
elif precioProducto >= 50000:
    print("El producto es Premium.")
    
else:
    print("Ingrese un precio valido.")
    # Este es en caso de ingresar un precio menor que cero, lo cual lo invalida.