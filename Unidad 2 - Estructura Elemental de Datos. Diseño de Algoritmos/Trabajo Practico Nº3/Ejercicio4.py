# Ejercicio 4: Control de acceso a un sistema
# Un sistema solicita:
# • nombre de usuario,
# • contraseña,
# • y si la cuenta está activa o no.
# 
# El usuario podrá ingresar al sistema solamente si:
# • el nombre de usuario es correcto,
# • la contraseña es correcta,
# • y la cuenta se encuentra activa.
# 
# Mostrar por pantalla:
# • “Acceso permitido” si cumple todas las condiciones.
# • “Acceso denegado” si alguna condición no se cumple.

# Usuario y Contraseña ya establecidos
usuario = "juanito1234"
contraseña = "juanitopro"

# Ahora solicitamos el nombre de usuario y contraseña para validar el acceso
ingresoUsuario = input("Ingrese su nombre de usuario:")
ingresoContraseña = input("Ingrese su contraseña:")
activa = input("Su cuenta está activa? - Responda con Si o No")

# Comprobamos si su cuenta está activa
if activa == str.lower("si"):
    cuentaActiva = True
else:
    cuentaActiva = False

# Comprobamos si puede acceder al sistema
if ingresoUsuario == usuario and ingresoContraseña == contraseña and cuentaActiva == True:
    print("Acceso Permitido")
else:
    print("Acceso Denegado")
