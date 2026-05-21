# Ejercicio 8: Precio final con IVA
# Ingresar el precio de un producto sin IVA. Calcular el precio final agregando un 21%.

precioProducto = float(input("Ingrese el precio del producto:"))
valorIva = 21

precioFinal = precioProducto * (1 + valorIva /100)

print("El precio a pagar es $", precioFinal)