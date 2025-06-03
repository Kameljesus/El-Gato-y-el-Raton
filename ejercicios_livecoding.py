## Ejercicio 1: completar movimientos del ratón:

def movimientos_disponibles_raton(tablero, x2, y2):
    direcciones_diagonales = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    movimientos = []

    for dx, dy in direcciones_diagonales:
        nueva_x = x2 + dx
        nueva_y = y2 + dy

        # 👇 COMPLETAR: verificar si la posición es válida (dentro del tablero y no una pared)
        if 0<= nueva_x < len(tablero) and 0<= nueva_y < len(tablero[0]) and tablero[nueva_x][nueva_y] != "#":
            movimientos.append((nueva_x, nueva_y))

    return movimientos



## Ejercicio 2: evaluar la posición para el ratón:

def evaluar_raton(tablero, posicion_raton):
    # 👇 COMPLETAR: encontrar posición del gato
    posicion_gato = None  # ...
    for x1 in range(len(tablero)):
        for y1 in range(len(tablero[0])):
            if tablero[x1][y1] == "G":
                posicion_gato = (x1, y1)  
  
    if posicion_gato is None:
        return 1000  # El ratón ganó (no hay gato)

    if posicion_raton == posicion_gato:
        return -1000  # El gato atrapó al ratón

    # 👇 COMPLETAR: calcular distancia Manhattan y convertirla en una puntuación alta si están lejos
    x1, y1 = posicion_gato
    x2, y2 = posicion_raton
    distancia_manhattan = abs(x1 - x2) + abs(y1 - y2)
    dist = distancia_manhattan * -100 
    return dist



## Ejercicio 3: completar un paso del minimax:

def minimax_raton(tablero, posicion_raton, profundidad):
    if profundidad == 0:
        return evaluar_raton(tablero, posicion_raton), posicion_raton

    mejor_valor = float('inf')
    mejor_movimiento = posicion_raton

    for movimiento in movimientos_disponibles_raton(tablero, *posicion_raton):
        nuevo_tablero = copy.deepcopy(tablero)
        x2, y2 = posicion_raton
        nueva_x2, nueva_y2 = movimiento

        nuevo_tablero[x2][y2] = '.'
        nuevo_tablero[nueva_x2][nueva_y2] = 'R'

        # 👇 COMPLETAR: llamada recursiva al minimax
        valor, _ = minimax_raton(nuevo_tablero, movimiento, profundidad -1)

        # 👇 COMPLETAR: actualizar mejor_valor y mejor_movimiento si el valor es menor
        if mejor_valor > valor:
            mejor_valor = valor 
            mejor_movimiento = movimiento

    return mejor_valor, mejor_movimiento



## Ejercicio 1: Movimientos del Guardián:

def movimientos_guardian(tablero, fila_guardian, col_guardian):
    # Movimiento posible: vertical y horizontal 1 paso
    posibles = []
    direcciones = [(1,0), (-1,0), (0,1), (0,-1)]

    for dx, dy in direcciones:
        nueva_fila = fila_guardian + dx
        nueva_col = col_guardian + dy

        # 👇 COMPLETAR: valida que la nueva posición esté dentro del tablero y no haya muro '*'
        if nueva_fila >= 0 and nueva_fila < len(tablero) and nueva_col >= 0 and nueva_col < len(tablero[0]) and tablero[nueva_fila][nueva_col] != '*':
            posibles.append((nueva_fila, nueva_col))

    return posibles



## Ejercicio 2: Evaluación del Rey:

def evaluar_rey(tablero, pos_rey):
    pos_torre = None

    # 👇 COMPLETAR: Buscar la posición de la torre 'T' en el tablero
    encontrada = False
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            if tablero[i][j] == 'T':
                pos_torre = (i, j)
                encontrada = True
                break
        
        if encontrada:
            break
    

    if pos_torre is None:
        return 999  # La torre fue capturada, gana el rey

    xr, yr = pos_rey
    xt, yt = pos_torre

    if pos_rey == pos_torre:
        return -999  # El rey fue capturado

    # 👇 COMPLETAR: Calcular distancia Manhattan invertida para la puntuación
    distancia = -(abs(xr - xt) + abs(yr - yt))
    puntuacion = 999 + distancia  # Pista: mientras más lejos, mejor

    return puntuacion



## Ejercicio 3: Minimax del Rey:

def minimax_rey(tablero, pos_rey, prof, es_max):
    if prof == 0:
        return evaluar_rey(tablero, pos_rey), pos_rey

    if es_max:
        mejor_val = float('-inf')
        mejor_mov = pos_rey
        for mov in movimientos_rey(tablero, *pos_rey):
            tablero_copia = copy.deepcopy(tablero)
            x, y = pos_rey
            nx, ny = mov

            tablero_copia[x][y] = '.'
            tablero_copia[nx][ny] = 'R'

            val, _ = minimax_rey(tablero_copia, mov, prof - 1, False)

            # 👇 COMPLETAR: actualizar mejor valor y movimiento si val es mayor
            if mejor_val < val:
                mejor_val = val
                mejor_mov = mov

    else:
        pos_torre = None
        for x in range(len(tablero)):
            for y in range(len(tablero[0])):
                if tablero[x][y] == 'T':
                        pos_torre = (x, y)
                        break
            
            if pos_torre is not None:
                break
        
        mejor_val = float('inf')
        mejor_mov = pos_rey
        for mov in movimientos_torre(tablero, *pos_torre):
            tablero_copia = copy.deepcopy(tablero)
        

            x, y = pos_torre
            nx, ny = mov

            tablero_copia[x][y] = '.'
            tablero_copia[nx][ny] = 'T'

            val, _ = minimax_rey(tablero_copia, mov, prof - 1, True)

            # 👇 COMPLETAR: actualizar mejor valor y movimiento si val es menor
            if mejor_val > val:
                mejor_val = val
                mejor_mov = mov

    return mejor_val, mejor_mov



