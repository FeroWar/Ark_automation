import string
import time

from GachaBotIsland import run_script_Square, gacha_square, open_crystals, tek_pause
from achatina_bot import achatina_chamber
from ark import Bed, Player, Dinosaur
from ark.interfaces.structures.teleporter import Teleporter

player = Player(500, 800, 100, 100)
tp = Teleporter("Main Base")
bed = Bed("")

G = ["AA"]
i = 0



time.sleep(1)
player.walk("d", 0.5)
