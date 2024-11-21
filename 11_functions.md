# Funciones en Python - Explicación 🚀

## ¿Qué es una Función? 🤔
Imagina que una función es como una receta de cocina: tomas algunos ingredientes (datos), sigues unos pasos (instrucciones) y obtienes un resultado (como un pastel). ¡Así funcionan las funciones en programación!

## Tipos de Funciones

### 1. Función Simple (La más básica)
```python
def saludar():
    print("¡Hola! ¿Qué tal?")

saludar()  # Esto muestra: ¡Hola! ¿Qué tal?
```
**Explicación:** Es como tener un botón que siempre hace lo mismo cuando lo presionas. Cuando escribes `saludar()`, le dices a Python "¡Hey, ejecuta esto!"

### 2. Función con Parámetros (Con ingredientes)
```python
def sumar_numeros(numero1, numero2):
    return numero1 + numero2

resultado = sumar_numeros(5, 3)  # resultado será 8
```
**Explicación:** Es como una máquina de jugos: le pones dos frutas (parámetros) y te da un jugo mezclado (resultado). Los parámetros son como los ingredientes que necesitas para que la función haga su trabajo.

### 3. Funciones con Valores por Defecto
```python
def saludar_persona(nombre="amigo"):
    print(f"¡Hola, {nombre}!")

saludar_persona()  # Muestra: ¡Hola, amigo!
saludar_persona("Ana")  # Muestra: ¡Hola, Ana!
```
**Explicación:** Es como cuando preparan un sandwich: si no dices qué ingredientes quieres, usan los básicos, pero si pides ingredientes específicos, usan esos.

### 4. Funciones que Devuelven Valores
```python
def calcular_edad_perro(edad_humana):
    edad_perro = edad_humana * 7
    return edad_perro

edad = calcular_edad_perro(2)  # edad será 14
```
**Explicación:** Es como una máquina de cambio: le das dinero (entrada) y te devuelve otras monedas (salida). El `return` es como decir "aquí está tu resultado".

### 5. Funciones con Múltiples Parámetros
```python
def crear_presentacion(nombre, edad, hobby):
    print(f"Me llamo {nombre}, tengo {edad} años y me gusta {hobby}")

crear_presentacion("Luis", 14, "jugar videojuegos")
```
**Explicación:** Como cuando te presentas a alguien nuevo: necesitas varios datos (nombre, edad, hobby) para hacer una presentación completa.

## Tipos de Datos que Puedes Usar 🎮

### Números
```python
def duplicar(numero: int):
    return numero * 2
```
**Explicación:** `int` es para números enteros, como 1, 2, 3. Es como contar sin usar decimales.

### Texto
```python
def gritar(texto: str):
    return texto.upper()
```
**Explicación:** `str` es para texto, como nombres o frases. Cualquier cosa entre comillas.

### Listas
```python
def primer_elemento(lista: list):
    return lista[0]
```
**Explicación:** Las listas son como una playlist de música: una colección de cosas en orden.

## Consejos Útiles 💡

1. **Nombres Claros**
```python
# Bien
def calcular_promedio(notas):
    return sum(notas) / len(notas)

# No tan bien
def calc(n):
    return sum(n) / len(n)
```
**Explicación:** El nombre de una función debe explicar claramente lo que hace, como poner etiquetas claras en cajas de almacenamiento.

2. **Comentarios Útiles**
```python
def calcular_nota_final(examen, trabajos):
    """
    Calcula la nota final del curso
    examen vale 60% y trabajos 40%
    """
    return (examen * 0.6) + (trabajos * 0.4)
```
**Explicación:** Los comentarios son como instrucciones que explican cómo funciona algo, igual que el manual de un juego.

3. **Validación**
```python
def dividir(a, b):
    if b == 0:
        return "¡No puedes dividir por cero!"
    return a / b
```
**Explicación:** Es como revisar que tienes todos los ingredientes antes de empezar a cocinar. ¡Siempre es bueno verificar!

## Ejemplos Prácticos 🎮

### Juego simple
```python
def adivinar_numero(intento: int) -> str:
    numero_secreto = 7
    if intento == numero_secreto:
        return "¡Ganaste! 🎉"
    return "Intenta otra vez 😉"
```
**Explicación:** Como un juego de adivinar: la función comprueba si adivinaste el número secreto.

### Calculadora de Puntos
```python
def calcular_puntos(enemigos: int, monedas: int) -> int:
    return (enemigos * 100) + (monedas * 10)
```
**Explicación:** Como calcular un puntaje en un juego: cada enemigo vale 100 puntos y cada moneda 10.

Recuerda: ¡Las funciones son como pequeños ayudantes que hacen tareas por ti! Cuanto más las uses, más fácil será programar cosas interesantes. 🤖✨