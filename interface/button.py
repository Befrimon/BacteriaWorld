from interface.texture import Texture
from templates import GroupTemplate
import pygame


class Button:
    def __init__(self, img: str, x: int, y: int):
        self.tex = GroupTemplate()
        self.tex.add(Texture("buttons/static_button.png", x, y), Texture(f"buttons/{img}.png", x, y))

    def draw(self, surface: pygame.Surface):
        self.tex.draw(surface)

    def move_cursor(self, event: pygame.event.Event):
        if event.type != pygame.MOUSEMOTION: return
        origin = self.tex.sprites()[0]
        if origin.rect.x <= event.pos[0] <= origin.rect.x + 60 and origin.rect.y <= event.pos[1] <= origin.rect.y + 60:
            origin.image = pygame.image.load("buttons/active_button.png")

