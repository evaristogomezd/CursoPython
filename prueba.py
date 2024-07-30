variableL  = lambda a, b: a + b    # al utilizar lambda le estoy diciendo que variable existe y como se realizara la operacion 
print(variableL(10,4))

tresvar = lambda a, b, c: a * b * c
print(tresvar(80,5,2))

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
