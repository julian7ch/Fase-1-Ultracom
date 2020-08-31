#Movimiento posibles para fichas de ajedrez

ficha= int(input ("Elija por favor el número de la ficha que desea mover: 1=Rey 2=Reina 3=Caballo 4=Alfíl 5=Torre 6=Peón. Indique el número de la ficha: "))

while ficha>6 or ficha<1:
    ficha= int(input ("valor inválido, por favor ingrese un valor entre 1 y 6, para deifnir la ficha a mover. " " Posibles fichas para mover: 1=Rey 2=Reina 3=Caballo 4=Alfil 5=Tore 6=Peon Ingresar numero de la ficha que desea mover:"))

if ficha==1:
    mover="El Rey"
elif ficha==2:
    mover="La Reina"
elif ficha==3:
    mover="El Caballo"
elif ficha==4:
    mover="El Alfíl"
elif ficha==5:
    mover="La Torre"
elif ficha==6:
    mover="El Peón"

print ("La ficha elegida fue " + mover)


#definicion de la matriz para el tablero de ajedrez, inicalmente vacio:
tablero = [[0 for _ in range(8)] for _ in range(8)]
for fila in tablero:
    print(fila)

#Elegir posición de la ficha dentro del tablero de ajedrez
import random
posicionHorizontal=int(input("Ingrese un valor entre 1 y 8, para elegir la posición horizontal de " + mover+ " dentro del  tablero de ajedrez , donde 1 es la posicón extrema izquierda y 8 la posición extrema derecha, en caso de querer una posición ALEATORIA, marque cero (0): "))-1
if posicionHorizontal==-1:
    posicionHorizontal=random.randint(0, 7)
    
posicionVertical=int(input("Ingrese un valor entre 1 y 8, para elegir la posición vertical de " + mover+ " dentro del  tablero de ajedrez , donde 1 es la posicón superir y 8 la posición inferior, en caso de querer una posición ALEATORIA, marque cero (0): "))-1
if posicionVertical==-1:
    posicionVertical=random.randint(0, 7)
        
if posicionHorizontal>=0 and posicionHorizontal<=7 and posicionVertical>=0 and posicionVertical<=7:
        
    if ficha==1:
        tablero[posicionVertical] [posicionHorizontal]=8
        hor_aux =()
        vert_aux =()
        instrucciones = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
        
        for instruccion in instrucciones:
            if 0 <= posicionHorizontal + instruccion[0] <= 7 and 0 <= posicionVertical + instruccion[1] <= 7:
                tablero [posicionVertical + instruccion[1]] [posicionHorizontal + instruccion[0]] = 1
        
        for fila in tablero:
            print(fila)
        
            
    if ficha==2:
        tablero[posicionVertical] [posicionHorizontal]=8
        instrucciones = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
        for instruccion in instrucciones:
            hor_aux = posicionHorizontal + instruccion[0]
            vert_aux = posicionVertical + instruccion[1]
        
            while 0 <= hor_aux <= 7 and 0 <= vert_aux <= 7:
                tablero[vert_aux][hor_aux] = 1
                
                hor_aux += instruccion[0] 
                vert_aux += instruccion[1]
            
        for fila in tablero:
            print(fila)
                
        
        
    elif ficha==3:          
        
        tablero[posicionVertical] [posicionHorizontal]=8
        
        instrucciones = [(-2, 1), (-1, 2), (2, -1), (1, -2), (1, 2), (2, 1), (-1, -2), (-2, -1)]
        
        for instruccion in instrucciones:
            if 0 <= posicionHorizontal + instruccion[0] <= 7 and 0 <= posicionVertical + instruccion[1] <= 7:
                tablero [posicionVertical + instruccion[1]] [posicionHorizontal + instruccion[0]] = 1
        
        for fila in tablero:
            print(fila)
        
        
    elif ficha==4:
        tablero[posicionVertical] [posicionHorizontal]=8
        
        instrucciones = [(-1, -1), (-1, 1), (1, 1), (1, -1)]

        for instruccion in instrucciones:
            hor_aux = posicionHorizontal + instruccion[0]
            vert_aux = posicionVertical + instruccion[1]
        
            while 0 <= hor_aux <= 7 and 0 <= vert_aux <= 7:
                tablero[vert_aux][hor_aux] = 1
                
                hor_aux += instruccion[0] 
                vert_aux += instruccion[1]
            
        for fila in tablero:
            print(fila)
        
    if ficha==5:
        tablero[posicionVertical] [posicionHorizontal]=8
        instrucciones = [(-1,0),(0,1),(1,0),(0,-1)]
        for instruccion in instrucciones:
            hor_aux = posicionHorizontal + instruccion[0]
            vert_aux = posicionVertical + instruccion[1]
        
            while 0 <= hor_aux <= 7 and 0 <= vert_aux <= 7:
                tablero[vert_aux][hor_aux] = 1
                
                hor_aux += instruccion[0] 
                vert_aux += instruccion[1]
            
        for fila in tablero:
            print(fila)
        
    elif ficha==6:
        if posicionVertical<=6 and posicionVertical>=2 :
            tablero[posicionVertical+1][posicionHorizontal]=1
            tablero[posicionVertical][posicionHorizontal]=8
        elif posicionVertical==1:
            tablero[posicionVertical+1][posicionHorizontal]=1
            tablero[posicionVertical+2][posicionHorizontal]=1
            tablero[posicionVertical][posicionHorizontal]=8
        elif posicionVertical==0:
            tablero[posicionVertical][posicionHorizontal]=8
            print(" no es una posicion posible de la ficha")
        elif posicionVertical==7:        
            tablero[posicionVertical][posicionHorizontal]=8
            print ("el Peón no tiene movimeintos disponibles")            
        for fila in tablero:
            print(fila)
    print("la posición de "+ mover + " es: Horizontal "+ str(posicionHorizontal+1)+ " y vertical:" + str(posicionVertical+1))
elif posicionHorizontal<0 or posicionHorizontal>7 :
    print ("El valor asignado a la posición HORIZONTAL  no esta dentro del rango aceptable(de 0 a 8), vuelve a empezar")
else:
    print ("El valor asignado a la posición VERTICAL  no esta dentro del rango aceptable(de 0 a 8), vuelve a empezar") 




