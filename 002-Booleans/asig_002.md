# Asignación 002

- Haga un algoritmo que pregunte el nombre y apellido de dos personas, que imprima el nombre de cada persona y verifique si tienen el mismo apellido.

- Cree un emulador de login. Pregunta el nombre de usuario y la contraseña. Si el nombre de usuario es "admin" y la contraseña es "cma92Q!.#1" imprima "Bienvenido". Si no, imprima "Usuario o contraseña incorrectos".

- Modifique el ejercicio anterior para que, en caso de ser la contraseña incorrecta, preguntar si tiene un código de recuperación "2bow O0w0 9999". De ser correcto, el usuario puede ingresar.

- Elabore una calculadora. El usuario debe poder ingresar dos números y el programa debe imprimir la suma, resta, multiplicación y división de ambos números. El usuario puede elegir que operación quiere realizar.

- Haga un algoritmo de su preferencia que cumpla con los siguientes criterios: 
    - Tiene al menos el uso de 2 variables de tipo boolean.
    - Tiene al menos el uso de 2 condicionales.
    - Hace uso de al menos una vez del operador lógico AND y OR.

# Entrega

```python
# ===============================
# Ejercio 01
# ===============================

#Primera persona
print ('Usuario #1: ')
w = input ('Cual es su nombre? ')                    #Variables de input user
x = input ('Cual es su apellido? ')

print (w + ' ' + x) 

#Segunda persona
print ('Usuario #2: ')
y = input ('Cual es su nombre? ')
z = input ('Cual es su apellido? ')
print (y + ' ' + z)
print ('Coinciden los apellidos? ')                 #Comparación de apellidos
print (x == z)

# ===============================
# Ejercio 02
# ===============================

print ('LOGIN')                                       
a = input ('Nombre de Usuario: ')                     #Variables de input user
b = input ('Contraseña: ')

user = a
user_db = 'admin'                                     #Login de admin con respuesta a respuesta correcta e incorrecta
password_input = b
password_db = 'cma92Q!.#1'
denied = 'Usuario o contraseña incorrectos.'

if (password_input == password_db) and (user == user_db):
    print ('Bienvenido')
else :
    print (denied)

if password_input != password_db : 
    print ('Tiene un código de recuperación? y/n: ')

# ===============================
# Ejercio 03
# ===============================

d = 'y'
e = 'n'
_2fa_db = '2bow O0w0 9999'
_2fa_question = input()
_2fa_input = input ('Introduzca el codigo: ')            #Pregunta para el codigo de recuperacion 

if d == _2fa_question :
    print (_2fa_input)
elif e == _2fa_question :
    print ('Intentelo de nuevo desde el inicio mamawebo')  
else :
    print ()

if _2fa_input == _2fa_db :
    print ('Bienvenido')
else:
    print ('Mamawebo no intente robar cuentas. Puto')


# ===============================
# Ejercio 04
# ===============================

print ('Calculadora')
print ('Operaciones')
print ('+')
print ('-')                             #Operaciones
print ('*')
print ('/')

def suma(x, y):
    return x + y
def resta(x, y):                        #designar operaciones a calculos
    return x - y
def multiplicacion(x, y):
    return x * y
def division(x, y):
    return x / y    

x = input ('primer numero: ')
y = input ('segundo numero: ')                                #inputs de user
math_resolver = input('Elegir +  -  *  / : ')

if math_resolver == '+':
    print(x, "+", y, "=", suma(int(x), int(y)))
elif math_resolver == '-':
    print(x, "-", y, "=", resta(int(x), int(y)))                    #condicionales sobre elección del user
elif math_resolver == '*':
    print(x, "*", y, "=", multiplicacion(int(x), int(y)))
elif math_resolver == '/':
    print(x, "/", y, "=", round(division(int(x), int(y))))


# ===============================
# Ejercio 05
# ===============================

x = (5 != 5)            #Variables
y = (10 >= 1)
print( x and y (10 >= 1) and (x == y))              #Boolean y operador logico and
print ('Ana' != 'Juan')
if 10 == 10:                                        #Condicionales
  print ('ve mamawebo si era igual')
elif 15 != 4 :
    print ('ve si son diferetes')
elif x == y :
    print ('ni idea de que es esto xd')
else :
    print ()
```

# Observaciones

- El ejercicio 003 pregunta por el código de recuperación aún cuando se especifica que no se tiene.
