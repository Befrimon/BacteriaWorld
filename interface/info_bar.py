from templates import SpriteTemplate
from const import draw_text
import pygame


class IBar(SpriteTemplate):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((224, 600))
        self.image.fill((30, 30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = 912, 300

        self.text = ""

    def set_text(self, info: str):
        self.text = info

    def draw(self, surface: pygame.Surface):
        draw_text(surface, self.text, 20, 810, 50)
