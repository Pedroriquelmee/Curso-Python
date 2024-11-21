# Clases en Python - Explicación Simple 🏗️

## ¿Qué es una Clase?
Una clase es como un plano o molde para crear objetos. Imagina que es como un molde para galletas: el molde es la clase, y las galletas son los objetos.

## 1. Clase Vacía
```python
class MyEmptyAnimal:
    pass
```
**Explicación:** Es como tener una caja vacía. No hace nada pero está lista para usar después. Es útil cuando estás planificando algo.

## 2. Clase Animal
```python
class Animal:
    def __init__(self, species, sound, age=0):
        self.species = species       # Público (todos pueden ver)
        self.__sound = sound        # Privado (solo la clase puede ver)
        self.age = age             # Público con valor inicial
```
**Explicación:** 
- Es como crear una ficha para un animal con:
  - Especie (como "perro" o "gato")
  - Sonido (su forma de comunicarse)
  - Edad (que empieza en 0 si no dices otra cosa)

Sí, añado la definición de propiedad protegida manteniendo el contenido original:

## Definiciones Importantes

### Constructor (__init__)
Es un método especial que se ejecuta automáticamente cuando creamos un nuevo objeto de la clase. Es como el "nacimiento" del objeto, donde se establecen sus características iniciales.

### Métodos
Son las funciones que pertenecen a una clase. Definen qué acciones puede realizar un objeto de esa clase.

### Propiedades Públicas
Son variables que pertenecen a la clase y pueden ser accedidas desde cualquier parte del código. Se definen sin guiones bajos.
```python
self.nombre = nombre
```

### Propiedades Privadas
Son variables que solo pueden ser accedidas desde dentro de la clase. Se definen con doble guion bajo.
```python
self.__secreto = valor
```

### Propiedades Protegidas
Son variables que se indican que deberían ser tratadas como internas y no accedidas desde fuera de la clase, aunque técnicamente se puede. Se definen con un solo guion bajo.
```python
self._valor = valor
```

### Self
Es una referencia al propio objeto que se está manipulando. Es como el "yo" del objeto y se usa para acceder a sus propiedades y métodos.

[Resto del contenido original se mantiene igual...]

### Métodos de la Clase Animal
```python
def make_sound(self):
    print(f"El {self.species} hace '{self.__sound}'")

def grow_older(self):
    self.age += 1
    print(f"El {self.species} ahora tiene {self.age} años")
```
**Explicación:**
- `make_sound`: Hace que el animal emita su sonido
- `grow_older`: Aumenta la edad del animal en 1 año

## 3. Usando la Clase Animal
```python
my_animal = Animal("Perro", "Guau")
my_animal.make_sound()      # El Perro hace 'Guau'
my_animal.grow_older()      # El Perro ahora tiene 1 años
```
**Explicación:** Es como crear un animal real usando nuestro molde. Podemos hacerlo hacer sonidos y envejecer.

## 4. Clase Vehicle
```python
class Vehicle:
    def __init__(self, brand, model, speed=0):
        self.brand = brand          # Público
        self._model = model         # Protegido
        self.__speed = speed        # Privado
```
**Explicación:** 
- Como una ficha de un vehículo con:
  - Marca (como "Toyota")
  - Modelo (como "Corolla")
  - Velocidad (empieza en 0)

### Métodos de Vehicle
```python
def accelerate(self, increment):
    self.__speed += increment
    print(f"El {self.brand} {self._model} ahora va a {self.__speed} km/h")

def brake(self):
    self.__speed = 0
    print(f"El {self.brand} {self._model} se ha detenido")
```
**Explicación:**
- `accelerate`: Hace que el vehículo vaya más rápido
- `brake`: Detiene el vehículo completamente

## Tipos de Propiedades 🔒

1. **Públicas** (normal)
   ```python
   self.species = species
   ```
   **Explicación:** Todos pueden ver y cambiar esto

2. **Protegidas** (con un _)
   ```python
   self._model = model
   ```
   **Explicación:** Es como decir "mejor no toques esto"

3. **Privadas** (con __)
   ```python
   self.__sound = sound
   ```
   **Explicación:** Solo la clase puede usar esto

## Ejemplo Práctico 🚗
```python
# Crear un coche
my_car = Vehicle("Toyota", "Corolla")
my_car.accelerate(60)  # Acelera a 60 km/h
my_car.brake()         # Se detiene
```

## Tips Importantes 💡
1. Las clases son como moldes para crear objetos
2. `__init__` es donde preparas todo al crear un objeto
3. Las propiedades privadas (`__`) son más seguras
4. Los métodos son las acciones que puede hacer un objeto

¡Ahora ya sabes cómo crear tus propias clases! 🌟