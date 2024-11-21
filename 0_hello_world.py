### Hola Mundo ###

# Nuestro hola mundo en Python
print("Hola Python")  # Imprime la cadena de texto "Hola Python" en la consola
# También imprime la cadena de texto "Hola Python", pero usando comillas simples
print('Hola Python')

# Esto es un comentario
# Los comentarios en Python comienzan con el símbolo '#' y no son ejecutados por el programa

"""
Este es un
comentario
en varias líneas
"""
# Este bloque entre comillas triples es un comentario o texto de varias líneas. Aunque realmente es una cadena de texto no asignada,
# se utiliza frecuentemente como comentarios de múltiples líneas.

'''
Este también es un
comentario
en varias líneas
'''
# Similar al comentario anterior, este es un comentario de varias líneas usando comillas simples triples.

# Cómo consultar el tipo de dato
# La función type() devuelve el tipo de dato. Aquí imprime que el tipo es 'str' (cadena de texto)
print(type("Soy un dato str"))
print(type(5))  # Imprime el tipo 'int' (entero) del número 5
print(type(1.5))  # Imprime el tipo 'float' para el número decimal 1.5
# Imprime el tipo 'complex' (número complejo) para el valor 3 + 1j
print(type(3 + 1j))
print(type(True))  # Imprime el tipo 'bool' (booleano) para el valor True

# Primero imprime "Mi cadena de texto".
print(type(print("Mi cadena de texto")))
# Luego, la función print() no retorna ningún valor (retorna None), y type() imprime que ese valor es de tipo 'NoneType'.
