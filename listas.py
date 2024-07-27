#Haremos un ejercio de listas
to_do = ["Agradecer un nuevo dia",
         "Meditar",
         "Hacer ejercicio en la mañana",
         "Bañarse","Desayuno saludable",
         "Leer 1 hr", 
         "Partir al trabajo"]
print(to_do) # al imprimirlas las pone todas seguidas pero separadas por espacio y entre comillas, osea no da enter 

#Mezcla de elemntos y aplicacion de indexaciones
#Indexación: En programación, la indexación se refiere a la manera en que se accede a los elementos dentro de estructuras de datos como arreglos, listas o diccionarios, usando un índice
numbers = [1,2,3,4,"cinco"]
print(numbers)
print(type(numbers)) # podemos observar que lo que nos dice es que es del tipo "list" y dentro puede haber de cualquier otro tipo de dato
mix = ["ich", 2, 3.14,True, [7,8,9]]
print(mix)
print(len(mix)) # para recorda "len" sirve para ver la longitud de un dato o conjunto de datos en este caso hay 5 datos en mix
print("Primer elemento es: ", mix[0])  # lo que significa es que queremos ver el elemnto de la posicion 0 (osea la primera) de la variable de lista "mix"
print("Segundo elemento es: ", mix[1])
print("Ultimo elemento es: ", mix[-1]) # Recordemos que puede utilizarse el mas uno oara alcanzar el ultimo elemnto

cadena = "Supercalifragilisticoespiralidoso" 
print("Primer elemento es: ", cadena[0])
print("Segundo elemento es: ", cadena[5])
print("Ultimo elemento es: ", cadena[-1]) # podemos ver que tambien podemos encotnrar lementos de una cadena 

print(mix[0:2]) #Podemos usar los : para decir "hasta" el ejemplo dice "de 0 hasta 2"
print(mix[:2])  #Podemos ver que si no especifico empezara desde el principio
print(mix[2:])  #Podemos ver que los mismo sucede para el final si no lo especifico
print(mix[:]) #Podemos si no pongo nada va de principio a fin

mix.append(False) # Aqui estamos usando un "METODO" particular de los "OBJETOS" LIST que sirve para egregar el elemnto dentro del ()
print(mix) # vemos que se agrego "False"
mix.append(["a","b"]) 
print(mix) 
mix.insert(1,["a","b"]) #Este es otro "METODO" pero este sirve para insertar el elemnto pero en la posicion que quiero no solo al final
print(mix)             #Aqui vemos que la lista ["a","b"] se coloco en la segunda posicion, recuerda primero va el 0, 1, 2,...
print(mix.index(["a","b"])) #"INDEX" es un método que se utiliza para encontrar el índice de un elemento específico en la lista
listanums = [34, 56, 78, 23, 12, 90, 44, 67, 89, 21, 11, 35, 50, 72, 60]
print("De la lista de estos numeros: ",listanums)
print("El mayor es: ", max(listanums)) # max y min son funciones incorporadas y justo sirven paa buscar el mayp ry menor de una lista 
print("El menor es: ", min(listanums)) # tambien podria usarse en cadenas para obtener el carácter con el valor máximo o mínimo basado en el orden ASCII.
del listanums[-1] #"DEL" pero en minuscula es una palabra reservada que se utiliza para eliminar, si especifico en los corchetes cuafrados solo eliminara lo que yo seleccione
print(listanums)
del listanums[:2] #i
print(listanums)
del listanums
#print(listanums) # esta comentad por que manda error al ejecutar ya que se elimino la variable "listanums"


print("--------------------------------------------------------------------------------------------------")
print("Cambio de clase - Metodo SLICE")
print("--------------------------------------------------------------------------------------------------")
#Metodo SLICE
listA = [34, 56, 78, 23, 12, 90, 44, 67, 89, 21, 11, 35, 50, 72, 60]
listB = listA
print(listA)
print(listB)
del listA[0] #Se mando a borrar en la "listA", pero se borro en las dos por que mabas ocupa y comparten el mismo lugar en memoria
print(listA)
print(listB)
print(id(listA))
print(id(listB)) #Como vemos ambas estan compartiendo el mismo espacio en memoria, por eso su numero es el mismo
#Para que esto no suceda es que se utiliza el METODO "SLICE"
listC = listA[:]
print(id(listA))
print(id(listB)) 
print(id(listC)) #Si nos damos cuenta el espacio en memoria ya cambio 
listA.append(89)
print(listA)
print(listB) 
print(listC) #podemos ver que aqui no se agrego la modificacion 
print(id(listA))
print(id(listB)) 
print(id(listC)) # aqui vemos wue mantiene el espacio de memoria tambien diferente
#En python podemos tener diferentes tipos de clases dentro de una coleccion en  otros lenguajs al parecer eso no se pude 
#En Python, puedes almacenar diferentes tipos de objetos dentro de una sola colección, como una lista, tupla o conjunto. Esto se debe a la flexibilidad del tipo de datos en Python
