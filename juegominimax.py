gato = "G"
raton = "R"
pared = "#"
vacio = "."
queso = "Q"


tablero = [
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", "G", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "R"]
]



x1, y1 = 2, 2
x2, y2 = 6, 12
posiciones_queso = [
    (2, 6),
    (2, 18),
    (7, 12),
    (12, 6),
    (12, 18)
]


def fuera_del_mapa():
    print("")
    print("Movimiento no Permitido: Juegue dentro del mapa")

def choque_con_pared_gato():
    tablero[x1][y1] = pared
    print("")
    print("Movimiento no Permitido: No puede chocar contra una pared")

def choque_con_pared_raton():
    tablero[x2][y2] = pared
    print("")
    print("Movimiento no Permitido: No puede chocar contra una pared")

def raton_atravesando_pared():
    print("El Raton no puede atravesar paredes")

# Funcion para mostrar el tablero con encabezado en emojis:
def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))


# Funcion para colocar los quesos:
def colocar_quesos(tablero, posiciones):
    for fila, col in posiciones:
        tablero[fila][col] = queso


print("Bienvenido al juego del Gato y el Raton:")
print("")

# Llamada a la función para mostrar el tablero:
mostrar_tablero(tablero)
print("")


def turno_gato():
    global x1, y1
    tablero[0][0] = "🚪"

    while True:
        movimiento = input("Gato, haga su movimiento (WASD):").lower()  

        # Movimiento hacia arriba:
        if movimiento == "w":
            tablero[x1][y1] = vacio
            colocar_quesos(tablero, posiciones_queso)
            x1 = x1 - 1

            if x1 > 6 or x1 < 0 or y1 > 12 or y1 < 0:
                fuera_del_mapa()
                x1 = x1 + 1
            
            elif tablero[x1][y1] == pared:
                choque_con_pared_gato()
                x1 = x1 + 1

            else:
                tablero[x1][y1] = gato
                print("")
                mostrar_tablero(tablero)
                break
        

        # Movimiento doble hacia arriba:
        if movimiento == "ww":
            tablero[x1][y1] = vacio
            colocar_quesos(tablero, posiciones_queso)
            x1 = x1 - 2
            
            if x1 > 6 or x1 < 0 or y1 > 12 or y1 < 0:
                fuera_del_mapa()
                x1 = x1 + 2
            
            elif tablero[x1][y1] == pared:
                choque_con_pared_gato()
                x1 = x1 + 2

            else:
                tablero[x1][y1] = gato
                print("")
                mostrar_tablero(tablero)
                break
        

        # Movimiento hacia abajo:
        elif movimiento == "s":
            tablero[x1][y1] = vacio
            colocar_quesos(tablero, posiciones_queso)
            x1 = x1 + 1
            
            if x1 > 6 or x1 < 0 or y1 > 12 or y1 < 0:
                fuera_del_mapa()
                x1 = x1 - 1
            
            elif tablero[x1][y1] == pared:
                choque_con_pared_gato()
                x1 = x1 - 1

            else:
                tablero[x1][y1] = gato
                print("")
                mostrar_tablero(tablero)
                break
        

        # Movimiento doble hacia abajo:
        elif movimiento == "ss":
            tablero[x1][y1] = vacio
            colocar_quesos(tablero, posiciones_queso)
            x1 = x1 + 2

            if x1 > 6 or x1 < 0 or y1 > 12 or y1 < 0:
                fuera_del_mapa()
                x1 = x1 - 2
            
            elif tablero[x1][y1] == pared:
                choque_con_pared_gato()
                x1 = x1 - 2
            
            else:
                tablero[x1][y1] = gato
                print("")
                mostrar_tablero(tablero)
                break

        
        # Movimiento hacia la izquierda:
        elif movimiento == "a":
            tablero[x1][y1] = vacio
            colocar_quesos(tablero, posiciones_queso)
            y1 = y1 - 1
            
            if x1 > 6 or x1 < 0 or y1 > 12 or y1 < 0:
                fuera_del_mapa()
                y1 = y1 + 1
            
            elif tablero[x1][y1] == pared:
                choque_con_pared_gato()
                y1 = y1 + 1

            else:
                tablero[x1][y1] = gato
                print("")
                mostrar_tablero(tablero)
                break
        

        # Movimiento doble hacia la izquierda:
        elif movimiento == "aa":
            tablero[x1][y1] = vacio
            colocar_quesos(tablero, posiciones_queso)
            y1 = y1 - 2

            if x1 > 14 or x1 < 0 or y1 > 24 or y1 < 0:
                fuera_del_mapa()
                y1 = y1 + 2
            
            elif tablero[x1][y1] == pared:
                choque_con_pared_gato()
                y1 = y1 + 2
            
            else:
                tablero[x1][y1] = gato
                print("")
                mostrar_tablero(tablero)
                break


        # Movimiento hacia la derecha:
        elif movimiento == "d":
            tablero[x1][y1] = vacio
            colocar_quesos(tablero, posiciones_queso)
            y1 = y1 + 1
            
            if x1 > 14 or x1 < 0 or y1 > 24 or y1 < 0:
                fuera_del_mapa()
                y1 = y1 - 1
            
            elif tablero[x1][y1] == pared:
                choque_con_pared_gato()
                y1 = y1 - 1

            else:
                tablero[x1][y1] = gato
                print("")
                mostrar_tablero(tablero)
                break

        
        # Movimiento doble hacia la derecha:
        elif movimiento == "dd":
            tablero[x1][y1] = vacio
            colocar_quesos(tablero, posiciones_queso)
            y1 = y1 + 2
        
            if x1 > 14 or x1 < 0 or y1 > 24 or y1 < 0:
                    fuera_del_mapa()
                    y1 = y1 - 2
            
            elif tablero[x1][y1] == pared:
                    choque_con_pared_gato()
                    y1 = y1 - 2
            
            else:
                    tablero[x1][y1] = gato
                    print("")
                    mostrar_tablero(tablero)
                    break
        

        else:
            print("Tecla no definida, recuerde solo pulsar WASD")

