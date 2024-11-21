# Hola Mundo en Python - Explicación 👋

## Imprimir Texto Básico
```python
print("Hola Python")  # Usando comillas dobles
print('Hola Python')  # Usando comillas simples
```
**Explicación:** Es como decirle a Python que muestre un mensaje en la pantalla. Puedes usar comillas simples o dobles, ¡funcionan igual!

## Comentarios
```python
# Esto es un comentario de una línea
```
**Explicación:** Los comentarios son notas que escribimos para explicar nuestro código. Python no los ejecuta, son solo para nosotros.

### Comentarios Multilínea
```python
"""
Este es un comentario
que ocupa varias
líneas
"""

'''
También puedes usar
comillas simples
para varias líneas
'''
```
**Explicación:** Cuando necesitas escribir explicaciones más largas, puedes usar tres comillas seguidas. Es como escribir una nota larga en el código.

## Tipos de Datos

### Ver el Tipo de un Dato
```python
print(type("Soy un dato str"))  # Tipo string (texto)
print(type(5))                  # Tipo integer (número entero)
print(type(1.5))               # Tipo float (número decimal)
print(type(3 + 1j))           # Tipo complex (número complejo)
print(type(True))             # Tipo boolean (verdadero/falso)
```
**Explicación:** 
- `type()` es como preguntar "¿qué tipo de cosa es esto?"
- `str`: para texto
- `int`: para números enteros
- `float`: para números con decimales
- `complex`: para números complejos
- `bool`: para verdadero o falso

### Caso Especial
```python
print(type(print("Mi cadena de texto")))
```
**Explicación:** Este es un caso especial:
1. Primero muestra "Mi cadena de texto"
2. Luego muestra `NoneType` porque `print()` no devuelve ningún valor

## Tips Importantes 💡
1. Los comentarios hacen tu código más fácil de entender
2. Puedes usar comillas simples o dobles para texto
3. `type()` es muy útil para saber con qué tipo de dato estás trabajando
4. Los comentarios multilínea son buenos para explicaciones largas

## Uso Práctico
```python
# Ejemplo combinado
nombre = "Alex"  # Esto es un string
edad = 15       # Esto es un integer
altura = 1.75   # Esto es un float
es_estudiante = True  # Esto es un boolean

print(f"Nombre: {nombre}, tipo: {type(nombre)}")
```

¡Ahora ya sabes cómo hacer que Python muestre mensajes y cómo comentar tu código! 🚀