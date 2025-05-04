import pygame

def mostrar_pantalla_inicio(pantalla):
    fuente = pygame.font.SysFont(None, 60)
    blanco = (255, 255, 255)
    gris = (200, 200, 200)
    negro = (0, 0, 0)

    pantalla.fill((30, 30, 30))

    # Texto del título
    titulo = fuente.render("GUERRA TECNOLÓGICA", True, blanco)
    pantalla.blit(titulo, (250, 100))

    # Botones
    botones = {
        "jugar": pygame.Rect(325, 250, 150, 50),
        "instrucciones": pygame.Rect(325, 320, 150, 50),
        "salir": pygame.Rect(325, 390, 150, 50),
    }

    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    for nombre, rect in botones.items():
        color = gris if rect.collidepoint(mouse_pos) else blanco
        pygame.draw.rect(pantalla, color, rect)
        texto = pygame.font.SysFont(None, 30).render(nombre.upper(), True, negro)
        pantalla.blit(texto, (rect.x + 20, rect.y + 10))

        if rect.collidepoint(mouse_pos) and click[0]:
            pygame.time.delay(200)  # Pequeño retraso para evitar doble clic
            return nombre

    return None
