### Ejemplos de Clases ###

# Definición de una clase vacía
class MyEmptyAnimal:
    pass  # Permite dejar la clase sin contenido por ahora


print(MyEmptyAnimal)  # Muestra información sobre la clase
print(MyEmptyAnimal())  # Crea una instancia de la clase

# Clase con constructor, métodos y propiedades públicas y privadas

class Animal:
    def __init__(self, species, sound, age=0):
        self.species = species  # Propiedad pública
        self.__sound = sound  # Propiedad privada
        self.age = age  # Propiedad pública con valor predeterminado

    def make_sound(self):
        # Método público que utiliza una propiedad privada
        print(f"El {self.species} hace '{self.__sound}'")

    def get_sound(self):
        # Método para acceder a la propiedad privada
        return self.__sound

    def grow_older(self):
        # Incrementa la edad del animal
        self.age += 1
        print(f"El {self.species} ahora tiene {self.age} años")


# Crear instancias de la clase Animal
my_animal = Animal("Perro", "Guau")
print(f"Especie: {my_animal.species}")  # Accede a una propiedad pública
my_animal.make_sound()  # Llama al método para hacer un sonido
my_animal.grow_older()  # Incrementa la edad
print(f"Edad: {my_animal.age}")  # Muestra la edad actual

my_other_animal = Animal("Gato", "Miau", age=3)  # Especificamos la edad inicial
print(f"Especie: {my_other_animal.species}")
print(f"Sonido: {my_other_animal.get_sound()}")  # Utiliza un método para acceder a la propiedad privada
my_other_animal.make_sound()

# Modificar una propiedad pública directamente
my_other_animal.age = 5
print(f"El gato ahora tiene {my_other_animal.age} años")

# Intentar acceder a una propiedad privada directamente (esto causará un error)
# print(my_other_animal.__sound)  # Descomenta para ver el error

# Clase con una propiedad protegida y métodos adicionales

class Vehicle:
    def __init__(self, brand, model, speed=0):
        self.brand = brand  # Propiedad pública
        self._model = model  # Propiedad protegida (convención)
        self.__speed = speed  # Propiedad privada

    def accelerate(self, increment):
        # Método para incrementar la velocidad
        self.__speed += increment
        print(f"El {self.brand} {self._model} ahora va a {self.__speed} km/h")

    def brake(self):
        # Método para detener el vehículo
        self.__speed = 0
        print(f"El {self.brand} {self._model} se ha detenido")

    def get_speed(self):
        # Método para obtener la velocidad actual
        return self.__speed


# Crear una instancia de Vehicle
my_vehicle = Vehicle("Toyota", "Corolla")
print(f"Vehículo: {my_vehicle.brand} {my_vehicle._model}")  # Accede a las propiedades públicas y protegidas
my_vehicle.accelerate(60)  # Incrementa la velocidad
print(f"Velocidad actual: {my_vehicle.get_speed()} km/h")  # Obtiene la velocidad actual
my_vehicle.brake()  # Detiene el vehículo

# Crear otro vehículo
my_other_vehicle = Vehicle("Tesla", "Model S", speed=20)
print(f"Vehículo: {my_other_vehicle.brand} {my_other_vehicle._model}")
print(f"Velocidad inicial: {my_other_vehicle.get_speed()} km/h")
my_other_vehicle.accelerate(40)
