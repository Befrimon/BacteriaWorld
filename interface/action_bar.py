from interface.button import Button
from const import ACTION_BUTTONS
from templates import *
import pygame


class ABar(SpriteTemplate):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((1024, 100))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.center = 512, 550

        self.buttons = []
        for btn in ACTION_BUTTONS:
            self.buttons.append(Button(btn[0], btn[1], 550))

    def update(self):
        pass

    def draw(self, surface: pygame.Surface):
        for btn in self.buttons:  btn.draw(surface)

