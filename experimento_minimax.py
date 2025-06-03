gato = "G"
raton = "R"
vacio = "."

tablero = [
    ["O", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", "G", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "R"]
]


x1, y1 = 2, 2
x2, y2 = 6, 12


def fuera_del_mapa():
    print("")
    print("Movimiento no Permitido: Juegue dentro del mapa")

def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))

print("Bienvenido al juego del Gato y el Raton:")
print("")

# Llamada a la función para mostrar el tablero:
mostrar_tablero(tablero)
print("")

def turno_raton():
    global x2, y2
    
    while True:
        movimiento_raton = input("Raton, haga su movimiento (W-A-S-D-Q-E-Z-C):").lower()
        

        # Moviento hacia arriba:
        if movimiento_raton == "w":
            tablero[x2][y2] = vacio
            x2 = x2 - 1
            
            if x2 > 6 or x2 < 0 or y2 > 12 or y2 < 0:
                fuera_del_mapa()
                x2 = x2 + 1

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

            else:
                tablero[x2][y2] = raton
                print("")
                mostrar_tablero(tablero)
                break
        
        # Tecla erronea que no sea WASDQEZC:
        else:
            print("Tecla no definida, recuerde solo pulsar WASD")


# Minimax:
import copy

def movimientos_validos(x1, y1):
    return 0 <= x1 < len(tablero) and 0 <= y1 < len(tablero[0])
    
    # len(tablero) te dice cuantas filas hay.
    # len(tablero[0]) te dice cuantas columnas tiene cada fila desde su la fila [0].

def movimiento_disponibles_gato(tablero, x1, y1):
    # Direcciones rectas simples: arriba, abajo, izquierda, derecha:
    # rectos_simples = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Direcciones rectas dobles: arriba, abajo, izquierda, derecha:
    # rectos_dobles = [(-2, 0), (2, 0), (0, -2), (0, 2)]

    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1), (-2, 0), (2, 0), (0, -2), (0, 2)]
    
    movimientos_gato = []

    for desplazamiento_x1, desplazamiento_y1 in direcciones:
        nueva_x1 = x1 + desplazamiento_x1
        nueva_y1 = y1 + desplazamiento_y1

        if 0 <= nueva_x1 < len(tablero) and 0 <= nueva_y1 < len(tablero[0]):
            movimientos_gato.append((nueva_x1, nueva_y1))

    return movimientos_gato


def distancia_manhattan(posicion_gato, posicion_raton):
    x1, y1 = posicion_gato
    x2, y2 = posicion_raton
    distancia = abs(x1 - x2) + abs(y1 - y2)
    return distancia


def decirle_a_gato_donde_raton(tablero):
    for x2 in range(len(tablero)):
        for y2 in range(len(tablero[0])):
            if tablero[x2][y2] == 'R':
                return (x2, y2)
    return None


def evaluar_gato(tablero, posicion_gato):
    posicion_raton = decirle_a_gato_donde_raton(tablero)
    if posicion_gato == posicion_raton:
        return 1000  # El gato ya ganó

    dist = distancia_manhattan(posicion_gato, posicion_raton)
    return -dist * 100  # Cuanto más cerca, mejor

    # Ejemplo:

    # Si el gato está a 3 pasos del ratón:
    
    # dist = 3

    # return -3 * 100 → -300

    # 1000 - 300 = 700

    # Si el gato lo alcanza:

    # gato == raton → retorna 1000


def minimax_gato(tablero, posicion_gato, profundidad, maximizando):
    
    if profundidad == 0:
        return evaluar_gato(tablero, posicion_gato), posicion_gato
    
    # Si ya alcanzamos la profundidad máxima (es decir, ya miramos suficientes movimientos hacia adelante), 
    # se detiene la simulación y se evalúa qué tan buena es la posición actual del gato.

    mejor_valor = float('-inf') if maximizando else float('inf')
    mejor_movimiento = posicion_gato

# ¿Qué significa maximizando?

    # Este parámetro le indica al algoritmo Minimax quién juega en ese turno:
    # Valor de maximizando	Significa que...
    # True	Juega el Gato (IA), que quiere maximizar su puntaje.
    # False	Jugaría el Ratón o el "otro jugador", que intenta minimizar el puntaje del Gato.


    # float('-inf'): representa el número más bajo posible → empieza desde lo peor, así cualquier valor real será mejor.

    # float('inf'): representa el número más alto posible → empieza desde lo mejor, así cualquier valor real será peor.

    x1, y1 = posicion_gato

    for movimiento_a_seguir in movimiento_disponibles_gato(tablero, x1, y1):
        nuevo_tablero = copy.deepcopy(tablero)
        nueva_x1, nueva_y1 = movimiento_a_seguir

        nuevo_tablero[x1][y1] = '.'
        nuevo_tablero[nueva_x1][nueva_y1] = 'G'


        valor, _ = minimax_gato(nuevo_tablero, movimiento_a_seguir, profundidad - 1, not maximizando)


        if maximizando and valor > mejor_valor:
            mejor_valor = valor
            mejor_movimiento = movimiento_a_seguir
        
        elif not maximizando and valor < mejor_valor:
            mejor_valor = valor
            mejor_movimiento = movimiento_a_seguir

    return mejor_valor, mejor_movimiento


def mover_gato_ia(tablero):
    posicion_gato = None
    for x1 in range(len(tablero)):
        for y1 in range(len(tablero[0])):
            if tablero[x1][y1] == 'G':
                posicion_gato = (x1, y1)
                break
        if posicion_gato:
            break


    _, mejor_movimiento = minimax_gato(tablero, posicion_gato, profundidad = 2, maximizando=True)

    if mejor_movimiento != posicion_gato:
        nueva_x1, nueva_y1 = mejor_movimiento
        tablero[x1][y1] = '.'
        tablero[nueva_x1][nueva_y1] = 'G'


while True:
    print("Turno del Raton:")
    turno_raton()

    if x2 == 0 and y2 == 0:
        print("El Raton se ha escapado, el raton ha ganado")
        break

    print("Turno del Gato:")
    mover_gato_ia(tablero)

    if x1 == x2 and y1 == y2:
        tablero[x1][y1] = "💥"
        print("")
        mostrar_tablero(tablero)
        print("Gato Wins, Flawless Victory: Animallity")
        break
    