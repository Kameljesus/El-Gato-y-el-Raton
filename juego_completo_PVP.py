gato = "G"
raton = "R"
pared = "#"
vacio = "."
queso = "Q"


tablero = [
    [gato,  ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".",    "#", "#", "#", ".", "#", "#", "#", "#", "#", ".", ".", ".", ".", ".", "#", "#", "#", "#", "#", ".", "#", "#", "#", "."],
    [".",    "#", "#", "#", ".", "#", queso, ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", queso, "#", ".", "#", "#", "#", "."],
    [".",    "#", "#", "#", ".", "#", ".", "#", "#", "#", ".", ".", ".", ".", ".", "#", "#", "#", ".", "#", ".", "#", "#", "#", "."],
    [".",    ".", ".", ".", ".", "#", ".", "#", ".", ".", ".", "#", ".", "#", ".", ".", ".", "#", ".", "#", ".", ".", ".", ".", "."],
    [".",    ".", ".", ".", ".", "#", ".", "#", ".", ".", ".", "#", ".", "#", ".", ".", ".", "#", ".", "#", ".", ".", ".", ".", "."],
    [".",    "#", ".", "#", ".", ".", ".", ".", ".", "#", "#", "#", ".", "#", "#", "#", ".", ".", ".", ".", ".", "#", ".", "#", "."],
    [".",    "#", ".", "#", ".", ".", ".", ".", ".", ".", ".", ".", queso, ".", ".", ".", ".", ".", ".", ".", ".", "#", ".", "#", "."],
    [".",    "#", ".", "#", ".", ".", ".", ".", ".", "#", "#", "#", ".", "#", "#", "#", ".", ".", ".", ".", ".", "#", ".", "#", "."],
    [".",    ".", ".", ".", ".", "#", ".", "#", ".", ".", ".", "#", ".", "#", ".", ".", ".", "#", ".", "#", ".", ".", ".", ".", "."],
    [".",    ".", ".", ".", ".", "#", ".", "#", ".", ".", ".", "#", ".", "#", ".", ".", ".", "#", ".", "#", ".", ".", ".", ".", "."],
    [".",    "#", "#", "#", ".", "#", ".", "#", "#", "#", ".", ".", ".", ".", ".", "#", "#", "#", ".", "#", ".", "#", "#", "#", "."],
    [".",    "#", "#", "#", ".", "#", queso, ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", queso, "#", ".", "#", "#", "#", "."],
    [".",    "#", "#", "#", ".", "#", "#", "#", "#", "#", ".", ".", ".", ".", ".", "#", "#", "#", "#", "#", ".", "#", "#", "#", "."],
    [".",    ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", raton]
]


x1, y1 = 0, 0
x2, y2 = 14, 24
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

            if x1 > 14 or x1 < 0 or y1 > 24 or y1 < 0:
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
            
            if x1 > 14 or x1 < 0 or y1 > 24 or y1 < 0:
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
            
            if x1 > 14 or x1 < 0 or y1 > 24 or y1 < 0:
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

            if x1 > 14 or x1 < 0 or y1 > 24 or y1 < 0:
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
            
            if x1 > 14 or x1 < 0 or y1 > 24 or y1 < 0:
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
            
            if x2 > 14 or x2 < 0 or y2 > 24 or y2 < 0:
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
            
            if x2 > 14 or x2 < 0 or y2 > 24 or y2 < 0:
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
            
            if x2 > 14 or x2 < 0 or y2 > 24 or y2 < 0:
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
            
            if x2 > 14 or x2 < 0 or y2 > 24 or y2 < 0:
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
            
            if x2 > 14 or x2 < 0 or y2 > 24 or y2 < 0:
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
            
            if x2 > 14 or x2 < 0 or y2 > 24 or y2 < 0:
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
            
            if x2 > 14 or x2 < 0 or y2 > 24 or y2 < 0:
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
            
            if x2 > 14 or x2 < 0 or y2 > 24 or y2 < 0:
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
            
            if x2 > 14 or x2 < 0 or y2 > 24 or y2 < 0:
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
            
            if x2 > 14 or x2 < 0 or y2 > 24 or y2 < 0:
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
            
            if x2 > 14 or x2 < 0 or y2 > 24 or y2 < 0:
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
            
            if x2 > 14 or x2 < 0 or y2 > 24 or y2 < 0:
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

while True:
    print("Turno del Gato:")
    turno_gato()

    if x1 == x2 and y1 == y2:
        tablero[x1][y1] = "💥"
        print("")
        mostrar_tablero(tablero)
        print("Gato Wins, Flawless Victory: Animallity")
        break

    print("Turno del Raton:")
    turno_raton()

    if puntaje_del_raton >= 5:
        print("Raton gana, has recogido 5 quesos!")
        break

    elif x2 == 0 and y2 == 0:
        print("El Raton se ha escapado, el raton ha ganado")
        break
    