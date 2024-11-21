# Variables en Python

Las variables son espacios en memoria que nos permiten almacenar datos. En Python, las variables son dinámicamente tipadas, lo que significa que no necesitamos declarar su tipo explícitamente.

Imagina que tienes cajas donde guardas cosas, y cada caja tiene una etiqueta que le pones para saber qué hay dentro. Esas cajas son como variables. Puedes poner dentro de las cajas cosas diferentes: números, palabras, o incluso listas de cosas.

En Python, no necesitas decir qué tipo de cosa vas a guardar en la caja. Simplemente pones lo que quieras, y Python se da cuenta solo. Por eso se dice que las variables en Python son dinámicamente tipadas.

## Tipos básicos de variables

### Strings (Cadenas de texto)
```python
# Creación de una variable de tipo string
my_string_variable = "My String variable"
print(my_string_variable)  # Salida: My String variable
```

La variable `my_string_variable` almacena una cadena de texto. Las cadenas pueden definirse usando comillas simples ('') o dobles ("").

### Integers (Números enteros)
```python
# Creación de una variable de tipo entero
my_int_variable = 5
print(my_int_variable)  # Salida: 5
```

### Conversión entre tipos
```python
# Convertir un número a string
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)  # Salida: "5"
print(type(my_int_to_str_variable))  # Salida: <class 'str'>
```

### Booleanos
```python
# Variables booleanas (True/False)
my_bool_variable = False
print(my_bool_variable)  # Salida: False
```

## Operaciones con variables

### Concatenación y print múltiple
```python
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
# Salida: My String variable 5 False

print("Este es el valor de:", my_bool_variable)
# Salida: Este es el valor de: False
```

### Funciones útiles
```python
# Obtener la longitud de una string
print(len(my_string_variable))  # Salida: 18
```

## Asignación múltiple

Python permite asignar múltiples variables en una sola línea:
```python
name, surname, alias, age = "Ruben", "Caravaca", 'brasombra', 51
print("Me llamo:", name, surname, ". Mi edad es:", age, ". Y mi alias es:", alias)
# Salida: Me llamo: Ruben Caravaca . Mi edad es: 51 . Y mi alias es: brasombra
```

## Entrada de datos

Python permite obtener datos del usuario mediante la función `input()`:
```python
name = input('¿Cuál es tu nombre? ')
age = input('¿Cuántos años tienes? ')
```

## Tipado dinámico

En Python, una variable puede cambiar de tipo durante la ejecución del programa:
```python
name = "Ruben"  # String
name = 51       # Integer
print(name)     # Salida: 51

age = 51        # Integer
age = "Ruben"   # String
print(age)      # Salida: Ruben
```

## Type Hints (Sugerencias de tipo)

Python 3 permite sugerir tipos, aunque no son estrictamente obligatorios:
```python
address: str = "Mi dirección"  # Sugerimos que address será string
address = True   # Pero podemos asignar un booleano
address = 5      # O un entero
address = 1.2    # O un flotante
print(type(address))  # Salida: <class 'float'>
```

### Nota importante
Aunque Python permite sugerir tipos con type hints, estas sugerencias no son vinculantes. Python seguirá siendo un lenguaje de tipado dinámico y permitirá cambiar el tipo de las variables en tiempo de ejecución.