from templates import SpriteTemplate
import pygame


class Texture(SpriteTemplate):
    def __init__(self, path: str, x: int, y: int):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(f"images/{path}")
        self.rect = self.image.get_rect()
        self.rect.center = x, y
