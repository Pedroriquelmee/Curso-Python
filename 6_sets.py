# Definición de conjuntos

my_set = set()  # Crea un conjunto vacío usando el constructor set()
my_other_set = {}  # Al usar solo {} sin elementos, se crea un diccionario, no un conjunto

print(type(my_set))  # Imprime <class 'set'>, que indica que my_set es un conjunto
# Imprime <class 'dict'>, ya que {} se interpreta como un diccionario vacío
print(type(my_other_set))

# Redefinición de my_other_set como conjunto con elementos
# Crea un conjunto con varios tipos de datos
my_other_set = {"Ruben", "Valentin", 35}
print(type(my_other_set))  # Imprime <class 'set'>

print(len(my_other_set))  # Imprime el número de elementos en el conjunto (3)

# Inserción de elementos en el conjunto

my_other_set.add("RuebenValentin")  # Agrega "RuebenValentin" al conjunto
print(my_other_set)  # Imprime el conjunto; el orden no está garantizado

# Intento de agregar "RuebenValentin" de nuevo; los duplicados no se añaden
my_other_set.add("RuebenValentin")
print(my_other_set)  # El conjunto no cambia, sigue sin duplicados

# Búsqueda de elementos en el conjunto

# Verifica si "Ruben" está en el conjunto; devuelve True
print("Ruben" in my_other_set)
# Verifica si "Rube" está en el conjunto; devuelve False
print("Rube" in my_other_set)

# Eliminación de elementos en el conjunto

my_other_set.remove("Valentin")  # Elimina "Valentin" del conjunto
print(my_other_set)  # Imprime el conjunto actualizado

my_other_set.clear()  # Vacía todos los elementos del conjunto
print(len(my_other_set))  # Imprime la longitud del conjunto vacío (0)

del my_other_set  # Elimina el conjunto completamente
# print(my_other_set)  # Da un error (NameError) ya que el conjunto ha sido eliminado

# Transformación de un conjunto en otra estructura de datos

my_set = {"Ruben", "Valentin", 35}  # Crea un nuevo conjunto
my_list = list(my_set)  # Convierte el conjunto en una lista
print(my_list)  # Imprime la lista resultante
print(my_list[0])  # Accede al primer elemento de la lista

# Definición de un nuevo conjunto para realizar operaciones

# Crea otro conjunto con lenguajes de programación
my_other_set = {"Kotlin", "Swift", "Python"}

# Otras operaciones con conjuntos

# Une my_set y my_other_set en un nuevo conjunto
my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union(
    {"JavaScript", "C#"}))  # Uniones múltiples con otros conjuntos

# Muestra los elementos de my_new_set que no están en my_set
print(my_new_set.difference(my_set))
