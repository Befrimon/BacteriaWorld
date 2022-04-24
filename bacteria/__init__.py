from templates import GroupTemplate
from bacteria.bacteria import Bacteria
from world import the_warda
import random

bacterias = GroupTemplate()


def create_bacteria(x: int = -1, y: int = -1):
    if x < 0: x = random.randint(2, 798)
    if y < 0: y = random.randint(2, 498)
    bacterias.add(Bacteria(the_warda, (x, y)))
