# Clase base o Superclase para vehículos
class Vehicle:
    def __init__(self, brand, model, year, max_speed, price):
        self.brand = brand  # Marca del vehículo
        self.model = model  # Modelo del vehículo
        self.year = year  # Año del vehículo
        self.max_speed = max_speed  # Velocidad máxima del vehículo
        self.price = price  # Precio del vehículo
        self.available = True  # Estado de disponibilidad del vehículo, inicialmente disponible
    
    def sell(self):  # Método para vender el vehículo
        if self.available:  # Verifica si el vehículo está disponible
            self.available = False  # Marca el vehículo como no disponible
            print(f"El vehículo {self.brand} {self.model} ha sido vendido")
        else:
            print(f"El vehículo {self.brand} {self.model} no está disponible")
    
    def check_avaliable(self):  # Método para devolver el vehículo
        self.available = True  # Marca el vehículo como disponible
        print(f"El vehículo {self.brand} {self.model} ha sido devuelto")

    def get_price(self):  # Método para obtener el precio del vehículo
        return self.price
    
    def start_engine(self):  # Método abstracto para encender el motor (debe ser implementado por las subclases)
        raise NotImplementedError("Este método debe ser implementado por la Subclase")
    
    def stop_engine(self):  # Método abstracto para apagar el motor (debe ser implementado por las subclases)
        raise NotImplementedError("Este método debe ser implementado por la Subclase")

# Subclase para automóviles
class Car(Vehicle):
    def start_engine(self):
        if not self.available:
            return f"El motor del {self.brand} {self.model} está en marcha"
        else:
            return f"El carro {self.brand} {self.model} no está disponible"

    def stop_engine(self):
        if self.available:
            return f"El motor del {self.brand} {self.model} se ha detenido"
        else:
            return f"El carro {self.brand} {self.model} no está disponible"

# Subclase para motocicletas
class MotorBike(Vehicle):
    def start_engine(self):
        if not self.available:
            return f"El motor de la {self.brand} {self.model} está en marcha"
        else:
            return f"La moto {self.brand} {self.model} no está disponible"

    def stop_engine(self):
        if self.available:
            return f"El motor de la {self.brand} {self.model} se ha detenido"
        else:
            return f"La moto {self.brand} {self.model} no está disponible"

# Subclase para vehículos eléctricos
class Electrics(Vehicle):
    def start_engine(self):
        if not self.available:
            return f"El motor del {self.brand} {self.model} está en marcha"
        else:
            return f"El vehículo eléctrico {self.brand} {self.model} no está disponible"

    def stop_engine(self):
        if self.available:
            return f"El motor del {self.brand} {self.model} se ha detenido"
        else:
            return f"El vehículo eléctrico {self.brand} {self.model} no está disponible"

class Customer:
    def __init__(self, name, customer_id):  # Inicializa al cliente con nombre e ID
        self.name = name  # Nombre del cliente
        self.customer_id = customer_id  # ID del cliente
        self.puchased=[]

    def buy_vehicle(self, vehicle : Vehicle):  # Método para que el cliente compre un automóvil
        if Vehicle.available:  # Verifica si el automóvil está disponible
            Vehicle.sell()  # Llama al método sell del automóvil para marcarlo como vendido
            print(f"{self.name} ha comprado el  vehiculo {vehicle.brand} {vehicle.model}")  # Mensaje de confirmación
            self.puchased.append(vehicle)
        else:
            print(f"El automóvil {vehicle.brand} {vehicle.model} no está disponible para la compra")  # Mensaje si el automóvil no está disponible

    def consulta(self, vehicle:Vehicle):  # Método para que el cliente devuelva un automóvil
        if vehicle.available():
            availability = "Disponible"
        else:
            availability = "No Disponible"
        print(f"El automóvil {vehicle.brand} está {availability} y tiene un preci de {vehicle.get_price()}")  # Mensaje si el automóvil no está disponible

class Dealership:
    def __init__(self):  # Inicializa la concesionaria
        self.inventory = []  # Lista para almacenar los automóviles en la concesionaria
        self.customers = []  # Lista para almacenar los clientes registrados

    def add_vehicle(self, vehicle:Vehicle):  # Método para agregar un automóvil a la concesionaria
        self.inventory.append(vehicle)  # Agrega el automóvil a la lista de automóviles
        print(f"El vehiculo {vehicle.brand} {vehicle.model} ha sido agregado al catálogo")  # Mensaje de confirmación

    def register_customer(self, customer:Customer):  # Método para registrar un cliente en la concesionaria
        self.customers.append(customer)  # Agrega el cliente a la lista de clientes
        print(f"El cliente {customer.name} ha sido registrado")  # Mensaje de confirmación

    def show_available_vehicles(self):  # Método para mostrar los automóviles disponibles en la concesionaria
        print("Vehiculos disponibles:")  # Encabezado para la lista de automóviles
        for vehicle in self.inventory:  # Recorre todos los automóviles en la concesionaria
            if vehicle.check_avaliable():  # Verifica si el automóvil está disponible
                print(f"{vehicle.brand}  {vehicle.model} ({vehicle.year}) - Vel. Max: {vehicle.max_speed} - Precio: ${vehicle.price}")  # Muestra la información del automóvil



# Ejemplo de uso
car1 = Car("Koenigsegg", "Jesko Absolut", 2024, "500 K/H", "$3,500,000.00 Dlls")  # Crea el primer automóvil
car2 = Car("SSC", "Tuatara", 2024, "474 K/h", "2,800,000.00 Dlls")  # Crea el segundo automóvil
car3 = Car("Bugatti", "Tourbillio", 2024, "445 K/H", "$4,200,000.00 Dlls")  # Crea el tercer automóvil
car4 = Car("Hennessey", "Venom F5", 2024, "435 K/H", "$3,200,000.00 Dlls")  # Crea el cuarto automóvil
car5 = Car("Rimac", "Nevera", 2024, "410 K/H", "$2,700,000.00 Dlls")  # Crea el quinto automóvil
motorbike1 = MotorBike("Dodge", "Tomahawk", 2024, "675 K/H", "$700,000.00 Dlls")
motorbike2 = MotorBike("MTT", "Turbine Superbike Y2K", 2024, "365 K/H", "$550,000.00 Dlls")
motorbike3 = MotorBike("Kawasaki", "Ninja H2R", 2024, "355 K/H", "$400,000.00 Dlls")
electric1 = Electrics("Tesla", "Roadster", 2024, "402 K/H", "$2,700,000.00 Dlls")
electric2 = Electrics("Audi", "e-Tron GT", 2024, "322 K/H", "$3,200,000.00 Dlls")
electric3 = Electrics("Lucid", "Sir Dream Edition", 2024, "290 K/H", "$2,000,000.00 Dlls")

print(car1.start_engine())
car1.sell()
car2.sell()
motorbike1.sell()
electric1.sell()
print(car1.start_engine())
print(car1.stop_engine())

car6 = Car("Rimac", "Nevera", 2024, "410 K/H", "$2,700,000.00 Dlls")  # Crea el quinto automóvil
motorbike4 = MotorBike("Dodge", "Tomahawk", 2024, "675 K/H", "$700,000.00 Dlls")
electric4 = Electrics("Tesla", "Roadster", 2024, "402 K/H", "$2,700,000.00 Dlls")

dealership = Dealership()
dealership.add_vehicle(car6)
dealership.add_vehicle(motorbike4)
dealership.add_vehicle(electric4)
dealership.show_available_vehicles()