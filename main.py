from bacteria import bacterias
from interface import UI
from const import *
import pygame


pygame.init()
pygame.display.set_caption("Bacterias")


while True:
    CLOCK.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        UI.update_events(event)
        bacterias.update_events(event)

    UI._process(SCREEN)
    bacterias._process(SCREEN)

    pygame.display.flip()
