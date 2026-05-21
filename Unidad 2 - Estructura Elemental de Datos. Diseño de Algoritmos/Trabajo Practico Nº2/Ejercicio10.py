# Ejercicio 10: Hipotenusa de un triángulo rectángulo
# Ingresar los dos catetos de un triángulo rectángulo y calcular la hipotenusa.

catetoAd = float(input("Ingrese el valor del cateto adyacente:"))
catetoOp = float(input("Ingrese el valor del cateto opuesto:"))

hipotenusa2 = round(((catetoOp ** 2) + (catetoAd ** 2)) ** 0.5, 2)

print("El valor de la hipotenusa es", hipotenusa2)