from interface.texture import Texture
from interface.action_bar import ABar
from interface.info_bar import IBar
from templates import GroupTemplate
from bacteria import create_bacteria


UI = GroupTemplate()
world_info = IBar()
world_actions = ABar()
for i in range(10):
    create_bacteria()
UI.add(world_info, world_actions, Texture("world_border.png", 400, 250))