def turno_raton():
    global x2, y2
    global puntaje_del_raton
    
    while True:
        movimiento_raton = input("Raton, haga su movimiento (W-A-S-D-Q-E-Z-C):").lower()
        

        # Moviento hacia arriba:
        if movimiento_raton == "w":
            tablero[x2][y2] = vacio
            x2 = x2 - 1
            
            if x2 > 6 or x2 < 0 or y2 > 12 or y2 < 0:
                fuera_del_mapa()
                x2 = x2 + 1

            elif tablero[x2][y2] == pared:
                choque_con_pared_raton()
                x2 = x2 + 1
            
            elif tablero[x2][y2] == queso:
                tablero[x2][y2] = raton
                posiciones_queso.remove((x2, y2))
                print("")
                mostrar_tablero(tablero)
                print("Agarraste el Queso! Ganaste +1 puntos.")
                puntaje_del_raton = puntaje_del_raton + 1
                break

            else:
                tablero[x2][y2] = raton
                print("")
                mostrar_tablero(tablero)
                break
        

        # Movimiento al lateral superior izquierdo:
        elif movimiento_raton == "q":
            tablero[x2][y2] = vacio
            x2 = x2 - 1
            y2 = y2 - 1
            
            if x2 > 6 or x2 < 0 or y2 > 12 or y2 < 0:
                fuera_del_mapa()
                x2 = x2 + 1
                y2 = y2 + 1

            elif tablero[x2][y2] == pared:
                choque_con_pared_raton()
                x2 = x2 + 1
                y2 = y2 + 1
            
            elif tablero[x2][y2] == queso:
                tablero[x2][y2] = raton
                posiciones_queso.remove((x2, y2))
                print("")
                mostrar_tablero(tablero)
                print("Agarraste el Queso! Ganaste +1 puntos.")
                puntaje_del_raton = puntaje_del_raton + 1
                break

            else:
                tablero[x2][y2] = raton
                print("")
                mostrar_tablero(tablero)
                break
        

        # Movimiento doble lateral superior izquierdo:
        elif movimiento_raton == "qq":
            tablero[x2][y2] = vacio
            x2 = x2 - 2
            y2 = y2 - 2
            
            if x2 > 6 or x2 < 0 or y2 > 12 or y2 < 0:
                fuera_del_mapa()
                x2 = x2 + 2
                y2 = y2 + 2

            elif tablero[x2][y2] == pared:
                choque_con_pared_raton()
                x2 = x2 + 2
                y2 = y2 + 2
            
            elif tablero[x2 + 1][y2 + 1] == pared:
                raton_atravesando_pared()
                x2 = x2 + 2
                y2 = y2 + 2
            
            elif tablero[x2][y2] == queso:
                tablero[x2][y2] = raton
                posiciones_queso.remove((x2, y2))
                print("")
                mostrar_tablero(tablero)
                print("Agarraste el Queso! Ganaste +1 puntos.")
                puntaje_del_raton = puntaje_del_raton + 1
                break

            else:
                tablero[x2][y2] = raton
                print("")
                mostrar_tablero(tablero)
                break
        

        # Movimiento al lateral superior derecho:
        elif movimiento_raton == "e":
            tablero[x2][y2] = vacio
            x2 = x2 - 1
            y2 = y2 + 1
            
            if x2 > 6 or x2 < 0 or y2 > 12 or y2 < 0:
                fuera_del_mapa()
                x2 = x2 + 1
                y2 = y2 - 1

            elif tablero[x2][y2] == pared:
                choque_con_pared_raton()
                x2 = x2 + 1
                y2 = y2 - 1
            
            elif tablero[x2][y2] == queso:
                tablero[x2][y2] = raton
                posiciones_queso.remove((x2, y2))
                print("")
                mostrar_tablero(tablero)
                print("Agarraste el Queso! Ganaste +1 puntos.")
                puntaje_del_raton = puntaje_del_raton + 1
                break

            else:
                tablero[x2][y2] = raton
                print("")
                mostrar_tablero(tablero)
                break
        
        
        # Movimiento doble al lateral superior derecho:
        elif movimiento_raton == "ee":
            tablero[x2][y2] = vacio
            x2 = x2 - 2
            y2 = y2 + 2
            
            if x2 > 6 or x2 < 0 or y2 > 12 or y2 < 0:
                fuera_del_mapa()
                x2 = x2 + 2
                y2 = y2 - 2

            elif tablero[x2][y2] == pared:
                choque_con_pared_raton()
                x2 = x2 + 2
                y2 = y2 - 2
            
            elif tablero[x2 + 1][y2 - 1] == pared:
                raton_atravesando_pared()
                x2 = x2 + 2
                y2 = y2 - 2
            
            elif tablero[x2][y2] == queso:
                tablero[x2][y2] = raton
                posiciones_queso.remove((x2, y2))
                print("")
                mostrar_tablero(tablero)
                print("Agarraste el Queso! Ganaste +1 puntos.")
                puntaje_del_raton = puntaje_del_raton + 1
                break

            else:
                tablero[x2][y2] = raton
                print("")
                mostrar_tablero(tablero)
                break


        # Movimiento hacia la izquierda:
        elif movimiento_raton == "a":
            tablero[x2][y2] = vacio
            y2 = y2 - 1
            
            if x2 > 6 or x2 < 0 or y2 > 12 or y2 < 0:
                fuera_del_mapa()
                y2 = y2 + 1

            elif tablero[x2][y2] == pared:
                choque_con_pared_gato()
                y2 = y2 + 1

            elif tablero[x2][y2] == queso:
                tablero[x2][y2] = raton
                posiciones_queso.remove((x2, y2))
                print("")
                mostrar_tablero(tablero)
                print("Agarraste el Queso! Ganaste +1 puntos.")
                puntaje_del_raton = puntaje_del_raton + 1
                break

            else:
                tablero[x2][y2] = raton
                print("")
                mostrar_tablero(tablero)
                break
        

        # Movimiento hacia la derecha:
        elif movimiento_raton == "d":
            tablero[x2][y2] = vacio
            y2 = y2 + 1
            
            if x2 > 6 or x2 < 0 or y2 > 12 or y2 < 0:
                fuera_del_mapa()
                y2 = y2 - 1

            elif tablero[x2][y2] == pared:
                choque_con_pared_raton()
                y2 = y2 - 1

            elif tablero[x2][y2] == queso:
                tablero[x2][y2] = raton
                posiciones_queso.remove((x2, y2))
                print("")
                mostrar_tablero(tablero)
                print("Agarraste el Queso! Ganaste +1 puntos.")
                puntaje_del_raton = puntaje_del_raton + 1
                break
            
            else:
                tablero[x2][y2] = raton
                print("")
                mostrar_tablero(tablero)
                break
        

        # Movimiento lateral inferior izquierdo:
        elif movimiento_raton == "z":
            tablero[x2][y2] = vacio
            x2 = x2 + 1
            y2 = y2 - 1
            
            if x2 > 6 or x2 < 0 or y2 > 12 or y2 < 0:
                fuera_del_mapa()
                x2 = x2 - 1
                y2 = y2 + 1

            elif tablero[x2][y2] == pared:
                choque_con_pared_raton()
                x2 = x2 - 1
                y2 = y2 + 1
            
            elif tablero[x2][y2] == queso:
                tablero[x2][y2] = raton
                posiciones_queso.remove((x2, y2))
                print("")
                mostrar_tablero(tablero)
                print("Agarraste el Queso! Ganaste +1 puntos.")
                puntaje_del_raton = puntaje_del_raton + 1
                break

            else:
                tablero[x2][y2] = raton
                print("")
                mostrar_tablero(tablero)
                break
        

        # Movimiento doble lateral inferior izquierdo:
        elif movimiento_raton == "zz":
            tablero[x2][y2] = vacio
            x2 = x2 + 2
            y2 = y2 - 2
            
            if x2 > 6 or x2 < 0 or y2 > 12 or y2 < 0:
                fuera_del_mapa()
                x2 = x2 - 2
                y2 = y2 + 2

            elif tablero[x2][y2] == pared:
                choque_con_pared_raton()
                x2 = x2 - 2
                y2 = y2 + 2
            
            elif tablero[x2 - 1][y2 + 1] == pared:
                raton_atravesando_pared()
                x2 = x2 - 2
                y2 = y2 + 2
            
            elif tablero[x2][y2] == queso:
                tablero[x2][y2] = raton
                posiciones_queso.remove((x2, y2))
                print("")
                mostrar_tablero(tablero)
                print("Agarraste el Queso! Ganaste +1 puntos.")
                puntaje_del_raton = puntaje_del_raton + 1
                break

            else:
                tablero[x2][y2] = raton
                print("")
                mostrar_tablero(tablero)
                break


        # Movimiento lateral inferior derecho:
        elif movimiento_raton == "c":
            tablero[x2][y2] = vacio
            x2 = x2 + 1
            y2 = y2 + 1
            
            if x2 > 6 or x2 < 0 or y2 > 12 or y2 < 0:
                fuera_del_mapa()
                x2 = x2 - 1
                y2 = y2 - 1

            elif tablero[x2][y2] == pared:
                choque_con_pared_raton()
                x2 = x2 - 1
                y2 = y2 - 1
            
            elif tablero[x2][y2] == queso:
                tablero[x2][y2] = raton
                posiciones_queso.remove((x2, y2))
                print("")
                mostrar_tablero(tablero)
                print("Agarraste el Queso! Ganaste +1 puntos.")
                puntaje_del_raton = puntaje_del_raton + 1
                break

            else:
                tablero[x2][y2] = raton
                print("")
                mostrar_tablero(tablero)
                break


        # Movimiento doble lateral inferior derecho:
        elif movimiento_raton == "cc":
            tablero[x2][y2] = vacio
            x2 = x2 + 2
            y2 = y2 + 2
            
            if x2 > 6 or x2 < 0 or y2 > 12 or y2 < 0:
                fuera_del_mapa()
                x2 = x2 - 2
                y2 = y2 - 2

            elif tablero[x2][y2] == pared:
                choque_con_pared_raton()
                x2 = x2 - 2
                y2 = y2 - 2
            
            elif tablero[x2 - 1][y2 - 1] == pared:
                raton_atravesando_pared()
                x2 = x2 - 2
                y2 = y2 - 2
            
            elif tablero[x2][y2] == queso:
                tablero[x2][y2] = raton
                posiciones_queso.remove((x2, y2))
                print("")
                mostrar_tablero(tablero)
                print("Agarraste el Queso! Ganaste +1 puntos.")
                puntaje_del_raton = puntaje_del_raton + 1
                break

            else:
                tablero[x2][y2] = raton
                print("")
                mostrar_tablero(tablero)
                break


        # Movimiento hacia abajo:
        elif movimiento_raton == "s":
            tablero[x2][y2] = vacio
            x2 = x2 + 1 
            
            if x2 > 6 or x2 < 0 or y2 > 12 or y2 < 0:
                fuera_del_mapa()
                x2 = x2 - 1

            elif tablero[x2][y2] == pared:
                choque_con_pared_raton()
                x2 = x2 - 1

            elif tablero[x2][y2] == queso:
                tablero[x2][y2] = raton
                posiciones_queso.remove((x2, y2))
                print("")
                mostrar_tablero(tablero)
                print("Agarraste el Queso! Ganaste +1 puntos.")
                puntaje_del_raton = puntaje_del_raton + 1
                break

            else:
                tablero[x2][y2] = raton
                print("")
                mostrar_tablero(tablero)
                break
        
        # Tecla erronea que no sea WASDQEZC:
        else:
            print("Tecla no definida, recuerde solo pulsar WASD")


