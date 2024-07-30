# POO - Programación Orientada a Objetos
# Objeto: Instancia de una clase que contiene datos y comportamientos específicos.
# Clase: Plantilla que define las propiedades (atributos) y comportamientos (métodos) de los objetos.
# Atributo: Variable dentro de una clase que almacena información sobre el objeto.
# Método: Función definida dentro de una clase que describe las acciones que un objeto puede realizar.
# Constructor: Método especial en una clase (__init__) que se llama automáticamente al crear un nuevo objeto para inicializar sus atributos.
# Parámetro: Variable en una función o método que recibe un valor al ser llamada para usar dentro de esa función o método.


#Ejercicios POO
class Person:                       # Definimos una nueva clase, una buena practica es utilizar mayuscalas al principio aqui
    def __init__(self,name,age):    # Es una funcion particular que define el costructor, Self es para que se llame a el mismo 
        self.name = name            # Al nuevo objeto "Person" , le da el atributo de que tiene "name"(nombre) y aqui se lo asigna
        self.age = age              # Lo mismo pero con "age" (edad)
# El constructor ya asigno nuevos atributos al objeto o clase de los parametros "name" y "age"
    def greet(self):                # Creamos / definimso una funcion para saludar
        #print(f"Hola,mi nombre es {self.name} y tengo {self.age}")
        print("Hola, mi nombre es", self.name, "y tengo", self.age)

person1 = Person("Ana",33)
person2 = Person("Luis",25)

person1.greet()
person2.greet()


