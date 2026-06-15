# Ejercicio 3 – Evaluación académica
# Una universidad registra tres evaluaciones parciales de un alumno.
# Crear una función que calcule el promedio.
# Luego otra función deberá determinar la condición académica.
# Condiciones
# • Promociona: promedio ≥ 8
# • Regulariza: promedio ≥ 6 y < 8
# • Libre: promedio < 6
# Mostrar
# • Promedio
# • Condición obtenida 

# Funcion/es

def promedioFuncion(n1, n2, n3):
    suma = n1 + n2 + n3
    p = suma / 3
    return p

def condicionAcademica(p):
    if p >= 8:
        resultado = "Promociona"
    elif p >= 6 and p < 8:
        resultado = "Regulariza"
    elif p < 6:
        resultado = "Libre"
        
    return resultado
    
# Programa principal

nota1 = float(input("Ingrese la Nota 1: "))
nota2 = float(input("Ingrese la Nota 2: "))
nota3 = float(input("Ingrese la Nota 3: "))

promedio = promedioFuncion(nota1, nota2, nota3)
condicion = condicionAcademica(promedio)

print(f"\nPromedio: {promedio:.2f}")
print(f"Condicion: {condicion}")