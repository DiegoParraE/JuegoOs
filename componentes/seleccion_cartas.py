import pygame
import random

# Tipos de cartas
TIPOS = ["ATQ", "DEF", "CUR"]

# Colores por tipo
COLORES = {
    "ATQ": (200, 50, 50),
    "DEF": (50, 200, 50),
    "CUR": (50, 50, 200)
}

# Crear una matriz de cartas aleatorias
def generar_matriz_cartas(filas=4, columnas=4):
    matriz = []
    for _ in range(filas):
        fila = []
        for _ in range(columnas):
            tipo = random.choice(TIPOS)
            valor = random.randint(1, 9)
            fila.append({"tipo": tipo, "valor": valor, "seleccionada": False})
        matriz.append(fila)
    return matriz

matriz_cartas = generar_matriz_cartas()

def mostrar_seleccion_cartas(pantalla):
    pantalla.fill((40, 40, 40))
    fuente = pygame.font.SysFont(None, 40)
    blanco = (255, 255, 255)

    titulo = fuente.render("Selecciona tus cartas", True, blanco)
    pantalla.blit(titulo, (250, 30))

    tam_carta = 80
    margen = 20
    offset_x = 120
    offset_y = 100

    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    for i, fila in enumerate(matriz_cartas):
        for j, carta in enumerate(fila):
            x = offset_x + j * (tam_carta + margen)
            y = offset_y + i * (tam_carta + margen)
            rect = pygame.Rect(x, y, tam_carta, tam_carta)

            color = COLORES[carta["tipo"]]
            if carta["seleccionada"]:
                pygame.draw.rect(pantalla, (255, 255, 0), rect)
            else:
                pygame.draw.rect(pantalla, color, rect)

            texto = pygame.font.SysFont(None, 24).render(f"{carta['tipo']} {carta['valor']}", True, blanco)
            pantalla.blit(texto, (x + 10, y + 25))

            if rect.collidepoint(mouse_pos) and click[0]:
                carta["seleccionada"] = not carta["seleccionada"]
                pygame.time.delay(150)

    # Botón continuar
    continuar_rect = pygame.Rect(600, 500, 150, 50)
    pygame.draw.rect(pantalla, blanco, continuar_rect)
    texto = pygame.font.SysFont(None, 30).render("CONTINUAR", True, (0, 0, 0))
    pantalla.blit(texto, (continuar_rect.x + 10, continuar_rect.y + 10))

    if continuar_rect.collidepoint(mouse_pos) and click[0]:
        pygame.time.delay(200)
        return matriz_cartas

    return None
