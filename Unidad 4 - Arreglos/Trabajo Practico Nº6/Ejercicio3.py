# Ejercicio 3 – Control de ventas diarias
# Nivel: Intermedio
# Un comercio registra el importe total vendido durante 15 días.
# Desarrollar un programa que almacene las ventas en un arreglo y posteriormente determine:
# 1.	Venta total acumulada.
# 2.	Venta promedio diaria.
# 3.	Mayor venta registrada.
# 4.	Día en que ocurrió la mayor venta.
# 5.	Menor venta registrada.
# 6.	Día en que ocurrió la menor venta.
# 7.	Cantidad de días cuyas ventas fueron superiores al promedio.
# 8.	Mostrar las ventas desde el último día hasta el primero.

n = 15 # Dias

ventas = [] # Lista

venta_total = 0 # Acumulador de Ventas

mayor_venta = 0 # Maximo
dia_mayor = ""
menor_venta = 0 # Minimo
dia_menor = ""

dias_superiores = 0

for i in range(n):
    
    venta_reg = float(input(f"Ingrese el importe de la venta del dia {i + 1}: "))
    
    venta_total = venta_total + venta_reg # Acumulador de ventas funcionando
    
    ventas.append(venta_reg)
    
venta_promedio = venta_total / n # Promedio de ventas
    
for i, venta in enumerate(ventas):
    
        if i == 0 or venta > mayor_venta:
            mayor_venta = venta
            dia_mayor = f"{i + 1}"
        
        if i == 0 or venta < menor_venta:
            menor_venta = venta
            dia_menor = f"{i + 1}"
            
        if venta > venta_promedio:
            dias_superiores = dias_superiores + 1
     
print()       
print(f"Venta total acumulada: ${venta_total}")
print(f"Venta promedio diaria: ${venta_promedio:.2f}")
print()
print(f"Mayor Venta Registrada: \n${mayor_venta}\nDia Nro.: {dia_mayor}")
print()
print(f"Menor Venta Registrada: \n${menor_venta}\nDia Nro.: {dia_menor}")
print()
print(f"Cantidad de dias cuyas ventas fueron superiores al promedio: {dias_superiores}")
print()
print("-- Ventas desde el ultimo dia hasta el primero --")

for i in range(len(ventas) -1,-1, -1):
    
    print(f"Dia {i + 1}: ${ventas[i]}")