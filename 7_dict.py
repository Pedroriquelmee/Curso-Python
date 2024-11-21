### Dictionaries ###

# Definición de diccionarios

my_dict = dict()  # Crea un diccionario vacío usando el constructor dict()
my_other_dict = {}  # Crea un diccionario vacío usando llaves {}

print(type(my_dict))  # Imprime el tipo de my_dict, que es <class 'dict'>
# Imprime el tipo de my_other_dict, que es <class 'dict'>
print(type(my_other_dict))

# Definición de un diccionario con elementos
my_other_dict = {"Nombre": "Ruben",
                 "Apellido": "Valentin", "Edad": 35, 1: "Python"}
# Claves de diferentes tipos: strings ("Nombre") y enteros (1)

# Definición de un diccionario con valores anidados
my_dict = {
    "Nombre": "Ruben",
    "Apellido": "Valentin",
    "Edad": 35,
    # Un set como valor de la clave "Lenguajes"
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1: 1.77  # Un número como clave
}

print(my_other_dict)  # Imprime el diccionario my_other_dict
print(my_dict)  # Imprime el diccionario my_dict

# Imprime el número de elementos (pares clave-valor) en my_other_dict
print(len(my_other_dict))
print(len(my_dict))  # Imprime el número de elementos en my_dict

# Búsqueda de valores en el diccionario

print(my_dict[1])  # Accede al valor de la clave 1 en my_dict
print(my_dict["Nombre"])  # Accede al valor de la clave "Nombre" en my_dict

# Verifica si "Valentin" es una clave en my_dict; devuelve False
print("Valentin" in my_dict)
# Verifica si "Apellido" es una clave en my_dict; devuelve True
print("Apellido" in my_dict)

# Inserción de nuevos pares clave-valor

# Agrega una nueva clave "Calle" con su valor
my_dict["Calle"] = "Calle ValentinDev"
print(my_dict)  # Imprime el diccionario actualizado con la nueva clave

# Actualización de valores

my_dict["Nombre"] = "Pedro"  # Cambia el valor de la clave "Nombre" a "Pedro"
print(my_dict["Nombre"])  # Imprime el nuevo valor de la clave "Nombre"

# Eliminación de pares clave-valor

del my_dict["Calle"]  # Elimina la clave "Calle" del diccionario
print(my_dict)  # Imprime el diccionario después de eliminar la clave

# Otras operaciones con diccionarios

# Imprime todos los pares clave-valor como una vista de elementos
print(my_dict.items())
print(my_dict.keys())  # Imprime todas las claves del diccionario
print(my_dict.values())  # Imprime todos los valores del diccionario

# Creación de un nuevo diccionario usando una lista de claves

my_list = ["Nombre", 1, "Piso"]  # Lista de claves para el nuevo diccionario

# Crea un diccionario con claves de my_list y valores None
my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)

# Otra forma de hacerlo con una tupla
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)

# Crea un diccionario con las mismas claves que my_dict y valores None
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)

# Crea un diccionario con las mismas claves y valores "ValentinDev"
my_new_dict = dict.fromkeys(my_dict, "ValentinDev")
print(my_new_dict)

# Exploración de valores en el diccionario

my_values = my_new_dict.values()  # Obtiene una vista de los valores de my_new_dict
# Imprime el tipo de my_values, que es <class 'dict_values'>
print(type(my_values))

print(my_new_dict.values())  # Imprime todos los valores del diccionario

# Operaciones de conversión con valores únicos y claves

# Convierte valores en una lista de claves únicas
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(tuple(my_new_dict))  # Convierte las claves del diccionario en una tupla
print(set(my_new_dict))  # Convierte las claves del diccionario en un conjunto
