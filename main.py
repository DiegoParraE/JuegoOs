import pygame
import sys

from componentes.pantalla_inicio import mostrar_pantalla_inicio
from componentes.seleccion_sistema import mostrar_seleccion_sistema
from componentes.seleccion_cartas import mostrar_seleccion_cartas
from componentes.campo_batalla import mostrar_campo_batalla

# Inicia pygame
pygame.init()

# Configuración de la ventana
ANCHO = 1000
ALTO = 1000

pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Guerra Tecnológica")

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Guerra Tecnológica")

# Estados del juego
ESTADO_INICIO = "inicio"
ESTADO_SELECCION = "seleccion"
ESTADO_CARTAS = "cartas"
ESTADO_BATALLA = "batalla"

estado_actual = ESTADO_INICIO
reloj = pygame.time.Clock()
corriendo = True

# Variables de juego
sistema_elegido = None
cartas_seleccionadas = None

# Loop principal del juego
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    if estado_actual == ESTADO_INICIO:
        resultado = mostrar_pantalla_inicio(pantalla)
        if resultado == "jugar":
            estado_actual = ESTADO_SELECCION
        elif resultado == "instrucciones":
            print("Instrucciones aún no disponibles.")
        elif resultado == "salir":
            corriendo = False

    elif estado_actual == ESTADO_SELECCION:
        sistema_elegido = mostrar_seleccion_sistema(pantalla)
        if sistema_elegido:
            estado_actual = ESTADO_CARTAS

    elif estado_actual == ESTADO_CARTAS:
        cartas_seleccionadas = mostrar_seleccion_cartas(pantalla)
        if cartas_seleccionadas:
            estado_actual = ESTADO_BATALLA

    elif estado_actual == ESTADO_BATALLA:
        mostrar_campo_batalla(pantalla, sistema_elegido, cartas_seleccionadas)
        pygame.time.delay(5000)  # Por ahora lo mostramos 5 segundos
        corriendo = False  # Aquí luego haremos combate interactivo

    pygame.display.flip()
    reloj.tick(60)

# Salir del juego
pygame.quit()
sys.exit()
