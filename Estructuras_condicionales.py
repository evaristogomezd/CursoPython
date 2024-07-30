#Clase de Estructuras condicionales
#Primero veremos el IF

x = 5
if x > 5:       #Primero se ejecuta y revisa esta linea si es verdadera se ejecuta el codigo
    print("X es mayor que 5")
    print("Adentro del IF")
elif x == 5:    #Si la condicion anterior es falsa y eta verdadera se ejecuta este codigo
    print("X es igual que 5")
else:           #Si ninguna condicion es verdadera, se ejecuta este codigo 
    print("X es menor que 5")
#Esta forma de utilizar if, elis y else, relaciona, y hace dependientes las condiciones
print("afuera") #con salir del nivel de identación es suficiente para salir del bloque de IF
#Los dos puntos (:) se utilizan después de las declaraciones if, elif, y else para indicar que se va a iniciar un bloque de código 
#Esto es parte de la sintaxis del lenguaje y es necesario para que Python entienda que las líneas que siguen son parte del mismo bloque de control
#La indentación se usa para definir bloques de código en lugar de llaves {} como en otros lenguajes de programación 
#La indentación en programación se refiere al uso de espacios o tabulaciones al comienzo de una línea de código para definir la estructura y jerarquía del código 
#En Python, la indentación es especialmente importante pq utiliza la indentación para delimitar bloques en lugar de llaves {} como en otros lenguajes
#Todos los bloques de código dentro de una declaración if, elif, o else deben estar indentados al mismo nivel

#Comparacion usando IF pero con mas de una variable
x = 15
y = 20
if x>10 and y>25:
    print("X es mayor que 10 y Y es mayor que 15")
if x>10 or y>25:
    print("X es mayor que 10 O Y es Mayor que 25")
if not x>10:
    print("X no es mayor que 10")
#al poner diferentes IF hace comparaciones independites, osea no son dependientes entre si


#IF dentro de otro IF
is_member = True
age = 11
if is_member:   #Primer condicion si se cumple entra el otro IF
    if age>=15: #Segunda condicion si se cumple entra a este IF
        print("Tienes acceso ya que eres miembro y mayor o igual a 15 años")
    else:       #Si no se cumple el SEGUNDO IF sucede esto, pero se CUMPLIO EL PRIMERO
        print("No tienes acceso ya que eres miembro pero menor a 15 años")
else:           #Si NO se cumple el PRIMER IF sucede esto
    print("No eres miembro y NO TIENES ACCESO")

# Definir una variable con un número
numero = 5 # Verificar si el número es positivo, negativo o cero
if numero > 0:                      # Si el número es mayor que cero, es positivo
    print("El número es positivo.")
elif numero < 0:                    # Si el número es menor que cero, es negativo
    print("El número es negativo.")
else:                                # Si el número no es ni mayor ni menor que cero, debe ser cero
    print("El número es cero.")


# Definir una variable con la edad de una persona
edad = 20           # Verificar si la persona es mayor de edad (18 años o más)
if edad >= 18:      # Si la edad es mayor o igual a 18, la persona es mayor de edad
    print("La persona es mayor de edad.")
else:               # Si la edad es menor a 18, la persona es menor de edad
    print("La persona es menor de edad.")


#Bucles y control e Iteraciones
#ya vimos que en la listas hay informacion  que puede ser cinsultada con la indexacion o con el slicing
#Sin envago hay una forma de automatizar el ñroceso cuando lo quermos hacer de manera iterable
#Para eso se utilizan lo bucles o controles de iteracion

#EJEMPLO
# en una lista [1,2,3,4,5,6,7,8,9,10]
#Si quieo buscar infrmacion dentro tendre que moverme eir almacendo informacion para saber donde estoy
#POS ser para la posicion
#VAL sera para su contenido o valor
# en la lista del ejemplo el uno esta en POS=0 pero du VAL="1"
numbers =[0,1,2,3,4,5,6,7,8,9,10] 
for i in numbers: #sin novedad se utiliza como un for en progra, solo no olvidemos los puntos y la identación
    if i == 3:      # este whiel esta dentro del for
        continue    #Lo utilizamos para saltar u omitir un paso, para eso seutiliza "continue"
    print ("Aqui 1 es igual ", i)       #en este ejemplo podemos ver que se brinca el 3
    #print ("Aqui 1 es igual ", i+1)    #aca como suma 1 numero a i se brinca el 4

    for i in range(10):
        print(i)

    for x in range(2,9):
        print(i)

    fruits = ["manzana", "uva", "mando","naranja", "lima", "mandarina"]
    for fruit in fruits:
        print(fruit)    
        if fruit == "Naranja":
            print("naranja encontrada")

    w=0
    while  w<5: #while es un mientras y se utiliza como siempre, solo no olvidemos los : a final, si no al dar enter no hace identacion
        if w == 3:  #se agrega una condicion como cualquier otra de if  que si se cumple
            break   #Hace que estre break pare el while y si no hay otra isntruccion se sale
        print(w)
        #w = w+1
        w +=1 # metodo abreviado de w = w +1
