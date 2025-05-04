import pygame
import random
from componentes.aplicar_cartas import aplicar_cartas  # Asegúrate de tener este archivo y función
from componentes.calcular_combate import calcular_combate  # Si usas una función aparte para combate

def mostrar_campo_batalla(pantalla, sistema, cartas):
    fuente = pygame.font.SysFont(None, 40)
    fuente_info = pygame.font.SysFont(None, 28)
    blanco = (255, 255, 255)

    jugador = aplicar_cartas(sistema, cartas)
    cpu = {
        "nombre": "CPU (macOS)",
        "ataque": random.randint(5, 15),
        "defensa": random.randint(5, 15),
        "vida": 100
    }

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

    ganador = None
    turno = 1

    while jugador["vida"] > 0 and cpu["vida"] > 0:
        pantalla.fill((0, 0, 0))
        pantalla.blit(fuente.render("¡Batalla por turnos!", True, blanco), (250, 20))
        pantalla.blit(fuente.render(f"Turno {turno}", True, blanco), (340, 60))

        daño_jugador, daño_cpu = realizar_turno(jugador, cpu)

        pygame.draw.rect(pantalla, (0, 0, 255), (100, 100, 200, 150))  # Jugador
        pygame.draw.rect(pantalla, (255, 0, 0), (500, 100, 200, 150))  # CPU

        mostrar_stats(jugador, 110, 270, daño_cpu)
        mostrar_stats(cpu, 510, 270, daño_jugador)

        pygame.display.update()
        pygame.time.delay(1500)
        turno += 1

    if jugador["vida"] > cpu["vida"]:
        ganador = jugador["nombre"]
    elif cpu["vida"] > jugador["vida"]:
        ganador = cpu["nombre"]
    else:
        ganador = "Empate"

    pantalla.fill((0, 0, 0))
    pantalla.blit(fuente.render("¡Batalla terminada!", True, blanco), (250, 200))
    pantalla.blit(fuente.render(f"Ganador: {ganador}", True, blanco), (270, 280))
    pygame.display.update()
    pygame.time.delay(3000)
