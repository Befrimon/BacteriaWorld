import pygame


SCREEN = pygame.display.set_mode((1024, 600))
CLOCK = pygame.time.Clock()
FPS = 50
MOVEMENT = {
    pygame.K_UP: (),
    pygame.K_DOWN: (),
    pygame.K_RIGHT: (),
    pygame.K_LEFT: ()
}
ACTION_BUTTONS = (("do_heater", 50), ("do_colder", 150))


def draw_text(surf: pygame.Surface, text: str, size: int, x: int, y: int,
              delta_y: int = 0, color=(0, 0, 0), font_name='fonts/default.ttf', position="normal"):
    font = pygame.font.Font(pygame.font.match_font(font_name), size)
    line_text = text.split("\n")
    for line in range(len(line_text)):
        text_surface = font.render(line_text[line], True, color)
        text_rect = text_surface.get_rect()
        if position == "normal": text_rect.x, text_rect.y = x, y+size*line+delta_y
        elif position == "center": text_rect.centerx, text_rect.y = x, y+size*line+delta_y
        surf.blit(text_surface, text_rect)
