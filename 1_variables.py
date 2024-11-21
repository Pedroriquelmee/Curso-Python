### Variables ###

# Se asigna una cadena de texto a la variable 'my_string_variable'
my_string_variable = "My String variable"
# Imprime el valor de la variable 'my_string_variable', que es "My String variable"
print(my_string_variable)

my_int_variable = 5  # Se asigna un número entero a la variable 'my_int_variable'
print(my_int_variable)  # Imprime el valor de 'my_int_variable', que es 5

# Convierte el valor entero '5' a una cadena de texto y lo guarda en 'my_int_to_str_variable'
my_int_to_str_variable = str(my_int_variable)
# Imprime el valor de 'my_int_to_str_variable', que ahora es "5" (cadena de texto)
print(my_int_to_str_variable)
# Imprime el tipo de dato de 'my_int_to_str_variable', que será 'str' (cadena)
print(type(my_int_to_str_variable))

# Asigna el valor booleano 'False' a la variable 'my_bool_variable'
my_bool_variable = False
print(my_bool_variable)  # Imprime el valor de 'my_bool_variable', que es False

# Concatenación de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
# Imprime varias variables en una sola línea, separadas por espacios: "My String variable 5 False"

print("Este es el valor de:", my_bool_variable)
# Imprime un texto y el valor de 'my_bool_variable': "Este es el valor de: False"

# Algunas funciones del sistema
print(len(my_string_variable))
# La función 'len()' devuelve la longitud de la cadena 'my_string_variable'. Aquí imprimirá 18, que es el número de caracteres de la cadena.

# Variables en una sola línea. ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Ruben", "Caravaca", 'brasombra', 51
# Se asignan múltiples variables en una sola línea. 'name' toma el valor "Ruben", 'surname' toma "Caravaca", 'alias' toma "brasombra" y 'age' toma 51.

print("Me llamo:", name, surname, ". Mi edad es:",
      age, ". Y mi alias es:", alias)
# Imprime las variables con un texto descriptivo: "Me llamo: Ruben Caravaca . Mi edad es: 51 . Y mi alias es: brasombra"

# Inputs
name = input('¿Cuál es tu nombre? ')
# Pide al usuario que ingrese su nombre y almacena el valor en la variable 'name'

age = input('¿Cuántos años tienes? ')
# Pide al usuario que ingrese su edad y almacena el valor en la variable 'age'

print(name)  # Imprime el nombre ingresado por el usuario
print(age)  # Imprime la edad ingresada por el usuario

# Cambiamos su tipo
# Ahora se reasigna un valor entero a la variable 'name' (antes era una cadena de texto)
name = 51
# Ahora se reasigna una cadena de texto a la variable 'age' (antes era numérica)
age = "Ruben"
print(name)  # Imprime el nuevo valor de 'name', que ahora es 51
print(age)  # Imprime el nuevo valor de 'age', que ahora es "Ruben"

# ¿Forzamos el tipo?
address: str = "Mi dirección"
# Se indica que la variable 'address' será de tipo 'str' (cadena de texto), pero Python no obliga a respetarlo.

address = True  # Reasignamos un valor booleano a 'address'
address = 5  # Luego un valor entero
address = 1.2  # Finalmente, un valor decimal
print(type(address))
# Imprime el tipo actual de 'address', que será 'float' (el último valor asignado es 1.2, que es un número decimal).
