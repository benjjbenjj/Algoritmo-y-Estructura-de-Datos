# Ejercicio 3: Descuento por compra
# Ingresar el importe de una compra y si el cliente es socio.
# Si la compra supera $50.000, recibe 10% de descuento.
# Si además es socio, recibe 5% adicional.

# Ingresa el importe de la compra
importeCompra = float(input("Ingrese el importe de la compra:"))
# Preguntamos si el cliente es Socio o no
socio = input("Es socio? - Responda con Si o No:")

# Compruebo si el importe es mayor a $50.000
if importeCompra > 50000:
    
    # Hacemos el primer descuento por una compra mayor a $50.000
    precioDescuento = importeCompra * 0.9
    
    # Comprobamos si es un socio o no
    if str.lower(socio) == 'si':
        # Hacemos el segundo descuento por ser un socio
        precioSocio = precioDescuento - (importeCompra * 0.05)
        print("Su precio final es de $", precioSocio)
        
    else:
        print("Su precio final es de $", precioDescuento)

# Comprueba si el importe es menor o igual a $50.000  
else:
    print("Su precio final es $", importeCompra)