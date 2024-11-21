# Clase Libro
class Book:
    def __init__(self, title, author):
        """
        Constructor de la clase Book.
        :param title: Título del libro.
        :param author: Autor del libro.
        """
        self.title = title  # Propiedad pública: título del libro
        self.author = author  # Propiedad pública: autor del libro
        self.__is_borrowed = False  # Propiedad privada: indica si el libro está prestado

    def borrow(self):
        """
        Método para prestar el libro.
        Retorna True si se prestó exitosamente, False si ya está prestado.
        """
        if self.__is_borrowed:
            return False
        self.__is_borrowed = True
        return True

    def return_book(self):
        """
        Método para devolver el libro.
        """
        self.__is_borrowed = False

    def is_borrowed(self):
        """
        Método para verificar si el libro está prestado.
        """
        return self.__is_borrowed

    def __str__(self):
        """
        Representación en string del libro.
        """
        status = "Prestado" if self.__is_borrowed else "Disponible"
        return f"'{self.title}' por {self.author} ({status})"


# Clase Biblioteca
class Library:
    def __init__(self):
        """
        Constructor de la clase Library.
        Inicializa una lista vacía de libros.
        """
        self.books = []  # Lista pública para almacenar los libros

    def add_book(self, book):
        """
        Método para agregar un libro a la biblioteca.
        :param book: Instancia de la clase Book.
        """
        self.books.append(book)
        print(f"Libro '{book.title}' agregado a la biblioteca.")

    def show_books(self):
        """
        Método para mostrar los libros disponibles en la biblioteca.
        """
        if not self.books:
            print("La biblioteca está vacía.")
            return
        print("\nLibros en la biblioteca:")
        for index, book in enumerate(self.books, start=1):
            print(f"{index}. {book}")

    def borrow_book(self, title):
        """
        Método para prestar un libro.
        :param title: Título del libro a prestar.
        """
        for book in self.books:
            if book.title == title:
                if book.borrow():
                    print(f"Has prestado el libro: '{title}'.")
                    return
                else:
                    print(f"El libro '{title}' ya está prestado.")
                    return
        print(f"No se encontró el libro con título: '{title}'.")

    def return_book(self, title):
        """
        Método para devolver un libro.
        :param title: Título del libro a devolver.
        """
        for book in self.books:
            if book.title == title:
                book.return_book()
                print(f"Has devuelto el libro: '{title}'.")
                return
        print(f"No se encontró el libro con título: '{title}'.")


# Ejecución del proyecto
if __name__ == "__main__":
    # Crear una instancia de la biblioteca
    my_library = Library()

    # Agregar libros a la biblioteca
    book1 = Book("Cien Años de Soledad", "Gabriel García Márquez")
    book2 = Book("Don Quijote de la Mancha", "Miguel de Cervantes")
    book3 = Book("El Principito", "Antoine de Saint-Exupéry")

    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.add_book(book3)

    # Mostrar libros
    my_library.show_books()

    # Prestar un libro
    my_library.borrow_book("El Principito")

    # Intentar prestar un libro que ya está prestado
    my_library.borrow_book("El Principito")

    # Devolver un libro
    my_library.return_book("El Principito")

    # Mostrar libros nuevamente
    my_library.show_books()
