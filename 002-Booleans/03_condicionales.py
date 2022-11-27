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