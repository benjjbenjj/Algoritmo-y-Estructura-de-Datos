# Ejercicio 4: Porcentaje de enfermos en una ciudad
# Ingresar la cantidad total de enfermos del país y la cantidad de enfermos de una
# ciudad. Calcular qué porcentaje representa la ciudad.

# Solicitamos al usuario que ingrese la cantidad de enfermos que hay en el pais y en la ciudad
enfermosPais = int(input("Ingrese la cantidad de enfermos que hay en el país:"))
enfermosCiudad = int(input("Ingrese la cantidad de enfermos que hay en la ciudad:"))

# Calculamos el porcentaje
porcentajeEnfermos = (enfermosCiudad / enfermosPais) * 100

print("El porcentaje de enfermos que representa la ciudad es %", porcentajeEnfermos)