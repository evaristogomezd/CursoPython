#Diccionarios
#Los diccionarios en phyton almacenan dos datos, la clave y el valor 
#Es como el diccionario por eso se les dice asi
#palabra = CLAVE
#definición = VALOR

numbers = {1:"uno", 2:"dos", 3:"tres"} 
mi_diccionario = { 'clave1': 'valor1',
                   'clave2': 'valor2',
                   'clave3': 'valor3'}
#Un diccionario en Python se define usando llaves {} y contiene pares de clave-valor separados por comas. 
#Las claves deben ser únicas e inmutables (pueden ser números, cadenas o tuplas), mientras que los valores pueden ser de cualquier tipo de datos 
print(numbers[2])
print(mi_diccionario["clave3"])

information = {"nombreI": "Evaristo",
               "Apellido": "Gomez",
               "Altura": 1.78,
               "Edad": 35}
print(information)
del information["Edad"]
print(information)
claves = information.keys()
print(claves)
#print(type(claves))
values = information.values()
print(values)
pairs = information.items()
print(pairs)

estudiante = {'nombreE': 'Varo',
              'edad': 20,
              'cursos': ['Matemáticas', 'Física', 'Química'],
              'promedio': 8.0 }
print(estudiante)
nombreE = estudiante['nombreE']
print(nombreE)  
edad = estudiante['edad']
print(edad)  
estudiante['edad'] = 22 # cambiando el valor de un diccionario
print(estudiante['edad'])  
clavesE = estudiante.keys() #metodo oara pedir las llaves o claves
print(clavesE)
#print(type(clavesE)) # poemos ver que es una variable del tipo dict osea diccionario
valuesE = estudiante.values() #Metodo para pedir los valores
print(valuesE)
pairsE = estudiante.items() #Metodo para pedir los pares de los valores, me los va a dar impresos en tuplas
print(pairsE)
estudiante['graduado'] = False # de esta forma agrego una nueva clave y valor, clave dentro de los [] y le digo que es igual al valor asignado
print(estudiante)  # Salida: {'nombre': 'Juan', 'edad': 22, 'cursos': ['Matemáticas', 'Física', 'Química'], 'promedio': 8.5, 'graduado': False}
del estudiante['promedio']
print(estudiante)  # Salida: {'nombre': 'Juan', 'edad': 22, 'cursos': ['Matemáticas', 'Física', 'Química'], 'graduado': False}
graduado = estudiante.pop('graduado') # esta es otra forma de eliminar 
print(estudiante)  # Salida: {'nombre': 'Juan', 'edad': 22, 'cursos': ['Matemáticas', 'Física', 'Química']}

contacts = {"Vane": {"Apellido": "Canto",
               "Altura": 1.60,
               "Edad": 29},
                "Evaristo": {"Apellido": "Gomez",
               "Altura": 1.80,
               "Edad": 35}}
print(contacts["Vane"])


# dict.keys(): Devuelve una vista de las claves del diccionario.
# dict.values(): Devuelve una vista de los valores del diccionario.
# dict.items(): Devuelve una vista de los pares clave-valor del diccionario.
# dict.get(clave, valor_por_defecto): Devuelve el valor asociado a la clave. Si la clave no existe, devuelve valor_por_defecto.
# dict.update(otro_diccionario): Actualiza el diccionario con los pares clave-valor de otro_diccionario.
