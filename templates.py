import pygame


class SpriteTemplate(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

    def update(self): pass
    def draw(self, surface: pygame.Surface): pass
    def cur_motion(self, event: pygame.event.Event): pass


class GroupTemplate(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

    def _process(self, surface: pygame.Surface):
        self.draw(surface)
        for sprite in self.sprites():
            sprite: SpriteTemplate
            sprite.update()
            sprite.draw(surface)

    def update_events(self, event: pygame.event.Event):
        for sprite in self.sprites():
            sprite: SpriteTemplate
            sprite.cur_motion(event)
