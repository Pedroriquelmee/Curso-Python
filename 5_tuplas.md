# Tuplas en Python

Las tuplas son estructuras de datos inmutables que permiten almacenar colecciones ordenadas de elementos. A diferencia de las listas, una vez creadas, no se pueden modificar sus elementos.

## Creación de Tuplas

```python
# Formas de crear tuplas vacías
my_tuple = tuple()  # Usando el constructor
my_other_tuple = () # Usando paréntesis

# Tuplas con valores
my_tuple = (35, 1.77, "Ruben", "Valentin", "Ruben")
my_other_tuple = (35, 60, 30)

print(type(my_tuple))  # <class 'tuple'>
```

## Acceso a Elementos

```python
# Acceso por índice
print(my_tuple[0])   # 35 (primer elemento)
print(my_tuple[-1])  # "Ruben" (último elemento)

# Búsqueda
print(my_tuple.count("Ruben"))    # Cuenta ocurrencias de "Ruben"
print(my_tuple.index("Valentin"))    # Índice donde se encuentra "Valentin"
print(my_tuple.index("Ruben"))    # Índice de la primera aparición de "Ruben"
```

## Operaciones con Tuplas

### Concatenación
```python
# Unir dos tuplas
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)
```

### Slicing (Subtuplas)
```python
# Crear una subtupla
print(my_sum_tuple[3:6])  # Elementos desde índice 3 hasta 6 (exclusivo)
```

## Inmutabilidad y Conversiones

Las tuplas son inmutables, lo que significa que no se pueden modificar después de su creación:

```python
# Esto generaría un error
# my_tuple[1] = 1.80  # TypeError: 'tuple' object does not support item assignment

# Para modificar una tupla, hay que convertirla a lista
my_tuple = list(my_tuple)     # Convierte a lista
my_tuple[4] = "RubenValentin"      # Modifica la lista
my_tuple.insert(1, "Azul")    # Inserta nuevo elemento
my_tuple = tuple(my_tuple)    # Convierte de nuevo a tupla
```

## Eliminación

```python
# No se pueden eliminar elementos individuales
# del my_tuple[2]  # TypeError

# Se puede eliminar la tupla completa
del my_tuple
# print(my_tuple)  # NameError: name 'my_tuple' is not defined
```

### Puntos importantes a recordar:

1. Las tuplas son inmutables: una vez creadas, no se pueden modificar sus elementos
2. Los elementos de una tupla pueden ser de diferentes tipos
3. Las tuplas permiten elementos duplicados
4. El acceso a elementos es por índice (comienza en 0)
5. Los índices negativos cuentan desde el final (-1 es el último elemento)
6. Para modificar una tupla, debe convertirse primero a lista
7. Se pueden eliminar tuplas completas pero no elementos individuales

### Ventajas de las tuplas sobre las listas:
- Son más rápidas
- Protegen los datos contra modificaciones accidentales
- Pueden usarse como claves en diccionarios
- Usan menos memoria

### Casos de uso comunes:
- Datos que no deben cambiar (constantes)
- Retorno de múltiples valores en funciones
- Datos heterogéneos relacionados (como coordenadas)
- Cuando se necesita garantizar que los datos no sean modificados