puntaje_del_raton = 0  # Inicializar fuera del ciclo



import copy

def es_movimiento_valido(tablero, x, y):
    return 0 <= x < len(tablero) and 0 <= y < len(tablero[0])

def obtener_movimientos_gato(tablero, pos_gato):
    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1), (-2, 0), (2, 0), (0, -2), (0, 2)]
    movimientos = []

    for dx, dy in direcciones:
        # Movimiento simple
        nx1, ny1 = pos_gato[0] + dx, pos_gato[1] + dy
        if es_movimiento_valido(tablero, nx1, ny1):
            movimientos.append((nx1, ny1))

    return movimientos

def distancia(a, b):
    return (abs(a[0] - b[0]) + abs(a[1] - b[1]))

def encontrar_raton(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            if tablero[i][j] == 'R':
                return (i, j)
    return None

def evaluar_gato(tablero, pos_gato):
    raton = encontrar_raton(tablero)
    if pos_gato == raton or raton is None:
        return 1000  # El gato ya ganó

    dist = distancia(pos_gato, raton)
    return -dist * 100  # Cuanto más cerca, mejor


def minimax_gato(tablero, pos_gato, profundidad, maximizando):
    if profundidad == 0:
        return evaluar_gato(tablero, pos_gato), pos_gato

    movimientos = obtener_movimientos_gato(tablero, pos_gato)
    if not movimientos:
        return evaluar_gato(tablero, pos_gato), pos_gato

    mejor_valor = float('-inf') if maximizando else float('inf')
    mejor_mov = pos_gato

    for mov in movimientos:
        nuevo_tablero = copy.deepcopy(tablero)
        x0, y0 = pos_gato
        x1, y1 = mov

        nuevo_tablero[x0][y0] = '.'
        nuevo_tablero[x1][y1] = 'G'


        valor, _ = minimax_gato(nuevo_tablero, mov, profundidad - 1, not maximizando)

        if maximizando and valor > mejor_valor:
            mejor_valor = valor
            mejor_mov = mov
        elif not maximizando and valor < mejor_valor:
            mejor_valor = valor
            mejor_mov = mov

    return mejor_valor, mejor_mov


def mover_gato_ia(tablero):
    pos_gato = None
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            if tablero[i][j] == 'G':
                pos_gato = (i, j)
                break
        if pos_gato:
            break


    _, mejor_mov = minimax_gato(tablero, pos_gato, profundidad = 2, maximizando=True)

    if mejor_mov != pos_gato:
        x0, y0 = pos_gato
        x1, y1 = mejor_mov
        tablero[x0][y0] = '.'
        tablero[x1][y1] = 'G'


while True:
    print("Turno del Raton:")
    turno_raton()
    print("")

    if tablero[x2][y2] == 'G':  # Verifica si en la posición del ratón está el gato
        tablero[x2][y2] = "💥"
        print("")
        mostrar_tablero(tablero)
        print("Gato Wins, Flawless Victory: Animallity")

        if x2 == 0 and y2 == 0:
            print("El Raton se ha escapado, el raton ha ganado")
            break
        break

    
    print("Turno del Gato:")
    mover_gato_ia(tablero)
    print("")
    mostrar_tablero(tablero)
    print("")

    if tablero[x2][y2] == 'G':  # Verifica si en la posición del ratón está el gato
        tablero[x2][y2] = "💥"
        print("")
        mostrar_tablero(tablero)
        print("Gato Wins, Flawless Victory: Animallity")
        break