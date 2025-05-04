import pygame

SISTEMAS = {
    "Windows": {"ataque": 8, "defensa": 4, "especial": 6},
    "Linux": {"ataque": 4, "defensa": 9, "especial": 5},
    "macOS": {"ataque": 6, "defensa": 6, "especial": 8},
}

def mostrar_seleccion_sistema(pantalla):
    pantalla.fill((50, 50, 80))
    fuente = pygame.font.SysFont(None, 40)
    blanco = (255, 255, 255)
    negro = (0, 0, 0)
    gris = (200, 200, 200)

    titulo = fuente.render("Elige tu Sistema Operativo", True, blanco)
    pantalla.blit(titulo, (220, 50))

    botones = {}
    x = 100
    for nombre, stats in SISTEMAS.items():
        rect = pygame.Rect(x, 150, 200, 200)
        botones[nombre] = rect
        pygame.draw.rect(pantalla, gris, rect)

        texto = pygame.font.SysFont(None, 30).render(nombre, True, negro)
        pantalla.blit(texto, (rect.x + 50, rect.y + 10))

        stat_texto = f"ATQ: {stats['ataque']} DEF: {stats['defensa']} ESP: {stats['especial']}"
        pantalla.blit(pygame.font.SysFont(None, 24).render(stat_texto, True, negro), (rect.x + 10, rect.y + 60))
        x += 250

    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    for nombre, rect in botones.items():
        if rect.collidepoint(mouse_pos):
            pygame.draw.rect(pantalla, (255, 255, 0), rect, 3)
            if click[0]:
                pygame.time.delay(200)
                return {"nombre": nombre, **SISTEMAS[nombre]}

    return None
