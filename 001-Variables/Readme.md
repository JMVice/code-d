# Asignación 001

- Debe comentar todos los pasos que este haciendo.

- Imprimir en consola "-265 limones" el cual es un resultado de una operacion aritmetica entre 15 variables distintas. Debe usar al menos 2 multiplicaciones, 2 diviciones, 2 potencias y parentesis.

- Crear un algoritmo en donde el output sea el siguiente:

```
Buenos dias 'su nombre'.

Estos son los insumos actuales:

'numero 1' 'insumo 1'.
'numero 1' 'insumo 2'.
'numero 2' 'inusmo 3' advertencia de peligrosidad.
```

Cada definicion que se encuentra entre ' debe ser una variable.

- Recrear el ejercicio anterior pero solo usando 2 variables.

Fecha limite de entrega: Miercoles 16 de Noviembre antes de las 23:59.

# Resumen

```python
# Este es un comentario.

'''
Comentarios
multi linea
'''

```
```python
# Variable sin valor.

n = None

# Variable de tipo número.

x = 5
y = 10

# Variables de tipo cadena de texto o String.

nombre = "Alberto"
otro_nombre = 'Carlos'

# Función print()

print(x) # => 5
print(y) # => 10
print() # => 'Salto de linea'.
print(nombre) # => Alberto
print(otro_nombre) # => Carlos
print()
# Print con salto de linea incluido en string.
print('Hola\nMundo') # => Hola
                    # => Mundo

# Output:

'''
5
10

Alberto
Carlos

Hola
Mundo
'''

```
```python
# Sumas
x = 5
y = 10
z = x + y # => 15

print(z) # => 15
print(z + 10) # => 25

# Restas

resta_x = 10
resta_y = 9

print(resta_y - resta_x) # => -1

# Multiplicación y Divición

print(25 * 4) # => 100
print(100 / 4) # => 25.0
print(round(100 / 4)) # => 25

```
```python
# Contatenación de Integer con String
nombre = 'Xinia'
x = 5

# No es posible concatenar String con Integer.
# Debe convertir el Integer a String.
# Para eso, se utiliza la función str().
print(nombre + str(x)) # => Xinia5

```

# Lab

- Haga un algoritmo que haga una operación aritmetica usando al menos 5 variables.

- Haga un algoritmo que haga una operación aritmetica que haga uso de una divición una multiplicación y su resultado sea 50.

- Haga un algoritmo que imprima su nombre.

- Haga un algoritmo que su output sea lo siguiente:

```
*
**
***
**
*
```

- Haga un algoritmo que muestre el nombre de una persona, su edad y su altura. Debe mostrarse de esta forma:
"(Nombre) (Apellido). Edad: (Edad). Altura: (Altura).
Cada cosa dentro de los () debe ser una variable.

# Lab results

```python
# ===============================
# Ejercio 01
# ===============================
a = 1
b = 2
c = 3
d = 4
e = 5

print(a + b + c + d + e) # Ejercicio 01

print(round((e**2)*d/b )) # Ejercicio 02 redondeado

print("Alberto") # Ejercio 03

print('*')
print('**')
print('***')  # Ejercio 04
print('**')
print('*')

nombre = 'Louis '
apellido = 'Zing'
edad = str(17) #'17'
altura = '1.73'

print(nombre + apellido + '.' + ' Edad:' + edad + '. Altura: ' + altura) # Ejercio 05
```
