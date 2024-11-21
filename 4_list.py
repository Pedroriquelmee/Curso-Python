### Lists ###

# Definición de listas vacías

my_list = list()  # Crea una lista vacía usando el constructor list()
my_other_list = []  # Crea una lista vacía usando corchetes []

print(len(my_list))  # Imprime la longitud de la lista vacía, que es 0

# Definición de una lista con valores

my_list = [35, 24, 62, 52, 30, 30, 17]  # Lista con valores enteros

print(my_list)  # Imprime la lista con valores
print(len(my_list))  # Imprime la longitud de la lista (número de elementos)

# Definición de una lista con diferentes tipos de datos

# Lista con enteros, float, y strings
my_other_list = [35, 1.77, "Ruben", "Caravaca"]

print(type(my_list))  # Muestra el tipo de my_list, que es <class 'list'>
# Muestra el tipo de my_other_list, que es <class 'list'>
print(type(my_other_list))

# Acceso a elementos y búsqueda

print(my_other_list[0])  # Accede al primer elemento de la lista
print(my_other_list[1])  # Accede al segundo elemento de la lista
print(my_other_list[-1])  # Accede al último elemento de la lista
# Accede al primer elemento (equivalente a my_other_list[0])
print(my_other_list[-4])
print(my_list.count(30))  # Cuenta cuántas veces aparece el valor 30 en my_list

# Acceso a un índice fuera del rango genera un error
# print(my_other_list[4])  # IndexError: fuera del rango
# print(my_other_list[-5])  # IndexError: fuera del rango

# Encuentra el índice del valor "Brais" en my_other_list
print(my_other_list.index("Ruben"))

# Desempaquetado de listas en variables

# Asigna cada elemento de my_other_list a una variable
age, height, name, surname = my_other_list
print(name)  # Imprime el valor de la variable name

# Desempaquetado individual
name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)  # Imprime el valor de la variable age

# Concatenación de listas

# Combina my_list y my_other_list en una nueva lista
print(my_list + my_other_list)
# print(my_list - my_other_list)  # No se puede restar listas, esto generaría un error

# Creación, inserción, actualización y eliminación de elementos

my_other_list.append("Caravaca")  # Agrega "MoureDev" al final de my_other_list
print(my_other_list)

my_other_list.insert(1, "Rojo")  # Inserta "Rojo" en la posición 1
print(my_other_list)

my_other_list[1] = "Azul"  # Cambia el valor en la posición 1 a "Azul"
print(my_other_list)

# Elimina el primer elemento con valor "Azul" de la lista
my_other_list.remove("Azul")
print(my_other_list)

my_list.remove(30)  # Elimina la primera aparición de 30 en my_list
print(my_list)

print(my_list.pop())  # Elimina y devuelve el último elemento de my_list
print(my_list)  # Imprime my_list después de la eliminación

# Elimina y devuelve el elemento en la posición 2
my_pop_element = my_list.pop(2)
print(my_pop_element)  # Imprime el valor eliminado
print(my_list)  # Imprime my_list después de la eliminación

del my_list[2]  # Elimina el elemento en la posición 2
print(my_list)  # Imprime my_list después de la eliminación

# Operaciones con listas

my_new_list = my_list.copy()  # Crea una copia de my_list

my_list.clear()  # Vacía todos los elementos de my_list
print(my_list)  # Imprime la lista vacía
print(my_new_list)  # Imprime la copia de la lista original

my_new_list.reverse()  # Invierte el orden de los elementos en my_new_list
print(my_new_list)  # Imprime my_new_list invertida

my_new_list.sort()  # Ordena los elementos de my_new_list
print(my_new_list)  # Imprime my_new_list ordenada

# Sublistas (slicing)

# Crea una sublista desde el índice 1 hasta el 3 (sin incluir el 3)
print(my_new_list[1:3])

# Cambio de tipo de lista a string

my_list = "Hola Python"  # Reasigna my_list a un string
print(my_list)  # Imprime el nuevo valor de my_list
print(type(my_list))  # Muestra el tipo actual de my_list, ahora es <class 'str'>
