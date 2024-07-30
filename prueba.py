# Fibonacci
def fibonacci(n):                     # Sumatoria de numeros; variable "n"
    if n == 0:                          # este es nuestro caso base osea nuestro caso minimo o de orignen 
        return 0                        # en este ejemplo no resta nada solo es 0
    elif n==1:
        return 1
    else:                               #este es nuestro caso recursuvi mientras no se cumpla el 0 seguiremos restando n-1
        return fibonacci(n-1) + fibonacci(n-2)   # en este ejemplo si tuvieramos n=5 seria sum_numbers(5-1) osea sum_numbers(4)
numberF = 8
resultF = fibonacci(numberF)                 # Llamada a la función
print("El numero de la serie de Fibonacci correspondiente a",numberF, "es :", resultF)