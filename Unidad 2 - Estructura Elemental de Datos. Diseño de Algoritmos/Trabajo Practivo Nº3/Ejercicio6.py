# Ejercicio 6: Calculadora con validaciones
# Ingresar dos números y una operación matemática.
# Resolver suma, resta, multiplicación o división.
# Si se divide por cero, mostrar error

print("A continuación debe ingresar dos números para realizar las operaciones básicas.")
print("En el caso de la división el primer numero será el dividendo y el segundo número será el divisor.")

numero1 = float(input("Ingrese el primer número:"))
numero2 = float(input("Ingrese el segundo número:"))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2

if numero2 == 0:
    print("")
    print("Resultado de la suma:", suma)
    print("Resultado de la resta:", resta)
    print("Resultado de la multiplicación:", multiplicacion)
    print("La division no se puede realizar porque el divisor es igual a cero.")
    
else:
    division = numero1 / numero2
    print("")
    print("Resultado de la suma:", suma)
    print("Resultado de la resta:", resta)
    print("Resultado de la multiplicación:", multiplicacion)
    print("Resultado de la división:", division)