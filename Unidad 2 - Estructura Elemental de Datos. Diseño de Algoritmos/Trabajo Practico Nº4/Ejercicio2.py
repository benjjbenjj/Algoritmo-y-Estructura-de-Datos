# Ejercicio 2 – Control de temperatura de una cámara frigorífica
# Enunciado
# Durante 7 horas se registra la temperatura de una cámara frigorífica.
# Mostrar:
# • Todas las temperaturas
# • Promedio general

# Conceptos aplicados
# • Acumulador
# • Promedio
# • FOR 

print("-- Control de temperatura de cámara frigorífica --")

# Registros obtenidos en cada hora
n = 7

# Lista donde guardaremos los registros
registro = ""

# Sumador de todas las temperaturas (acumulador)
sumadorTemp = 0

# Bucle donde solicitaremos las temperaturas registradas
for i in range(n):
    
    # Solicitamos cada temperatura
    temperaturas = float(input(f"Ingrese la temperatura nº {i+1}: "))
    
    # Guardamos la temperatura en el registro
    registro = registro + f"Temperatura Nº {i+1}: {temperaturas} ºC\n"
    
    sumadorTemp = sumadorTemp + temperaturas

promedioTemperaturas = sumadorTemp / n

print()
print(f"Temperaturas registradas: {n}")
print()

print(registro)
    
print(f"Promedio de las temperaturas: {promedioTemperaturas} ºC")