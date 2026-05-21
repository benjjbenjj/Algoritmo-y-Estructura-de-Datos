# Ejercicio 5: Clasificación de edad con validación
# Ingresar la edad de una persona.
# Validar que no sea negativa ni mayor a 120.
# Luego clasificarla como:
# • Niño
# • Adolescente
# • Adulto
# • Adulto mayor 

edad = int(input("Ingrese la edad de la persona:"))

if edad > 0 and edad <= 120:
    
    if edad <= 10:
        print("Niño")
        
    elif edad > 10 and edad < 18:
        print("Adolescente")
        
    elif edad >=18 and edad < 60:
        print("Adulto")
        
    else:
        print("Adulto Mayor")
else:
    print("Edad invalida")