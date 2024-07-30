#Automotriz
#El Rey de los SportsCar
class Car:
    def __init__(self, brand, model, year, max_speed, price):
        self.brand = brand  # Marca del automóvil
        self.model = model  # Modelo del automóvil
        self.year = year  # Año del automóvil
        self.max_speed = max_speed  # Velocidad máxima del automóvil
        self.price = price  # Precio del automóvil
        self.available = True  # Estado de disponibilidad del automóvil, inicialmente disponible
    
    def sell(self):  # Método para vender el automóvil
        if self.available:  # Verifica si el automóvil está disponible
            self.available = False  # Marca el automóvil como no disponible
            print(f"El automóvil {self.brand} {self.model} ha sido vendido")  # Mensaje de confirmación
        else:
            print(f"El automóvil {self.brand} {self.model} no está disponible")  # Mensaje si no está disponible

    def return_car(self):  # Método para devolver el automóvil
        self.available = True  # Marca el automóvil como disponible
        print(f"El automóvil {self.brand} {self.model} ha sido devuelto")  # Mensaje de confirmación

class Customer:
    def __init__(self, name, customer_id):  # Inicializa al cliente con nombre e ID
        self.name = name  # Nombre del cliente
        self.customer_id = customer_id  # ID del cliente

    def buy_car(self, car):  # Método para que el cliente compre un automóvil
        if car.available:  # Verifica si el automóvil está disponible
            car.sell()  # Llama al método sell del automóvil para marcarlo como vendido
            print(f"{self.name} ha comprado el automóvil {car.brand} {car.model}")  # Mensaje de confirmación
        else:
            print(f"El automóvil {car.brand} {car.model} no está disponible para la compra")  # Mensaje si el automóvil no está disponible

    def return_car(self, car):  # Método para que el cliente devuelva un automóvil
        car.return_car()  # Llama al método return_car del automóvil para marcarlo como devuelto
        print(f"{self.name} ha devuelto el automóvil {car.brand} {car.model}")  # Mensaje de confirmación

class Dealership:
    def __init__(self):  # Inicializa la concesionaria
        self.cars = []  # Lista para almacenar los automóviles en la concesionaria
        self.customers = []  # Lista para almacenar los clientes registrados

    def add_car(self, car):  # Método para agregar un automóvil a la concesionaria
        self.cars.append(car)  # Agrega el automóvil a la lista de automóviles
        print(f"El automóvil {car.brand} {car.model} ha sido agregado al catálogo")  # Mensaje de confirmación

    def register_customer(self, customer):  # Método para registrar un cliente en la concesionaria
        self.customers.append(customer)  # Agrega el cliente a la lista de clientes
        print(f"El cliente {customer.name} ha sido registrado")  # Mensaje de confirmación

    def show_available_cars(self):  # Método para mostrar los automóviles disponibles en la concesionaria
        print("Automóviles disponibles:")  # Encabezado para la lista de automóviles
        for car in self.cars:  # Recorre todos los automóviles en la concesionaria
            if car.available:  # Verifica si el automóvil está disponible
                print(f"{car.brand} {car.model} ({car.year}) - Vel. Max: {car.max_speed} km/h - Precio: ${car.price}")  # Muestra la información del automóvil

    def welcome_message(self):  # Método para mostrar un mensaje de bienvenida
        print("*********************************************************")
        print("* Bienvenido a Concesionaria El Rey de los Sportscars! *")  # Mensaje de bienvenida
        print("*********************************************************") 

# Crear los automóviles
car1 = Car("Koenigsegg", "Jesko Absolut", 2024, "500 K/H", "$3,500,000.00 Dlls")  # Crea el primer automóvil
car2 = Car("SSC", "Tuatara", 2024, "474 K/h", "2,800,000.00 Dlls")  # Crea el segundo automóvil
car3 = Car("Bugatti", "Tourbillio", 2024, "445 K/H", "$4,200,000.00 Dlls")  # Crea el tercer automóvil
car4 = Car("Hennessey", "Venom F5", 2024, "435 K/H", "$3,200,000.00 Dlls")  # Crea el cuarto automóvil
car5 = Car("Rimac", "Nevera", 2024, "410 K/H", "$2,700,000.00 Dlls")  # Crea el quinto automóvil

# Crear cliente
customer1 = Customer("Alice", "001")  # Crea un nuevo cliente

# Crear concesionaria
dealership = Dealership()  # Crea una nueva concesionaria
dealership.welcome_message()  # Muestra el mensaje de bienvenida
dealership.add_car(car1)  # Agrega el primer automóvil al catálogo
dealership.add_car(car2)  # Agrega el segundo automóvil al catálogo
dealership.add_car(car3)  # Agrega el tercer automóvil al catálogo
dealership.add_car(car4)  # Agrega el cuarto automóvil al catálogo
dealership.add_car(car5)  # Agrega el quinto automóvil al catálogo
dealership.register_customer(customer1)  # Registra el cliente en la concesionaria

# Mostrar automóviles disponibles
dealership.show_available_cars()  # Muestra todos los automóviles disponibles en la concesionaria

# Realizar compra
customer1.buy_car(car1)  # El cliente compra el primer automóvil

# Mostrar automóviles disponibles después de la compra
dealership.show_available_cars()  # Muestra los automóviles disponibles después de la compra

# Devolver automóvil
customer1.return_car(car1)  # El cliente devuelve el primer automóvil

# Mostrar automóviles disponibles después de la devolución
dealership.show_available_cars()  # Muestra los automóviles disponibles después de la devolución
