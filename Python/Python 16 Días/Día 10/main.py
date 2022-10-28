# Importamos Libreria desde pip install pygame
import pygame
from pygame import mixer
import random
import math

# Inicializamos pygame para poder trabajar con él
pygame.init()

# Creamos una pantalla. En una tupla enviamos el ancho y el alto que tendra la pantalla.
pantalla = pygame.display.set_mode((800, 600))

# Configuracion de icono y titulo del juego
# Nombre del juego (pantalla)
pygame.display.set_caption("Invasión Espacial")
# Icono para la pantalla del juego
icono = pygame.image.load("C:\\Programming\\MyLearning\\Python\\Python 16 Días\\Día 10\\ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("C:\\Programming\\MyLearning\\Python\\Python 16 Días\\Día 10\\Fondo.jpg")

# Msuica
mixer.music.load("C:\\Programming\\MyLearning\\Python\\Python 16 Días\\Día 10\\MusicaFondo.mp3")
mixer.music.play(-1)

# Jugador
img_jugador = pygame.image.load("C:\\Programming\\MyLearning\\Python\\Python 16 Días\\Día 10\\cohete.png")
jugador_x = 368
jugador_y = 500
jugar_x_cambio = 0
jugar_y_cambio = 0

# LISTA
cantidad_enemigos = 8
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []

# Enemigo
for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("C:\\Programming\\MyLearning\\Python\\Python 16 Días\\Día 10\\enemigo.png"))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambio.append(0.5)
    enemigo_y_cambio.append(50)


# Bala
img_bala = pygame.image.load("C:\\Programming\\MyLearning\\Python\\Python 16 Días\\Día 10\\bala.png")
bala_x = 0
bala_y = 400
bala_x_cambio = 0
bala_y_cambio = 2
bala_visible = False

# Puntos
puntaje = 0
fuente = pygame.font.Font("freesansbold.ttf", 32)
texto_x = 10
texto_y = 10
# Texto final
fuente_final = pygame.font.Font("freesansbold.ttf", 45)

def texto_final():
    mi_fuente_final = fuente_final.render("GAME OVER", True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (60, 200))

def mostrar_puntuaje(x, y):
    texto = fuente.render(f"Puntuaje: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto, (x, y))

def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))

def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))    

def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))

# Funcion Detectar Coliciones
def hay_colicones(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_1 - y_2, 2))
    if distancia <= 27:
        return True
    else:
        return False
    

# Variable para determinar si el juego se debe ejecutar o no
se_ejecuta = True

# En Pygame todo es un evento, clic, presion de teclas, etc.
while se_ejecuta:
    # RGB de pantalla
    #pantalla.fill((164, 141, 178))
    # Imagen de fondo
    pantalla.blit(fondo, (0,0))
    # Mover al jugador
    
    # Recorreremos la lista completa de eventos de Pygame
    for evento in pygame.event.get():
        # Cuando nuestro evento sea igual el evento de salir (x en ventana) saldra
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        
        # Eventos para determinar que flecha fue presionada 
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                # Establece valores para mover al jugardor
                jugar_x_cambio = -0.5
            if evento.key == pygame.K_RIGHT:
                jugar_x_cambio = 0.5
            if evento.key == pygame.K_UP:
                jugar_y_cambio = -0.5
            if evento.key == pygame.K_DOWN:
                jugar_y_cambio = 0.5
            # Disparar al presionar espacio
            if evento.key == pygame.K_SPACE:
                sondio_bala = mixer.Sound("C:\\Programming\\MyLearning\\Python\\Python 16 Días\\Día 10\\disparo.mp3")
                sondio_bala.play()
                if bala_visible == False:
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)
        
        # Evento para cuando la tecla deje de ser presionada, se vuelte
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugar_x_cambio = 0
            if evento.key == pygame.K_UP or evento.key == pygame.K_DOWN:
                jugar_y_cambio = 0
        

    # Modificar valores en vace a cuanto se presiona la tecla
    jugador_x += jugar_x_cambio
    jugador_y += jugar_y_cambio

    # Mantener dentro de bordes
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    if jugador_y <= 0:
        jugador_y = 0
    elif jugador_y >= 536:
        jugador_y = 536
    
    # Modidicar valores enemigo
    for e in range(cantidad_enemigos):
        #Fin del juego
        if enemigo_y[e] > 500:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break
        enemigo_x[e] += enemigo_x_cambio[e]
    
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.5
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -0.5
            enemigo_y[e] += enemigo_y_cambio[e]

        # Colicion
        colision = hay_colicones(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if colision == True:
            sondio_colision = mixer.Sound("C:\\Programming\\MyLearning\\Python\\Python 16 Días\\Día 10\\Golpe.mp3")
            bala_y = 500
            bala_visible = False
            puntaje += 1
            enemigo_x[e] = random.randint(0, 736)
            enemigo_y[e] = random.randint(50, 200)

        enemigo(enemigo_x[e], enemigo_y[e], e)
    
    # Movimiento BALA
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False
    if bala_visible == True:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio



    # Mostrar Jugador en pantalla
    jugador(jugador_x, jugador_y)
    mostrar_puntuaje(texto_x, texto_y)
    pygame.display.update()




