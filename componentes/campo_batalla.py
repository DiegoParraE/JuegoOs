import pygame
import random
import sys

pygame.init()

from componentes.aplicar_cartas import aplicar_cartas
from componentes.calcular_combate import calcular_combate  # Si usas esta función

ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Batalla Drag and Drop")

blanco = (255, 255, 255)
negro = (0, 0, 0)

fuente = pygame.font.SysFont(None, 40)
fuente_info = pygame.font.SysFont(None, 28)

slot_size = 80

# --- Clase Carta ---
class Carta:
    def __init__(self, tipo, imagen, x, y):
        self.tipo = tipo  # 'ataque', 'defensa', 'salud'
        self.imagen = imagen
        self.rect = imagen.get_rect(topleft=(x, y))
        self.arrastrando = False
        self.colocada = False

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, self.rect.topleft)

# --- Crear espacios de la matriz 3x3 ---
espacios_cartas = [[None for _ in range(3)] for _ in range(3)]
espacios_posiciones = []
for fila in range(3):
    fila_pos = []
    for col in range(3):
        x = 20 + col * (slot_size + 10)
        y = 100 + fila * (slot_size + 10)
        fila_pos.append(pygame.Rect(x, y, slot_size, slot_size))
    espacios_posiciones.append(fila_pos)

# --- Crear cartas jugador ---
cartas_jugador = []
colores = {
    'ataque': (200, 0, 0),
    'defensa': (0, 200, 0),
    'salud': (0, 0, 200)
}

for i, tipo in enumerate(['ataque', 'defensa', 'salud']):
    for j in range(3):
        imagen = pygame.Surface((60, 90))
        imagen.fill(colores[tipo])
        carta = Carta(tipo, imagen, 150 + j * 70, 500 + i % 1 * 10)  # Reposo inicial
        cartas_jugador.append(carta)

# --- Entidades ---
sistema = {"nombre": "Jugador (Windows)", "ataque": 10, "defensa": 10, "vida": 100}
jugador = aplicar_cartas(sistema, cartas_jugador)
cpu = {"nombre": "CPU (macOS)", "ataque": random.randint(5, 15), "defensa": random.randint(5, 15), "vida": 100}

def mostrar_stats(entidad, x, y, daño):
    pantalla.blit(fuente_info.render(f"{entidad['nombre']}", True, blanco), (x, y))
    pantalla.blit(fuente_info.render(f"ATQ: {entidad['ataque']}", True, blanco), (x, y + 30))
    pantalla.blit(fuente_info.render(f"DEF: {entidad['defensa']}", True, blanco), (x, y + 60))
    pantalla.blit(fuente_info.render(f"VIDA: {entidad['vida']} (-{daño})", True, blanco), (x, y + 90))

def realizar_turno(jugador, cpu):
    daño_jugador = max(jugador["ataque"] - cpu["defensa"], 5)
    daño_cpu = max(cpu["ataque"] - jugador["defensa"], 5)
    cpu["vida"] -= daño_jugador
    jugador["vida"] -= daño_cpu
    return daño_jugador, daño_cpu

def todas_cartas_colocadas():
    return all(carta.colocada for carta in cartas_jugador)

def mostrar_campo_batalla():
    ganador = None
    turno = 1
    offset_x, offset_y = 0, 0
    jugador_ya_jugo = False

    while jugador["vida"] > 0 and cpu["vida"] > 0:
        pantalla.fill(negro)
        pantalla.blit(fuente.render("¡Batalla por turnos!", True, blanco), (250, 20))
        pantalla.blit(fuente.render(f"Turno {turno}", True, blanco), (340, 60))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                for carta in cartas_jugador:
                    if carta.rect.collidepoint(evento.pos):
                        carta.arrastrando = True
                        offset_x = carta.rect.x - evento.pos[0]
                        offset_y = carta.rect.y - evento.pos[1]

            elif evento.type == pygame.MOUSEBUTTONUP:
                for carta in cartas_jugador:
                    if carta.arrastrando:
                        carta.arrastrando = False
                        for i in range(3):
                            for j in range(3):
                                if espacios_posiciones[i][j].collidepoint(evento.pos) and espacios_cartas[i][j] is None:
                                    carta.rect.topleft = espacios_posiciones[i][j].topleft
                                    espacios_cartas[i][j] = carta
                                    carta.colocada = True
                                    break

            elif evento.type == pygame.MOUSEMOTION:
                for carta in cartas_jugador:
                    if carta.arrastrando:
                        carta.rect.x = evento.pos[0] + offset_x
                        carta.rect.y = evento.pos[1] + offset_y

        # Mostrar matriz de slots
        for fila in espacios_posiciones:
            for slot in fila:
                pygame.draw.rect(pantalla, (50, 50, 50), slot, 2)

        # Dibujar entidades
        pygame.draw.rect(pantalla, (0, 0, 255), (300, 100, 100, 150))  # Jugador
        pygame.draw.rect(pantalla, (255, 0, 0), (500, 100, 100, 150))  # CPU

        # Dibujar cartas
        for carta in cartas_jugador:
            carta.dibujar(pantalla)

        mostrar_stats(jugador, 300, 270, 0)
        mostrar_stats(cpu, 500, 270, 0)

        pygame.display.update()

        # Esperar a que jugador termine su turno
        if todas_cartas_colocadas() and not jugador_ya_jugo:
            daño_jugador, daño_cpu = realizar_turno(jugador, cpu)
            mostrar_stats(jugador, 300, 270, daño_cpu)
            mostrar_stats(cpu, 500, 270, daño_jugador)
            pygame.display.update()
            pygame.time.delay(1500)
            turno += 1
            jugador_ya_jugo = True

    pantalla.fill(negro)
    if jugador["vida"] > cpu["vida"]:
        ganador = jugador["nombre"]
    elif cpu["vida"] > jugador["vida"]:
        ganador = cpu["nombre"]
    else:
        ganador = "Empate"

    pantalla.blit(fuente.render("¡Batalla terminada!", True, blanco), (250, 200))
    pantalla.blit(fuente.render(f"Ganador: {ganador}", True, blanco), (270, 280))
    pygame.display.update()
    pygame.time.delay(3000)

mostrar_campo_batalla()
