Saludo = "Hola"
Saludo2 = 'HOLA por dos'
Nombre = "Evaristo "
Nombre2 = '''Gomez
Davalos''' # escribir comillas simples pero de forma triple me permite que se vean e incluyan cambios de linea
Caracter = "C" # en lo personal prefiero comillas dobles por que son las que mas ampliamente se usan
Presentacion = "Hola, Yo soy"
Fullname = "Evaristo Gomez Davalos"
print (type(Caracter))
print ((Saludo + " " +  Nombre))
print(Fullname[0]) # Ponemos 0 por ue se empeiza a contar de 0 
print(Fullname[-1]) # Puedo poner numeros dnegativos para empzar del final al principio -1 seria 
print (Presentacion + " " +Fullname) # en python se utiliza + para concatenar
print (Nombre *5)
print (len(Fullname))
print (Saludo2.lower()) #LOWER es un METODO que me sirve para convertir en minuscula
print (Saludo.upper())  #UPPER es un METODO para convertir a MAYUSULAS
print (Fullname.strip())#STRIP es un METODO para cortar por decirlo de una forma en ese caso espacios
texto = "###Hola, mundo!###"
print (texto.strip("#")) #STRIP  en este caso cortara el simbolo de #
print (Presentacion, Fullname) # aqui estoy usando la coma para poner espacio en lugar del + 
print ("la", "coma", "permite", "poner", "espacios") # Al concatenar elementos
print ("la", "coma", "permite", "poner", "espacios", sep="-") # sep permite elegir como separar los elemnetos 

#formas de asiganr variables
frase = "Al infinito y mas alla"
author = "Buzz Lightyear"
print("Frase:", frase, "Autor:", author) # usar comas para espacio y variables para decir donde estan
print(f"Frase: {frase}, Autor: {author}") #f-strings nosmsrive para decirleque s una cadena de texto y que lo que este dentro de las llaves lo ponga asi
print("Frase: {}, Autor: {}".format(frase, author)) # el  format y llaves vacias nos yudan a acomodar los valores en las llaves pero hay que cuidar el orden
valor = 3.14159
print("Valor: {:.2f}".format(valor)) # de esta forma especificas cuantos numeros decimales osea depues del punto quieres ver
print("Cambio\n de linea") #slashN \n sirve parfa cambio de linea
print("Me  dicen \"Varo\"") # Para usar comillas debes usar slash
print("La ruta de archivo es: C:\\Users\\Usuario\\Desktop\\archivo.txt") # para poner slashh debes ponerlo doble


x = 10
y = 5.678
z = 1.5e2
a = 5.6e-7
print (x)
print(type(x))
print (y)
print(type(y))
print (z)
print(type(z))
print (a)
print(type(a))
print (x+x)
buleanoT = True
print (buleanoT)
print (type(buleanoT))