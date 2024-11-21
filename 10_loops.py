### Ejemplos de Loops ###

# While

counter = 1  # Inicializamos un contador

# Bucle while básico
while counter <= 5:  # Se ejecuta mientras el contador sea menor o igual a 5
    print(f"Contador actual: {counter}")  # Imprime el valor actual del contador
    counter += 1  # Incrementa el contador en 1
else:  # Esta parte se ejecuta si el bucle no se rompe con un break
    print("El contador es mayor que 5")

print("La ejecución continúa")

# Ejemplo con una condición de salida
counter = 0

while counter < 10:  # Se ejecuta mientras el contador sea menor que 10
    counter += 1  # Incrementa el contador
    if counter == 7:  # Si el contador es igual a 7
        print("Bucle detenido en 7")
        break  # Sale del bucle
    print(counter)  # Imprime el valor actual del contador

print("La ejecución continúa")

# For

# Iterar sobre una lista de nombres
names = ["Ana", "Luis", "Pedro", "Clara"]

for name in names:  # Itera sobre cada elemento de la lista
    print(f"Hola, {name}")  # Saluda a cada nombre

# Iterar sobre una tupla de edades
ages = (25, 30, 35, 40)

for age in ages:  # Itera sobre cada edad en la tupla
    print(f"Tienes {age} años")  # Imprime cada edad

# Iterar sobre un conjunto de números
numbers_set = {10, 20, 30, 40}

for number in numbers_set:  # Itera sobre cada elemento del conjunto
    print(f"Número: {number}")  # Imprime el número actual

# Iterar sobre un diccionario con clave-valor
person = {"Nombre": "María", "Edad": 28, "Ciudad": "Madrid"}

for key, value in person.items():  # Itera sobre las claves y valores del diccionario
    print(f"{key}: {value}")  # Imprime la clave y el valor actual
    if key == "Edad":  # Si la clave es "Edad"
        break  # Detiene el bucle

print("La ejecución continúa")

# Ejemplo con continue
for key, value in person.items():  # Itera sobre claves y valores
    if key == "Ciudad":  # Si la clave es "Ciudad"
        continue  # Salta a la siguiente iteración
    print(f"{key}: {value}")  # Imprime clave y valor si no se cumplió el continue
else:  # Se ejecuta al finalizar el bucle sin un break
    print("El bucle for sobre el diccionario ha finalizado")

print("Fin del programa")
