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