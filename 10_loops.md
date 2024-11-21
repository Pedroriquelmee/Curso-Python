# Bucles (Loops) en Python - Guía Simple

Los bucles nos permiten repetir acciones varias veces. Hay dos tipos principales: `while` y `for`.

## Bucle While
Es como decir "mientras esto sea cierto, sigue haciéndolo".

```python
# Ejemplo básico de while
counter = 1
while counter <= 5:
    print(f"Contador actual: {counter}")
    counter += 1
```
**Explicación simple:** Es como contar del 1 al 5. En cada vuelta, muestra el número y suma 1.

## Break en While
`break` es como un botón de emergencia que detiene el bucle.

```python
counter = 0
while counter < 10:
    counter += 1
    if counter == 7:
        print("Bucle detenido en 7")
        break
    print(counter)
```
**Explicación simple:** Cuenta hasta 10, pero si llega a 7, se detiene.

## Bucle For
For es útil cuando quieres hacer algo con cada elemento de una colección.

### Con Listas
```python
names = ["Ana", "Luis", "Pedro", "Clara"]
for name in names:
    print(f"Hola, {name}")
```
**Explicación simple:** Saluda a cada persona de la lista.

### Con Tuplas
```python
ages = (25, 30, 35, 40)
for age in ages:
    print(f"Tienes {age} años")
```
**Explicación simple:** Muestra cada edad de la tupla.

### Con Conjuntos
```python
numbers_set = {10, 20, 30, 40}
for number in numbers_set:
    print(f"Número: {number}")
```
**Explicación simple:** Muestra cada número del conjunto.

### Con Diccionarios
```python
person = {"Nombre": "María", "Edad": 28, "Ciudad": "Madrid"}
for key, value in person.items():
    print(f"{key}: {value}")
```
**Explicación simple:** Muestra cada dato de la persona (como "Nombre: María").

## Continue
`continue` es como decir "salta esta vez y sigue con la siguiente".

```python
for key, value in person.items():
    if key == "Ciudad":
        continue
    print(f"{key}: {value}")
```
**Explicación simple:** Muestra todos los datos excepto la ciudad.

### Consejos Útiles:
1. `while` es mejor cuando no sabes cuántas veces necesitas repetir algo
2. `for` es mejor cuando quieres hacer algo con cada elemento de una colección
3. `break` detiene el bucle completamente
4. `continue` salta a la siguiente vuelta del bucle

### Cuándo Usar Cada Uno:
- Usa `while` cuando:
  * No sabes cuántas veces necesitas repetir algo
  * Quieres repetir hasta que algo sea verdadero

- Usa `for` cuando:
  * Quieres hacer algo con cada elemento de una lista
  * Sabes exactamente cuántas veces quieres repetir algo
