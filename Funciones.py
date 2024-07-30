# FUNCIONES
# en este codigo aprenderemos a usar funcione

def function1():                # Aquie definidmos la funcion
    print("Hola universo")      # Aqui decimos que va a hcer la funcion, en este caso solo es un mensje 

function1()                     # Aqui llamamos a la funcion y realiza lo que tiene dentro

def greet(name, last_name="No tiene apellido"):     # Aqui definimos la funcion y al poner comas decimso que tiene 2 variabkes depentientes  y si una no existe va a decir un mensaje
    print("Hola", name, last_name)                  # La tarea de la funcion es imprimir un mensaje y luego la variable name y despues last_name

greet("Evarsto", "Gomez")                           # se pone como el orden de las comas (name, last_name)
greet("Varo")                                       # Aqui solo existe  el name por lo tanto imprimira "No tiene apellido"
greet(last_name = "Gomez", name = "Evaristo")       # Aqui se especifican las variables a donde se asigna 

def add(a,b):                   # esta funciono solo asigna los valosres de a y b        
    return a+b                  # como resutado de la funcion devuelve la suma de a y b

def substract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

def calculator():
    while True:
        print("------------------------------------------------------------")
        print("------------------------------------------------------------")
        print("Seleccione una operación")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        option = input("Ingrese su opción (1,2,3,4,5): ")

        if option == "5": # en este if no se pone elif o else por el break
            print("Saliendo de la calculadora")
            break

        if option in ["1","2","3","4"]: #aqui decimso que si es cualquiers de esas 4 opciones pregunte por num1 y num2
            num1 = float(input("Ingrese el primer numero: "))       # Aqui si declaramos que se aun flotante por que el dato es introducido por el usuari
            num2 = float(input("Ingrese el segundo numero: "))      # Aqui si declaramos que se aun flotante por que el dato es introducido por el usuari

            if option == "1":
                print("La suma es:", add(num1, num2))
            elif option == "2":
                print("La resta es:", substract(num1, num2))
            elif option == "4":
                print("La división es:", divide(num1, num2))
            elif option == "3":
                print("La multiplicación es:", multiply(num1, num2))
        
        else:
            print("Opción no válida, por intenta de nuevo")

calculator()    

# NOTA CURIOSA
#En Python, no estás obligado a declarar el tipo de una variable porque Python 
# es un lenguaje de programación dinámico y de tipado fuerte. 
# Esto significa que el tipo de una variable se determina automáticamente en tiempo de ejecución, 
# y no necesitas especificarlo explícitamente cuando declaras la variable.


# FUNCIONES LAMBDA Y PROGRAMACION FUNCIONAL EN PYTHON
# lambda no cupa declar funciones
# es una forma de hacer funcones anonimas 
# Se utliza para funcon3es sencillas, lambda solo requeire parametros y la operacion requerida

variableL  = lambda a, b: a + b    # al utilizar lambda le estoy diciendo que variable existe y como se realizara la operacion 
print(variableL(10,4))             #Al llamar a la variable que tiene la funcion lambda las declaro como estan acomodadas y le asignara los valores
                            #Al imprimirlo me mostrara ya directamente el resultado
tresvar = lambda a, b, c: a * b * c
print(tresvar(80,5,2))

#Cuadrado de cada numero
numbers = range(11)         # Recordemos que range genera numeros y no especificamos inicio va de 0 al 11, en variable numbers
squared_numbers = list(map(lambda x: x**2, numbers))  # "map" sirve para alacenar los datos de x  en memoria pero no pueden ser accesado directamnte solo almacenados 
#vermap = map(lambda x: x**2, numbers)                # por eso que ocupamos "list", "list" va por ellos ala memria y los va sacando en forma de lista para leerlos
#print(vermap) # asi es como se veria si lo immprimo "<map object at 0x0000023E6E9F21D0>"
print("Cuadrados:", squared_numbers ) # se almacenana en la variable y esta ya puede ser leida


#Pares
even_numbers = list(filter(lambda x: x%2 == 0, numbers)) # con "filter" podemos seleccionar los elementos si cumplen cierta funcion
#verfiltro= filter(lambda x: x%2 == 0, numbers) # con ambda le decimos que para x siempre que dividamos entre 2 y que el RESTO sea 0
#print(verfiltro) # se ve asi <filter object at 0x0000023E5C8EE6E0> , podemos ver que solo se guarda en memoria pero no puede ser accedido asi es por eso que tmbn neceitamos "list"
print("Pares:", even_numbers) 