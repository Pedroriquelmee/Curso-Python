# Ejercicios de Entrada/Salida en Python

Este documento presenta varios ejercicios básicos que demuestran la interacción con el usuario mediante entrada y salida de datos en Python.

## 1. Lectura de Número

```python
print("=" * 20)
print("LECTURA DE NÚMERO")
print("=" * 20)

numero = int(input("Dame un número (no letras): "))
print(f"Me has dado el número: {numero}")
```

**Explicación:**
- Usa `input()` para obtener entrada del usuario
- `int()` convierte la entrada en número entero
- f-strings para formatear la salida
- Manejo básico de entrada/salida

## 2. Calculadora Básica

```python
print("=" * 20)
print("CALCULADORA BÁSICA")
print("=" * 20)

num1 = int(input("Primer número: "))
num2 = int(input("Segundo número: "))

print(f"Suma: {num1 + num2}")
print(f"Resta: {num1 - num2}")
print(f"Multiplicación: {num1 * num2}")
print(f"División: {num1 / num2}")
```

**Explicación:**
- Solicita dos números al usuario
- Realiza las cuatro operaciones básicas
- Muestra los resultados usando f-strings
- Demuestra operaciones matemáticas básicas

## 3. Repetir Nombre

```python
print("Dame tu nombre de usuario")
usuario = input()
numero = input("Introduce un número entero: ")
print((usuario + "\n") * int(numero))
```

**Explicación:**
- Solicita nombre de usuario y un número
- Usa `\n` para saltos de línea
- Multiplica el string por el número para repetirlo
- Demuestra manipulación básica de strings

## 4. Análisis de Nombre

```python
nombre = input("Introduce tu nombre: ")
print(f"{nombre.upper()} tiene {len(nombre)} letras")
```

**Explicación:**
- Solicita un nombre al usuario
- Usa `upper()` para convertir a mayúsculas
- `len()` para contar caracteres
- Combina manipulación de strings con f-strings

### Conceptos Importantes:

1. **Entrada de datos:**
   - `input()`: Lee entrada del usuario
   - Siempre devuelve un string
   - Necesita conversión para otros tipos de datos

2. **Conversión de tipos:**
   - `int()`: Convierte a entero
   - Importante para operaciones matemáticas
   - Puede generar error si la entrada no es válida

3. **Formateo de strings:**
   - f-strings: `f"texto {variable}"`
   - Permiten incrustar expresiones
   - Más legible que otros métodos de formateo

4. **Manipulación de strings:**
   - Concatenación con `+`
   - Multiplicación con `*`
   - Métodos como `upper()` y `len()`

### Buenas Prácticas:

1. **Validación de entrada:**
   - Siempre validar entrada numérica
   - Manejar posibles errores
   - Proporcionar mensajes claros al usuario

2. **Claridad en mensajes:**
   - Instrucciones claras
   - Feedback apropiado
   - Formato consistente

3. **Estructura del código:**
   - Separar diferentes funcionalidades
   - Usar comentarios descriptivos
   - Mantener consistencia en el estilo

