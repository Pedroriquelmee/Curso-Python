# Operadores en Python

## Operadores Aritméticos

Los operadores aritméticos en Python permiten realizar operaciones matemáticas básicas.

### Operaciones con números
```python
numero1 = 2
numero2 = 5

# Operaciones básicas
print(numero1 + numero2)  # Suma: 7
print(numero1 - numero2)  # Resta: -3
print(numero1 * numero2)  # Multiplicación: 10
print(numero1 / numero2)  # División: 0.4
print(numero1 % numero2)  # Módulo (resto de la división): 2
print(numero1 // numero2) # División entera: 0
print(numero1 ** numero2) # Exponente (2⁵): 32
```

### Operaciones combinadas
```python
# Las operaciones respetan la precedencia matemática
print(2**3 - 7/1//4)  # 8 - 7//4 = 8 - 1 = 7
```
# Explicación de la expresión en Python: `2**3 - 7/1//4`

La expresión es:

```python
2**3 - 7/1//4
```

## Paso a paso:

#### 1. **Potencia primero (`2**3`)**
El operador `**` significa "elevado a la potencia". Entonces hacemos:

```python
2**3 = 8
```

#### 2. **División (`7/1`)**
El operador `/` significa "dividir". Entonces hacemos:

```python
7/1 = 7.0
```
(Nos da 7.0 porque en Python, una división con `/` siempre da un número decimal, aunque el resultado sea exacto).

#### 3. **División entera (`7.0//4`)**
El operador `//` significa "división entera", lo que quiere decir que nos quedamos solo con la parte entera del resultado, sin decimales. Hacemos:

```python
7.0 // 4 = 1.0
```

#### 4. **Resta final (`8 - 1.0`)**
Ahora solo queda restar:

```python
8 - 1.0 = 7.0
```

Entonces, el resultado es **7.0**. Python lo muestra como un número decimal porque en algún momento de la operación apareció un número con decimales.

### Operaciones con texto (Strings)

Las cadenas de texto tienen sus propias operaciones:

```python
# Concatenación (unión de strings)
print("Hola " + "Jose")  # Salida: Hola Jose

# Concatenación con números (conversión necesaria)
# print("Hola " + 5)     # Error: no se puede concatenar string con número
print("Hola " + str(5))  # Salida: Hola 5

# Multiplicación de strings
print("-----" * 5)      # Salida: ---------------
print("Hola " * 5)      # Salida: Hola Hola Hola Hola Hola 

# Operaciones complejas con strings
print("Hola " * (3 ** 5))  # Repite "Hola " 243 veces
```

### Consideraciones con tipos de datos
```python
my_float = 2.5 * 2      # my_float = 5.0
print(type(my_float))   # Salida: <class 'float'>

# print("Hola " * my_float)  # Error: no se puede multiplicar string por float
print("Hola " * int(my_float))  # Correcto: convierte float a int
```

## Operadores Comparativos

Los operadores comparativos devuelven valores booleanos (True/False).

```python
# Mayor que
print(3 > 4)   # False

# Menor que
print(3 < 4)   # True

# Mayor o igual que
print(3 >= 4)  # False

# Menor o igual que
print(4 <= 4)  # True

# Igual a
print(3 == 4)  # False

# Diferente de
print(3 != 4)  # True

# Comparación con variables
numero1 = 2
numero2 = 5
print(numero1 != numero2)  # True
```

### Notas importantes:
1. La división (/) siempre devuelve un float, mientras que la división entera (//) devuelve un int.
2. El operador módulo (%) devuelve el resto de la división.
3. No se pueden realizar operaciones directas entre strings y números sin conversión.
4. Los operadores de comparación son útiles en estructuras de control como if, while, etc.