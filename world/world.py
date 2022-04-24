from  templates import GroupTemplate
import random
import pygame
import const


class World:
    def __init__(self):
        # Add it later
        # self.oxygen = 0
        # self.water = 0
        # self.radioactivity = 0
        self.temperature = 10
        self.temperature_range = {
            0: (0, 10), 1: (8, 20),
            2: (-2, 10), 3: (-10, 0)
        }  # 0 - spring; 1 - summer; 2 - autumn; # 3 - winter

        self.width = 800
        self.height = 500
        self.x, self.y = 0, 0

        self.year = 0
        self.season = 0
        self.day = 0
        self.time = 0
        self.bacterias = GroupTemplate()

    def _process(self):
        self.time += 1
        if self.time == 1024:
            self.next_day()
            self.time = 0

    def _key_pressed(self, event: pygame.event.Event):
        if event.type != pygame.KEYDOWN: return
        self.x += const.MOVEMENT[event.key][0]
        self.y += const.MOVEMENT[event.key][0]

    def next_day(self):
        self.day += 1
        if self.day == 64:
            self.next_season()
            self.day = 0
        self.temperature = random.choice(self.temperature_range[self.season])

    def next_season(self):
        self.season += 1
        if self.season == 4:
            self.season = 0
            self.year += 1

