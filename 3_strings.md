# Strings (Cadenas de texto) en Python

## Declaración de Strings
Los strings en Python pueden declararse usando comillas simples o dobles:
```python
variable1 = "Jose"
variable2 = 'Perez'

print(variable1)  # Jose
print(variable2)  # Perez
```

## Concatenación básica
```python
print(variable1 + " " + variable2)  # Jose Perez
```

## Caracteres especiales
```python
# Salto de línea (\n)
variable3 = "Esto es un string\ncon salto de linea"
print(variable3)
# Salida:
# Esto es un string
# con salto de linea

# Tabulación (\t)
variable4 = "\tEsto es un string con tabulación"
print(variable4)
# Salida: [TAB]Esto es un string con tabulación

# Escapar caracteres especiales (\)
variable_5 = "\\tEsto es un string\\ncon caracteres escapados"
print(variable_5)  # \tEsto es un string\ncon caracteres escapados
```

## Formateo de Strings
Existen varias formas de formatear strings:

### 1. f-strings (Método moderno)
```python
name, surname, age = "Ruben", "Caravaca", 50
print(f"Mi nombre es {name} {surname} y mi edad es {age}")
```

### 2. Método .format()
```python
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
```

### 3. Formateo antiguo con %
```python
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))
```

## Manipulación de Strings

### Desempaquetado de caracteres
```python
language = "Python"
a, b, c, d, e, f = language
print(a)  # P
print(b)  # y
```

### Slicing (División de strings)
```python
language = "Python"
print(language[1:3])    # yt (índices 1 y 2)
print(language[1:])     # ython (desde índice 1 hasta el final)
print(language[-2])     # o (segundo carácter desde el final)
print(language[0:6:2])  # Pto (caracteres de 0 a 6, saltando de 2 en 2)
print(language[::-1])   # nohtyP (string invertido)
```

## Funciones de String

### Modificación de strings
```python
fruit = "Strawberry"
# Reemplazar caracteres
print(fruit.replace('r', 'R'))  # StRawbeRRy

# Cambiar mayúsculas/minúsculas
print(fruit.capitalize())  # Strawberry (primera letra en mayúscula)
print(fruit.upper())       # STRAWBERRY (todo en mayúsculas)
print(fruit.lower())       # strawberry (todo en minúsculas)
```

### Análisis de strings
```python
# Contar caracteres
print(fruit.count("r"))    # 3 (número de 'r' en el string)
print(len(fruit))          # 10 (longitud total del string)

# Verificación de propiedades
print(fruit.islower())     # False (¿está todo en minúsculas?)
print(language.startswith("Py"))  # True (¿empieza con "Py"?)
```

### Ejemplos prácticos
```python
# Mostrar longitud de una variable
print(f"la variable {fruit} tiene: {len(fruit)} caracteres")

# Verificar si un string es numérico
numero_de_letras = len(fruit)
print(str(numero_de_letras).isnumeric())  # True

# Comparación sensible a mayúsculas/minúsculas
print("Py" == "py")  # False
```

### Notas importantes:
1. Los strings en Python son inmutables (no se pueden modificar directamente)
2. El índice de los strings comienza en 0
3. Los métodos de string devuelven una nueva copia del string, no modifican el original
4. Los f-strings son la forma más moderna y recomendada de formatear strings en Python