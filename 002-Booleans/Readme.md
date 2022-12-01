# Resumen

# Booleans

```python
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

```

# Operadores lógicos

```python
# Operadores logicos AND y OR

# ========================================
# AND
# ========================================

#      True         True
#      vvvvvv      vvvvvvvv
print((5 == 5) and (5 == 5)) # True

#      True         False
#      vvvvvv      vvvvvvvv
print((5 == 5) and (5 == 0)) # False

password_input_2 = '123'
password_db_2 = '123'

_2fa_input = '123456'
_2fa_app = '482913'

print((password_input_2 == password_db_2) and (_2fa_input == _2fa_app)) # False

# ========================================
# OR
# ========================================

print((5 == 0) or (10 == 10)) # True

```

# Condicionales

```python
# Las condicionales basicas son
# if, else, elif.

# if evalua si la consulta es verdadero.
# Para hacer la consulta se utilizan boolean
# con operadores logicos.

# ===================================
# if
# ===================================

if 5 == 5: 
    print('Es verdadero')

if 5 == 10: 
    print('Es verdadero') # El codigo no llega aqui

if (10 == 10) and (15 == 15):
    print('Es verdadero')

if 5 != 10: 
    print('Es verdadero')

# ===================================
# else
# ===================================

# else no puede existir sin haber un if primero.
if 10 != 10:
    print() # El codigo no llega aqui
else:
    print ('Es falso')

# ===================================
# elif
# ===================================

# No es necesario que termine con un else.
if 10 == 15:
    print() # El codigo no llega aqui
elif 15 == 20:
    print() # El codigo no llega aqui
elif 15 == 18 and 15 > 200:
    print() # El codigo no llega aqui

# Ejemplo que termina con else.
if 10 == 15:
    print() # El codigo no llega aqui
elif 15 == 20:
    print() # El codigo no llega aqui
elif 15 == 18 and 15 > 200:
    print() # El codigo no llega aqui
else:
    print('Ninguno es verdadero')
```

# Password Simulator

```python
# input() se utiliza para pedirle al usuario que
# ingrese el valor que tendra una variable.

# Ejemplo de suma de numeros.
x = input('Ingrese el primer numero: ')
y = input('Ingrese el segundo numero: ')

print(int(x) + int(y))

# Simulador de pedir contraseña.

password_input = input('Ingrese la contraseña: ')
password_db = '12345'

if password_input == password_db:
    print('La contraseña es correcta.')
else:
    print('La contraseña es incorrecta.')

input('El programa ha finalizado.')
```

# Lab

- Haga un algoritmo que pregunte su nombre completo y lo imprima en consola.

- Haga un algoritmo que haga una resta de inventario, es decir, que pregunte cuantos productos tiene en inventario y cuantos vendió, y que imprima cuantos le quedan. El output además debe mostrar el nombre del producto.

- Haga un algoritmo que su output sea lo siguiente (debe utilizar input para contruir la piramide:

```
*
**
***
**
*
```

- Haga un algoritmo que reciba 2 números e imprima el mayor de ellos.

# Entrega lab

```python
x = input ('Cual es su nombre completo?')
print (x)

x = input ('Articulo: ') 
z = int (input ('Cantidad de Articulos: '))
y = int ( input ('Cuantos vendio rasta? '))

print (x + ' ' + str (z))
print ()
print (z - y)
print ()
input ('rasta ya no hay na mas, va jalao') 

print ('Dibuje una piramide ak7:')
v = input () 
w = input () 
x = input ()
y = input () 
z = input ()
print ( v + '\n' + w + '\n' + x + '\n' + y + '\n' + z ) 

x = input ('primer numero: ')
y = input ('segundo numero: ')

if x == y :
    print ('Son iguales')
elif x > y : 
    print (x)
else: print (y)
```

# Observaciones

- El ejercicio número 2 funciona correctamente pero con deficiencias. Mostrar un mensaje de que ya no hay existencias siempre. Muestra output de cuantos hay restantes pero no claramente que significa ese output. Es decir, para el usuario debería mostrar, por ejemplo, "Le quedan 5 unidades".

- El último ejercicio no funciona correctamente debido a que debe convertir los output en numeros. Recuerde que por defecto son strings.

```python
#   vvv CONVERTIR A NÚMERO
x = int(input ('primer numero: '))
#   vvv CONVERTIR A NÚMERO
y = int(input ('segundo numero: '))

if x == y :
    print ('Son iguales')
elif x > y :
    print (x)
else: 
    print (y)
```