import string
import time

from GachaBotIsland import run_script_Square, gacha_square, y_module, open_crystals, tek_pause
from ark import Bed, Player, Dinosaur
from ark.interfaces.structures.teleporter import Teleporter

player = Player(500, 800, 100, 100)
tp = Teleporter("Main Base")
bed = Bed("")

G = ["AA"]
i = 0

time.sleep(1)
player.look_down_hard()