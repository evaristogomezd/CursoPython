#Este ejercicio es una tarea o ejercicio del curso
#Intrucciones:
#Evaluar entrada de dos jugadores
#Usando estructuras condicionales Evaluaras cual es el ganador  

print("Vamos a jugar \nDeben elegerir entre PIEDRA, PAPEL O TIJERA")
Eleccion1 = input ("Jugador Uno es tu turno, escribe tu elección: ")
Eleccion2 = input ("Jugador Dos es tu turno, escribe tu elección: ")
#print(Eleccion1)
#print(Eleccion2)

#REGLAS
#GANAN > PIERDE
#PIEDRA > TIJERA ; TIJERA > PAPEL ; PAPEL > PIEDRA
#EMPATES
#TIJERA = TIJERA ; PIEDRA = PIEDRA ; PAPEL = PAPEL
#OTRA COSA
#No introdujiste una palabra valida
if Eleccion1.upper() == "PIEDRA" and Eleccion2.upper() == "PAPEL":
    print("Jugador Uno eligio PIEDRA y el jugador Dos eligio PAPEL \nJugador DOS GANA")
elif Eleccion1.upper() == "PIEDRA" and Eleccion2.upper() == "TIJERA":
    print("Jugador Uno eligio PIEDRA y el jugador Dos eligio TIJERA \nJugador UNO GANA")