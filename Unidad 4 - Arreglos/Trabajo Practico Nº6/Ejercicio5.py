# Ejercicio 5 – Generación de un segundo arreglo
# Nivel: Avanzado
# Una empresa registra en un arreglo la cantidad de unidades vendidas de 10 productos durante un determinado período.
# A partir del arreglo original se deberá crear un segundo arreglo, denominado clasificacion.
# Para cada posición:
# •	Si la venta es menor a 20 unidades, almacenar "BAJA".
# •	Si la venta está entre 20 y 50 unidades inclusive, almacenar "MEDIA".
# •	Si la venta es mayor a 50 unidades, almacenar "ALTA".
# Finalmente determinar:
# 1.	Cantidad de productos con ventas BAJAS.
# 2.	Cantidad con ventas MEDIAS.
# 3.	Cantidad con ventas ALTAS.
# 4.	Producto con mayor cantidad de unidades vendidas.
# 5.	Posición que ocupa dicho producto en el arreglo.

n = 10 # Cantidad de Productos

ventas = []
clasificacion = []

cantidad_baja = 0
cantidad_media = 0
cantidad_alta = 0

cantidadMayor = 0
lugarMayor = 0

for i in range(n):
    
    unidades_vendidas = int(input(f"Ingresar las unidades vendidas para el producto nº { i + 1 }: "))
    
    ventas.append(unidades_vendidas)
    
for i,producto in enumerate(ventas):
    
    if i == 0 or producto > cantidadMayor:
        
        cantidadMayor = producto
        lugarMayor = i + 1
    
    if producto < 20:
        
        clasificacion.append("BAJA")
        
        cantidad_baja = cantidad_baja + 1
        
    elif producto >= 20 and producto <= 50:
        
        clasificacion.append("MEDIA")
        
        cantidad_media = cantidad_media + 1
        
    elif producto > 50:
        
        clasificacion.append("ALTA")
        
        cantidad_alta = cantidad_alta + 1
        
print()
print(f"Cantidad de Productos con ventas BAJAS: {cantidad_baja}")
print(f"Cantidad de Productos con ventas MEDIAS: {cantidad_media}")
print(f"Cantidad de Productos con ventas ALTAS: {cantidad_alta}")
print()
print(f"Producto con mayor cantidad de unidades: {cantidadMayor}\nPosicion: {lugarMayor}")