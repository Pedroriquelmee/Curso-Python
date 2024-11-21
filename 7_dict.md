# Diccionarios en Python

Los diccionarios son estructuras de datos que almacenan pares clave-valor. Las claves deben ser únicas y pueden ser de cualquier tipo inmutable.

## Creación de Diccionarios

```python
# Formas de crear diccionarios vacíos
my_dict = dict()           # Usando constructor
my_other_dict = {}        # Usando llaves

# Diccionario con elementos
my_other_dict = {
    "Nombre": "Ruben",
    "Apellido": "Valentin",
    "Edad": 35,
    1: "Python"
}

# Diccionario con valores anidados
my_dict = {
    "Nombre": "Ruben",
    "Apellido": "Valentin",
    "Edad": 35,
    "Lenguajes": {"Python", "Swift", "Kotlin"},  # Set como valor
    1: 1.77  # Número como clave
}
```

## Acceso y Búsqueda

```python
# Acceso a valores
print(my_dict[1])             # Accede por clave numérica
print(my_dict["Nombre"])      # Accede por clave string

# Verificación de existencia
print("Valentin" in my_dict)  # False
print("Apellido" in my_dict)  # True
```

## Modificación del Diccionario

### Inserción y Actualización
```python
# Añadir nuevo par clave-valor
my_dict["Calle"] = "Calle ValentinDev"

# Actualizar valor existente
my_dict["Nombre"] = "Pedro"
```

### Eliminación
```python
# Eliminar par clave-valor
del my_dict["Calle"]
```

## Métodos de Diccionarios

```python
# Obtener información del diccionario
print(my_dict.items())    # Vista de pares clave-valor
print(my_dict.keys())     # Vista de claves
print(my_dict.values())   # Vista de valores
```

## Creación de Diccionarios con fromkeys()

```python
# Crear diccionario desde lista de claves
my_list = ["Nombre", 1, "Piso"]
my_new_dict = dict.fromkeys(my_list)        # Valores None por defecto

# Desde tupla
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))

# Desde claves de otro diccionario
my_new_dict = dict.fromkeys(my_dict)        # Valores None
my_new_dict = dict.fromkeys(my_dict, "ValentinDev")  # Valor específico
```

## Conversiones

```python
# Obtener valores únicos
my_values = my_new_dict.values()
print(type(my_values))    # <class 'dict_values'>

# Convertir a diferentes tipos
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(tuple(my_new_dict))  # Convierte claves a tupla
print(set(my_new_dict))    # Convierte claves a conjunto
```

### Características importantes:

1. **Claves únicas**: No puede haber claves duplicadas
2. **Claves inmutables**: Las claves deben ser de tipo inmutable (strings, números, tuplas)
3. **Valores flexibles**: Los valores pueden ser de cualquier tipo
4. **Mutabilidad**: Los diccionarios son mutables
5. **Orden**: Desde Python 3.7, mantienen el orden de inserción

### Casos de uso comunes:
- Mapeo de datos relacionados
- Cachés y memorización
- Conteo de frecuencias
- Representación de objetos JSON
- Almacenamiento de configuraciones

### Buenas prácticas:
1. Usar nombres de claves descriptivos
2. Manejar posibles KeyError al acceder a valores
3. Utilizar el método .get() para valores por defecto
4. Considerar defaultdict para valores por defecto automáticos
5. Usar comprehensions para transformaciones

### Rendimiento:
- Búsqueda por clave: O(1) en promedio
- Inserción y eliminación: O(1) en promedio
- Mayor uso de memoria que listas debido a la tabla hash