### Ejemplos de Funciones ###

# Definición

def greet():
    print("¡Hola! Bienvenido a mi programa")

# Llamadas a la función
greet()
greet()
greet()

# Función con parámetros de entrada/argumentos

def multiply_two_values(a: int, b: int):
    print(a * b)

# Llamadas a la función con diferentes valores
multiply_two_values(3, 4)
multiply_two_values(10, 25)
multiply_two_values(1.5, 2)
multiply_two_values("Hola", 3)

# Función con parámetros de entrada/argumentos y retorno

def multiply_two_values_with_return(a, b):
    result = a * b
    return result

# Usando la función con retorno
product = multiply_two_values_with_return(6, 7)
print(f"El producto es: {product}")

product = multiply_two_values_with_return(2.5, 4)
print(f"El producto es: {product}")

# Función con parámetros de entrada/argumentos por clave

def show_full_address(city, country):
    print(f"Vives en {city}, {country}")

# Llamada a la función usando argumentos por clave
show_full_address(country="España", city="Madrid")

# Función con parámetros de entrada/argumentos por defecto

def introduce_yourself(name, profession="Desconocida"):
    print(f"Me llamo {name} y soy {profession}")

# Llamadas a la función
introduce_yourself("Luis")
introduce_yourself("Clara", "Ingeniera")

# Función con parámetros de entrada/argumentos arbitrarios

def print_lower_texts(*texts):
    print(type(texts))  # Muestra el tipo de datos de texts (una tupla)
    for text in texts:
        print(text.lower())

# Llamadas a la función con diferentes números de argumentos
print_lower_texts("HOLA", "MUNDO", "PYTHON")
print_lower_texts("ESTO ES UN TEXTO")
