from templates import SpriteTemplate
from bacteria import decode
import pygame
import random


class Bacteria(SpriteTemplate):
    def __init__(self, world, position: tuple):
        pygame.sprite.Sprite.__init__(self)

        # set render param
        self.image = pygame.Surface((10, 10))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position

        # set life param
        self.arial = world
        self.energy = 100
        self.dna = [27]*32
        self.active = 0

        # set characteristic param
        self.autotroph = 0
        self.heterotroph = 0
        self.scavenger = 0
        self.eaten = 0

    def set_dna(self, new_dna: list):
        self.dna = new_dna

    def mutate(self, index: int, new_code: int = random.randint(10, 99)):
        self.dna[index] = new_code

    def cur_motion(self, event: pygame.event.Event):
        if event.type != pygame.MOUSEMOTION: return

    def update(self):
        state = decode.proc(self, self.dna[self.active])
        self.active += state
        if self.active >= 32: self.active -= 32


