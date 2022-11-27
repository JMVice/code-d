# Los booleans sólo pueden tener 2 valores:
# True o False.
# Los cuales representan encendido/apagado o verdadero o falso.
n = True # 1
z = False # 0

# Operador de equivalencia. ==
# Pregunta si los variables tienen el mismo valor.
x = 5
y = 5

a1 = x == y # True
a2 = x == 5 # True
a3 = 5 == 6 # False

print(a1) # True
print(a2) # True
print(a3) # False

# Operador de diferencia !=
# Pregunta si dos variables tienen un valor distinto

print(1 != 0)
print(1 != 1)

# Operador de mayor y menor.
# <, >, >=, <=

print(0 < 10) # True
print(0 > 10) # False

print(5 <= 5) # True
print(5 >= 5) # True

print(5 < 5) # False

# Las cadenas de texto pueden ser consultadas también.
# Los operadores de equivalencia en cadenas de texto son sensibles a mayusculas.

password_input = '1234'
password_db = '123'

print(password_input == password_db) # Contraseña incorrecta.

print('Ana' == 'Ana') # True
print('Ana' == 'ana') # False

print('Ana' != 'ana') # True
