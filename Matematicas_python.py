#Operadores numericos
a= 10
b= 3
print("Suma:", a+b)
print("Resta:", a-b)
print("Multiplicación:", a*b)
print("División:", a/b)
print("Moddulo o resto:", a%b) # modulo l resto es para lo que sobra en una division 
print("Entero de la división:", a//b) # la dobke division no es que divida dos veces es que solo me da los numeros enteres
print("potenciació :", a**b) # el doble asterisco sirve para elevar ala potencia aqui seria 1 al cubo

a= a +2
print(a)
a+= 2
print(a)
a-= 2
print(a)
a*= 2
print(a)
a/=2
print("A vale:",a)

#PEMDAS
# La regla PEMDAS dice que:
#orden de operaciones
# Parentheses (Paréntesis)
# Exponents (Exponenciación y raíces)
# Multiplication (Multiplicación)
# Division (División)
# Addition (Suma)
# Subtraction (Resta)

operacion1 = 2+3*4
print(operacion1)
operacion2 = 2+(3*4)
print(operacion2)
operacion3 = (2+3)*(4**2) / 8 -1
print(operacion3)

#operadores booleanos o de comparación
print (a>b)   #Evalua si a es  mayor  que b y devuelve si eso es falso o verdadero
print (a<b)   #Evalua si a es  menor  que b y devuelve si eso es falso o verdadero
print (a>=b)  #Evalua si a es  mayor o igual  que b y devuelve si eso es falso o verdadero
print (a<=b)  #Evalua si a es  menor o igual  que b y devuelve si eso es falso o verdadero
print (a==b)  #Evalua si a es  igual  que b y devuelve si eso es falso o verdadero
print (a!=b)  #Evalua si a es  diferente  que b y devuelve si eso es falso o verdadero
