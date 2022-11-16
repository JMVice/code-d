# Entrega

```python
# ==========================================================================================================================================

# Ejercicio 01
'''Debe comentar todos los pasos'''

# ==========================================================================================================================================

# Ejercicio 02
'''Imprimir en consola "-265 limones" el cual es un resultado de una operacion aritmetica entre 15 variables distintas. 
   Debe usar al menos 2 multiplicaciones, 2 diviciones, 2 potencias y parentesis.'''

# ==========================================================================================================================================

a = -1
b = 2
c = 3
d = 4
e = 5
f = 6
g = 7
h = 8
i = 9
j = 10      #Designar variables únicas
k = 11
l = 12
m = 13
n = 14
o = 15

print(str(round((a + b ** f + c ** d + d + e + f + g + h + i + j + k * l + n + m * o) / b / a + b)) + ' limones') 
print()
# Suma de todas las variables, se potencia divide y multiplica según fue necesario, print final para que el output sea mas ordenado


# ==========================================================================================================================================

# Ejercicio 03
""" Crear un algoritmo en donde el output sea el siguiente:

Buenos dias 'su nombre'.

Estos son los insumos actuales:

'numero 1' 'insumo 1'.
'numero 1' 'insumo 2'.
'numero 2' 'inusmo 3' advertencia de peligrosidad. """

# ==========================================================================================================================================

nombre = 'Davi'
numero1 = 45
numero2 = 24
numero3 = 12
insumo1 = 'Chocolates'           #Designar de variables requeridas para el ejercicio y la recreación
insumo2 = 'Galletas'
insumo3 = 'Botellas de Alcohol'
print('Buenos dias ' + nombre + '.')
print()
print('Estos son los insumos actuales:')                        #Print del ejercicio con variables y uso de print para formato 
print()
print(str(numero1) + '  ' + str(insumo1)+ '.')
print(str(numero1) + '  ' + str(insumo2)+ '.')
print(str(numero2) + '  ' + str(insumo3)+ ' advertencia de peligrosidad.')
print() # print final para que el output sea mas ordenado

# ==========================================================================================================================================

# Ejercicio 04
'''Recrear el ejercicio anterior pero solo usando 2 variables.'''

# ==========================================================================================================================================

print('Buenos dias Davi.')
print()
print('Estos son los insumos actuales:')                        #Print del ejercicio anterior con solo dos variables y uso de print para formato 
print()
print(str(numero1) + '  ' + str(insumo1)+ '.')
print('45' + '  Galletas.')
print('24' + '  Botellas de Alcohol advertencia de peligrosidad.')
print() # print final para que el output sea mas ordenado


""" Segunda aproximación """

encabezado = 'Bueno dias Davi.\n' + '\nEstos son los insumos actuales:\n'   

tabla = '45  Chocolates.'+ '\n45  Galletas.' + '\n24  Botellas de Alcohol advertencia de peligrosidad.'  # Solo dos variables

print(encabezado)       # Segunda aproximación del print del ejercicio anterior con solo dos variables y uso de print para formato
print(tabla)
print() # print final para que el output sea mas ordenado

# ==========================================================================================================================================
```

# Observaciones

- Recordó la cadena de texto escapada `\n` para el salto de línea sin que estuviera en los ejemplos de la clase. Bien hecho.

- En el ejericio 04 ambas aproximaciones están incorrectas aunque sus resoluciones están validas en tanto al uso de 2 variables. La aproximación esperada era el uso de 2 variables mientras estas se mutan sus valores:

```python

# Todo lo que esté entre ' debe ser sustituido por una variable.

texto = 'Davi'
numero = None

print('Buenos días ' + texto + '.')
print()
print('Estos son los insumos actuales:')
print()

numero = 45
texto = 'Chocolates'
print(str(numero) + ' ' + texto + '.')

numero = 15
texto = 'Galletas'
print(str(numero) + ' ' + texto + '.')

numero = 24
texto = 'Botellas de Alcohol'
print(str(numero) + ' ' + texto + ' advertencia de peligrosidad.')

```
