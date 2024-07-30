from typing import Any
# Libreria
# En esta clase vamos a crear una libreria

class Book:
    def __init__(self, title, author):  # Inicializa el libro con título y autor
        self.title = title  # Asigna el título del libro
        self.author = author  # Asigna el autor del libro
        self.available = True  # Marca el libro como disponible inicialmente
    
    def borrow(self):  # Método para prestar el libro
        if self.available:  # Verifica si el libro está disponible
            self.available = False  # Marca el libro como no disponible
            print(f"El libro {self.title} ha sido prestado")  # Mensaje de confirmación
        else:
            print(f"El libro {self.title} no está disponible")  # Mensaje si no está disponible

    def return_book(self):  # Método para devolver el libro
        self.available = True  # Marca el libro como disponible
        print(f"El libro {self.title} ha sido devuelto")  # Mensaje de confirmación

class User:
    def __init__(self, name, user_id):  # Inicializa al usuario con nombre e ID
        self.name = name  # Asigna el nombre del usuario
        self.user_id = user_id  # Asigna el ID del usuario
        self.borrowed_books = []  # Lista para almacenar los libros prestados por el usuario

    def borrow_book(self, book):  # Método para que el usuario tome prestado un libro
        if book.available:  # Verifica si el libro está disponible
            book.borrow()  # Llama al método borrow del libro para marcarlo como prestado
            self.borrowed_books.append(book)  # Agrega el libro a la lista de prestados
        else:
            print(f"El libro {book.title} no está disponible")  # Mensaje si el libro no está disponible

    def return_book(self, book):  # Método para que el usuario devuelva un libro
        if book in self.borrowed_books:  # Verifica si el libro está en la lista de prestados
            book.return_book()  # Llama al método return_book del libro para marcarlo como devuelto
            self.borrowed_books.remove(book)  # Remueve el libro de la lista de prestados
        else:
            print(f"El libro {book.title} no está en la lista de prestados")  # Mensaje si el libro no está en la lista

class Library:
    def __init__(self):  # Inicializa la biblioteca
        self.books = []  # Lista para almacenar los libros de la biblioteca
        self.users = []  # Lista para almacenar los usuarios registrados

    def add_book(self, book):  # Método para agregar un libro a la biblioteca
        self.books.append(book)  # Agrega el libro a la lista de libros
        print(f"El libro {book.title} ha sido agregado")  # Mensaje de confirmación

    def register_user(self, user):  # Método para registrar un usuario en la biblioteca
        self.users.append(user)  # Agrega el usuario a la lista de usuarios
        print(f"El usuario {user.name} ha sido registrado")  # Mensaje de confirmación

    def show_available_books(self):  # Método para mostrar los libros disponibles en la biblioteca
        print("Libros disponibles:")  # Encabezado para la lista de libros
        for book in self.books:  # Recorre todos los libros en la biblioteca
            if book.available:  # Verifica si el libro está disponible
                print(f"{book.title} por {book.author}")  # Muestra el título y autor del libro

# Crear los libros
book1 = Book("El Señor de los Anillos: La Comunidad del Anillo", "J. R. R. Tolkien")  # Crea el primer libro
book2 = Book("El Señor de los Anillos: Las Dos Torres", "J. R. R. Tolkien")  # Crea el segundo libro
book3 = Book("El Señor de los Anillos: El Retorno del Rey", "J. R. R. Tolkien")  # Crea el tercer libro

# Crear usuario
user1 = User("Varo", "007")  # Crea un nuevo usuario

# Crear Biblioteca
library = Library()  # Crea una nueva biblioteca
library.add_book(book1)  # Agrega el primer libro a la biblioteca
library.add_book(book2)  # Agrega el segundo libro a la biblioteca
library.add_book(book3)  # Agrega el tercer libro a la biblioteca
library.register_user(user1)  # Registra el usuario en la biblioteca

# Mostrar libros disponibles
library.show_available_books()  # Muestra todos los libros disponibles en la biblioteca

# Realizar préstamo
user1.borrow_book(book1)  # El usuario toma prestado el primer libro

# Mostrar libros disponibles después del préstamo
library.show_available_books()  # Muestra los libros disponibles después del préstamo

# Devolver libro
user1.return_book(book1)  # El usuario devuelve el primer libro

# Mostrar libros disponibles después de la devolución
library.show_available_books()  # Muestra los libros disponibles después de la devolución
