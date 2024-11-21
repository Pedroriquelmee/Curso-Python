# Conjuntos (Sets) en Python

Los conjuntos son estructuras de datos que almacenan elementos únicos y desordenados. A diferencia de las listas y tuplas, los conjuntos no permiten duplicados y no mantienen un orden específico.

## Creación de Conjuntos

```python
# Creación de conjuntos
my_set = set()           # Conjunto vacío usando constructor
my_other_set = {}        # ¡Cuidado! Esto crea un diccionario vacío

print(type(my_set))         # <class 'set'>
print(type(my_other_set))   # <class 'dict'>

# Conjunto con elementos
my_other_set = {"Ruben", "Valentin", 35}
print(len(my_other_set))    # 3
```

## Operaciones Básicas

### Añadir elementos
```python
my_other_set.add("RuebenValentin")
print(my_other_set)

# Los duplicados se ignoran automáticamente
my_other_set.add("RuebenValentin")  # No se añade de nuevo
```

### Búsqueda de elementos
```python
print("Ruben" in my_other_set)   # True
print("Rube" in my_other_set)    # False
```

### Eliminación de elementos
```python
# Eliminar un elemento específico
my_other_set.remove("Valentin")
print(my_other_set)

# Vaciar el conjunto
my_other_set.clear()
print(len(my_other_set))    # 0

# Eliminar el conjunto completo
del my_other_set
# print(my_other_set)  # NameError
```

## Conversión entre Tipos de Datos

```python
my_set = {"Ruben", "Valentin", 35}
my_list = list(my_set)      # Conversión a lista
print(my_list)              # Orden no garantizado
print(my_list[0])          # Acceso por índice después de convertir
```

## Operaciones con Conjuntos

```python
my_set = {"Ruben", "Valentin", 35}
my_other_set = {"Kotlin", "Swift", "Python"}

# Unión de conjuntos
my_new_set = my_set.union(my_other_set)

# Uniones múltiples
print(my_new_set.union(my_new_set)
                .union(my_set)
                .union({"JavaScript", "C#"}))

# Diferencia entre conjuntos
print(my_new_set.difference(my_set))
```

### Características importantes:

1. **Unicidad**: Los conjuntos no permiten elementos duplicados
2. **Desorden**: Los elementos no mantienen un orden específico
3. **Mutabilidad**: Los conjuntos son mutables (se pueden modificar)
4. **Heterogeneidad**: Pueden contener diferentes tipos de datos
5. **Hashable**: Los elementos deben ser inmutables (no pueden contener listas o diccionarios)

### Casos de uso comunes:
- Eliminar duplicados de una secuencia
- Operaciones matemáticas de conjuntos (unión, intersección, diferencia)
- Verificar membresía de elementos de manera eficiente
- Mantener colecciones de elementos únicos

### Operaciones adicionales disponibles:
- `intersection()`: Elementos comunes entre conjuntos
- `difference()`: Elementos en un conjunto pero no en otro
- `symmetric_difference()`: Elementos en cualquiera de los conjuntos, pero no en ambos
- `issubset()`: Verifica si un conjunto está contenido en otro
- `issuperset()`: Verifica si un conjunto contiene a otro

### Notas de rendimiento:
- Las operaciones de búsqueda son muy eficientes (O(1) en promedio)
- Útiles cuando la unicidad y la velocidad de búsqueda son importantes
- Consumen más memoria que las listas debido a su implementación hash