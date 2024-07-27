#En esta clases vamos a ver Matrices
#Por lo visto a esto le dien lista de listas O.o
matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(matriz) #Even we saw the matriz in one line, the system respect the order of columns and rows
print(matriz[0]) #Whit this I can saw and use teh first list, in the positio 0 of the rows
matrix = [[[1,2],[3,4]],
          [[5,6],[7,8]]]
print(matrix)
 
print("--------------------------------------------------------------------------------------------------")
#Ahora veremos TUPLAS # es la misma clase
numbers = (1,2,3,4,5) # para las tuplas puedo o NO poner parentesis, python solito se da cuenta aue es una TUPLA
print(numbers)
print(type(numbers))
print(numbers[0])
#numbers[0] = "uno" #comentamos esta parte por que marca error
#print(numbers)     #marca erro por que las TUPLAS son INMUTABLES