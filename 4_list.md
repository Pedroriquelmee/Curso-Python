# Listas en Python

Las listas son estructuras de datos que permiten almacenar colecciones ordenadas de elementos. Pueden contener elementos de diferentes tipos y son mutables (modificables).

## Creación de Listas

```python
# Formas de crear listas vacías
my_list = list()  # Usando el constructor
my_other_list = []  # Usando corchetes
print(len(my_list))  # 0

# Lista con valores
my_list = [35, 24, 62, 52, 30, 30, 17]
print(len(my_list))  # 7

# Lista con diferentes tipos de datos
my_other_list = [35, 1.77, "Ruben", "Caravaca"]
```

## Acceso a Elementos

```python
# Acceso por índice (comienza en 0)
print(my_other_list[0])   # 35
print(my_other_list[1])   # 1.77
print(my_other_list[-1])  # "Caravaca" (último elemento)
print(my_other_list[-4])  # 35 (primer elemento desde el final)

# Búsqueda
print(my_list.count(30))          # Cuenta ocurrencias de 30
print(my_other_list.index("Ruben"))  # Índice donde se encuentra "Ruben"
```

## Desempaquetado de Listas

```python
# Desempaquetado completo
age, height, name, surname = my_other_list
print(name)  # "Ruben"

# Desempaquetado selectivo
name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
```

## Modificación de Listas

### Añadir elementos
```python
my_other_list.append("Caravaca")    # Añade al final
my_other_list.insert(1, "Rojo")     # Inserta en posición específica
```

### Actualizar elementos
```python
my_other_list[1] = "Azul"  # Modifica elemento en posición 1
```

### Eliminar elementos
```python
my_other_list.remove("Azul")  # Elimina primera ocurrencia
my_list.pop()                 # Elimina y retorna último elemento
my_list.pop(2)               # Elimina y retorna elemento en índice 2
del my_list[2]               # Elimina elemento en índice 2
```

## Operaciones con Listas

### Copiar y limpiar
```python
my_new_list = my_list.copy()  # Crea una copia
my_list.clear()               # Vacía la lista
```

### Ordenamiento
```python
my_new_list.reverse()  # Invierte el orden
my_new_list.sort()     # Ordena los elementos
```

### Concatenación
```python
combined_list = my_list + my_other_list  # Une dos listas
```

## Slicing (Sublistas)
```python
print(my_new_list[1:3])  # Elementos desde índice 1 hasta 3 (exclusivo)
```

## Conversión de tipos
```python
my_list = "Hola Python"  # Convierte la variable a string
print(type(my_list))     # <class 'str'>
```

### Notas importantes:
1. Los índices comienzan en 0
2. Los índices negativos cuentan desde el final (-1 es el último elemento)
3. Las listas pueden contener elementos de diferentes tipos
4. Las listas son mutables (se pueden modificar después de su creación)
5. El acceso a índices fuera de rango genera un IndexError
6. La operación de resta (-) no está definida para listas

Esta guía cubre las operaciones básicas con listas en Python. Las listas son una de las estructuras de datos más versátiles y utilizadas en Python, por lo que es importante dominar su uso.