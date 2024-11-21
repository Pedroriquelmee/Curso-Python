### Ejemplos de condicionales ###

# if

# Declaramos una variable inicial
number = 10

# Condicional if básico
if number > 5:  # Verifica si el número es mayor que 5
    print("El número es mayor que 5")  # Se ejecuta si la condición es verdadera

# Cambiamos el valor de la variable
number = 3

# Nuevo condicional if con comparación explícita
if number == 3:  # Verifica si el número es igual a 3
    print("El número es igual a 3")  # Este mensaje se imprime si la condición es verdadera

# if, elif, else

# Declaramos otra variable
age = 18

if age < 18:  # Verifica si la edad es menor a 18
    print("Eres menor de edad")  # Este mensaje se imprime si la condición es verdadera
elif age == 18:  # Verifica si la edad es exactamente 18
    print("Tienes 18 años, justo en la mayoría de edad")  # Se ejecuta si la condición es verdadera
else:  # Si ninguna condición anterior se cumple
    print("Eres mayor de edad")  # Este mensaje se imprime en ese caso

print("La ejecución continúa...")  # Mensaje que indica que el programa sigue

# Inspección de valores con condicionales

# Declaramos una lista
my_list = []

# Verificamos si la lista está vacía
if not my_list:  # Se cumple si la lista está vacía
    print("La lista está vacía")  # Este mensaje se imprime si la condición es verdadera

# Añadimos un valor a la lista
my_list.append(42)

# Verificamos si la lista contiene un elemento específico
if 42 in my_list:  # Verifica si el número 42 está en la lista
    print("El número 42 está en la lista")  # Este mensaje se imprime si la condición es verdadera

# Otro ejemplo con strings
name = "Carlos"

# Verificamos si el nombre coincide con un valor
if name == "Carlos":  # Compara si el nombre es "Carlos"
    print("Hola, Carlos")  # Mensaje de bienvenida si la condición es verdadera
elif name == "María":  # Otra comparación
    print("Hola, María")  # Mensaje de bienvenida si el nombre es "María"
else:  # Si el nombre no coincide con ninguno anterior
    print("Hola, desconocido")  # Mensaje genérico

print("Fin del programa")  # Mensaje final indicando el fin de la ejecución
