# Ejercicio 10: Sistema integral de compra
# Una tienda calcula el precio final según:
# • Si compra más de $100.000: 20% de descuento.
# • Si compra entre $50.000 y $100.000: 10% de descuento.
# • Si es socio: 5% adicional.
# • Si paga con transferencia: 3% adicional.
# • Si paga con tarjeta en cuotas: recargo del 12%.

# Solicitamos los siguientes datos al usuario
precioCompra = float(input("Ingrese el monto de la compra:"))
socio = input("Es socio? - Responda con Si o No")
metodoPago = input("Elija el metodo de pago.\n1)Efectivo\n2)Transferencia\n3) Tarjeta en Cuotas")

if str.lower(socio) == 'si':
    # Si es socio le damos un descuento del 5%
    socioDescuento = 0.05
else:
    # Si no es socio no hacemos ningun descuento
    socioDescuento = 0

if metodoPago == '1':
    # Si paga en efectivo no hacemos ningun descuento
    recargoDescuento = 0
    
elif metodoPago == '2':
    # Si paga con transferencia le hacemos un descuento del 3%
    recargoDescuento = 0.03
elif metodoPago == '3':
    # Si paga con Tarjeta en cuotas le hacemos un recargo del 12%
    recargoDescuento = -0.12

# Calculo el precio con descuentos de socios y descuento/recargo de metodo de pago
precioPreFinal = precioCompra - (precioCompra * socioDescuento) - (precioCompra * recargoDescuento)

# Validamos el precio final de la compra
if precioCompra < 50000:
    print("Precio Final: $", precioPreFinal)
    
elif precioCompra >=50000 and precioCompra <= 100000:
    descuento50K = 0.1
    print("Precio Final: $", precioPreFinal - (precioCompra * descuento50K))
    
elif precioCompra > 100000:
    descuento100K = 0.2
    print("Precio Final: $", precioPreFinal - (precioCompra * descuento100K))