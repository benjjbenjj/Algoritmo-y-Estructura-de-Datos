# Ejercicio 1: El Validador de Notas Avanzado (Funciones con Retorno)
# Enunciado: Escribí una función llamada solicitar_nota_valida() que no reciba parámetros. La función debe pedir una nota por teclado (float) dentro de un ciclo while. Si la nota no está entre 0 y 10, debe mostrar un mensaje de error y volverla a pedir. El ciclo solo termina cuando la nota sea válida o cuando el usuario ingrese -1 (para finalizar). La función debe retornar la nota válida ingresada.

# Para el programa principal (Script): Usá esa función dentro de un bucle para cargar las notas de un curso. Al finalizar (cuando la función retorne -1), mostrá el promedio de las notas válidas.

# Concepto clave a probar: Crear una función que valide datos usando un while adentro y devuelva el valor limpio mediante return.

def solicitar_nota_valida():
    nota = float(input("Ingrese una nota entre 0 y 10 (-1 para finalizar): "))
    
    while (nota != -1 and nota < 0) or nota > 10:
        
        nota = float(input("ERROR - Ingrese una nota valida por favor (-1 para finalizar): "))
    return nota
    
n = True
notaSuma = 0
notaContador = 0

while n:
    
    notaValor = solicitar_nota_valida()
    
    if notaValor == -1:
        n = False
    else:
        notaContador = notaContador + 1
        notaSuma = notaSuma + notaValor
        
if notaContador == 0:
    promedio = 0
else:
    promedio = notaSuma / notaContador
    
print(f"\nPromedio de las notas: {promedio:.2f}")