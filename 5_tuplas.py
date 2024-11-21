### Tuplas ###

# Definición de tuplas

my_tuple = tuple()  # Crea una tupla vacía usando el constructor tuple()
my_other_tuple = ()  # Crea una tupla vacía usando paréntesis

# Definición de tuplas con valores
# Tupla con diferentes tipos de datos, incluyendo duplicados
my_tuple = (35, 1.77, "Ruben", "Valentin", "Ruben")
my_other_tuple = (35, 60, 30)  # Tupla con solo valores enteros

print(my_tuple)  # Imprime la tupla my_tuple
print(type(my_tuple))  # Muestra el tipo de my_tuple, que es <class 'tuple'>

# Acceso a elementos y búsqueda en tuplas

print(my_tuple[0])  # Accede al primer elemento de my_tuple
print(my_tuple[-1])  # Accede al último elemento de my_tuple
# print(my_tuple[4])  # IndexError: fuera del rango
# print(my_tuple[-6])  # IndexError: fuera del rango

# Cuenta cuántas veces aparece "Ruben" en my_tuple
print(my_tuple.count("Ruben"))
# Encuentra el índice de "Valentin" en my_tuple
print(my_tuple.index("Valentin"))
# Encuentra el índice de la primera aparición de "Ruben" en my_tuple
print(my_tuple.index("Ruben"))

# my_tuple[1] = 1.80  # Error: las tuplas son inmutables y no permiten la reasignación de valores

# Concatenación de tuplas

# Crea una nueva tupla concatenando my_tuple y my_other_tuple
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)  # Imprime la tupla resultante de la concatenación

# Subtuplas (slicing)

# Crea una subtupla desde el índice 3 hasta el 6 (sin incluir el 6)
print(my_sum_tuple[3:6])

# Tupla mutable mediante conversión a lista

# Convierte la tupla my_tuple en una lista para permitir modificaciones
my_tuple = list(my_tuple)
# Muestra el tipo actual de my_tuple, ahora es <class 'list'>
print(type(my_tuple))

# Modificación de la lista
my_tuple[4] = "RubenValentin"  # Cambia el valor en el índice 4 de la lista
my_tuple.insert(1, "Azul")  # Inserta "Azul" en la posición 1 de la lista

# Conversión de la lista nuevamente a tupla
my_tuple = tuple(my_tuple)  # Convierte la lista de nuevo a tupla
print(my_tuple)  # Imprime la tupla modificada
# Muestra el tipo actual de my_tuple, ahora es <class 'tuple'>
print(type(my_tuple))

# Eliminación de tuplas

# del my_tuple[2]  # Error: las tuplas no permiten la eliminación de elementos específicos

del my_tuple  # Elimina completamente la variable my_tuple
# print(my_tuple)  # Error: NameError, ya que my_tuple ha sido eliminado
