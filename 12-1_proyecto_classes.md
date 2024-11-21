# Sistema de Biblioteca en Python - Guía Paso a Paso 📚

## 1. Clase Book (Libro)
Esta clase representa un libro individual en nuestra biblioteca.

### Atributos
```python
def __init__(self, title, author):
    self.title = title            # Título del libro
    self.author = author          # Autor del libro
    self.__is_borrowed = False    # Estado del préstamo
```
**Explicación:** 
- Es como crear una ficha para cada libro
- `title` y `author` son públicos (cualquiera puede verlos)
- `__is_borrowed` es privado (solo el libro sabe si está prestado)

### Métodos del Libro
```python
def borrow(self):
    if self.__is_borrowed:
        return False
    self.__is_borrowed = True
    return True
```
**Explicación:**
- `borrow()`: Intenta prestar el libro
  - Si ya está prestado → devuelve False
  - Si está disponible → lo marca como prestado y devuelve True

```python
def __str__(self):
    status = "Prestado" if self.__is_borrowed else "Disponible"
    return f"'{self.title}' por {self.author} ({status})"
```
**Explicación:**
- `__str__`: Define cómo se muestra el libro cuando lo imprimimos
- Como decir "Este libro es [título] escrito por [autor] y está [estado]"

## 2. Clase Library (Biblioteca)
Esta clase maneja la colección de libros.

### Atributos
```python
def __init__(self):
    self.books = []  # Lista de libros
```
**Explicación:**
- Como un estante vacío listo para poner libros

### Métodos de la Biblioteca
```python
def add_book(self, book):
    self.books.append(book)
```
**Explicación:**
- Agrega un nuevo libro al estante

```python
def show_books(self):
    if not self.books:
        print("La biblioteca está vacía.")
        return
    print("\nLibros en la biblioteca:")
    for index, book in enumerate(self.books, start=1):
        print(f"{index}. {book}")
```
**Explicación:**
- Muestra todos los libros en el estante
- Si no hay libros, dice que está vacía
- Numera los libros para fácil referencia

## 3. Uso del Sistema

### Crear la Biblioteca
```python
my_library = Library()  # Crear una biblioteca vacía
```

### Agregar Libros
```python
book1 = Book("Cien Años de Soledad", "Gabriel García Márquez")
my_library.add_book(book1)
```
**Explicación:**
- Primero creamos un libro nuevo
- Luego lo agregamos a la biblioteca

### Prestar y Devolver
```python
my_library.borrow_book("El Principito")
my_library.return_book("El Principito")
```
**Explicación:**
- `borrow_book`: Marca un libro como prestado
- `return_book`: Marca un libro como devuelto

## 4. Características Importantes 🎯

1. **Encapsulación**
   - Los libros manejan su propio estado de préstamo
   - La biblioteca no puede cambiar directamente si un libro está prestado

2. **Organización**
   - Cada clase tiene una responsabilidad clara
   - La biblioteca maneja la colección
   - Cada libro maneja su propia información

3. **Facilidad de Uso**
   - Interfaz simple para prestar y devolver
   - Fácil visualización de los libros disponibles

## 5. Ejemplo de Ejecución 🚀
```python
biblioteca = Library()
libro = Book("Harry Potter", "J.K. Rowling")
biblioteca.add_book(libro)
biblioteca.show_books()
biblioteca.borrow_book("Harry Potter")
biblioteca.show_books()
```

Este sistema simula una biblioteca real donde puedes:
- Agregar nuevos libros
- Ver qué libros hay disponibles
- Prestar libros
- Devolver libros
- Ver el estado de cada libro

¡Ahora puedes gestionar tu propia biblioteca virtual! 📚✨