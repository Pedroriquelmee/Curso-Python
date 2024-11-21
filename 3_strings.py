### Strings ###

# Declaración de strings usando comillas simples y dobles
variable1 = "Jose"
variable2 = 'Perez'


print(variable1)
print(variable2)

# Concatenar string con un espacio en blanco
print(variable1 + " " + variable2)

# Crear un salto de linea

variable3 = "Esto es un string\ncon salto de linea"
print(variable3)

# Insertar tabulacion
variable4 = "\tEsto es un string con salto de linea"
print(variable4)


# Escapar caracteres especiales
variable_5 = "\\tEsto es un string\\ncon salto de linea"
print(variable_5)

# Formateo de strings

name, surname, age = "Ruben", "Caravaca", 50

# Formateo usando .format()

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))

# Formateo antiguo usando %

print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))

# Cocatenar varios string

print("Mi nombre es" + name + " " + surname + " y mi edad es " + str(age))

# Formateo usando f-strings (moderno)

print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# desempaquetando caracteres

language = "Python"

a, b, c, d, e, f = language

print(a)
print(b)

# Dividir string (Slice)

# toma el segundo caracter hasta el 3(sin incluir el índice 3)
language_slice = language[1:3]
print(language_slice)  # output:  yt

language_slice = language[1:]  # Toma el segundo caracter hasta el final
print(language_slice)

language_slice = language[-2]  # Toma el segundo caracter por detras
print(language_slice)

# Toma caracteres de índice 0 al 6, saltado de 2 en 2
language_slice = language[0:6:2]
print(language_slice)

# Revertir la cadena de texto
language_slice = language[::-1]
print(language_slice)

### Funciones de string ###

# Remplazar caracteres de un string

fruit = "Strawberry"
fruit_replace = fruit.replace('r', 'R')
print(fruit_replace)

# Convertir el primer caracter del texto a Mayuscula
print(fruit.capitalize())

# Convertir el texto a Mayusculas

print(fruit.upper())

# Contar cuantos caracteres hay del mismo tipo
print(fruit.count("r"))

# Contar todos los caracteres de una palabra
print(len(fruit))


# Ejemplos
print(f"la variable {fruit} tiene: " + str(len(fruit)))

numero_de_letras = len(fruit)
print(numero_de_letras)
print(str(numero_de_letras).isnumeric())

# Convertir el texto a Minusculas

print(fruit.lower())

# Verificar si todo el texto esta en minusculas

print(fruit.islower())

# Verificar comienza la cadena con unos caracteres
# Ejemplo Py

print(language.startswith("Py"))

# Compara si "Py" es igual a "py" (sensible a mayúsculas y minúsculas)
print("Py" == "py")  # Output: False
