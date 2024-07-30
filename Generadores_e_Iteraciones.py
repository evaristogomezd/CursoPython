#Generadores e iteraciones
#Sirven muy bien para trabajr conn colecciones de manera eficiente 
#De hecho podemos trabajar con grandes cantidades de infrmacion sin almacener todo a la vez en memoria
#Iterar significa repetir un proceso o ejecutar una serie de instrucciones varias veces. 
#En programación, iterar a menudo se refiere a recorrer una colección de elementos 
#(como un array, una lista o un conjunto de datos) y realizar una operación en cada uno de esos elementos.
#
#ITERADDORES
lista1 = [0,1,2,3,4,5]   # Creamos una lista
iterador = iter(lista1)             # Creamos el iter
print(next(iterador))               # usamoa el iterado y la funcion next nos sirve para ver lo que se ssta guaradndo
print(next(iterador))               #next nos ayuda a ver cuales son ls alors o información que se guarda en memria
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))

# ITERAR EN CADENAS
text = "hola mundo"         #Creamos la cadena de texto (string)
iter_text = iter(text)      #Creamos el iterador
for char in iter_text:      #En este paso empezamos a iterar la cadena
    print(char)

# IERADOR DE NUMEROS IMPARES
limit = 10                              #creamos una variable llamada limite para que sea nuesyro tope 
odd_iter = iter(range(1,limit+1,2))     #la funcion range nos sirva para decir de donde a donde y comoe mpieza en uno  podemos decirle en el tercer escoacio de range (0,0,X) sirve para marcar el paso 
for nume in odd_iter:
    print(nume)


# GENERADOR 
# Un generador es una función que permite iterar sobre una secuencia de valores, produciendo un valor en cada iteración sin almacenar toda la secuencia en memoria. 
# Los generadores son especialmente útiles para trabajar con grandes conjuntos de datos o secuencias infinitas, ya que generan valores bajo demanda.
# def se utiliza para definiri funciones
def contador(max): # La función contador es un generador que produce una secuencia de números del 1 al valor especificado por 'max'.
    contador = 1
    while contador <= max:      # 'yield' produce un valor y pausa la ejecución de la función generadora, guardando su estado para reanudar desde aquí la próxima vez que se llame.
        yield contador
        contador += 1           # Incrementa el contador en 1
for numero in contador(5):      # Uso del generador, Itera sobre los valores producidos por el generador 'contador'
    print(numero)               # En cada iteración, 'numero' toma el valor producido por 'yield' en el generador

# Uso del GENERADOR
def generator():                 #definimos nuestar funcion "generator"
    yield "a"                      #yield se utiliza no para retornar datos  no para agregaf a la variable generator
    yield "b"
    yield "c"

for value in generator():
    print(value)

# FIBONACCI
# 0 1 1 2 3 5 8 13 21
def fibo(max):
    a, b= 0, 1
    # a = 0
    # b = 1
    while a < max:
        yield a
        a, b = b, a + b
        # a = b
        # b = a + b
for num in fibo(50):
    print(num)