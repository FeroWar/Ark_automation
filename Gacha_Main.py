import string
import time

from GachaBot import run_script, preload_croplots
from ark import Bed, Player
from ark.interfaces.structures.teleporter import Teleporter

player = Player(500, 800, 100, 100)
tp = Teleporter("Main Base")
bed = Bed("")

Y = ["A", "B", "C", "D", "E"]
G = string.ascii_uppercase
i = 3

player.suicide()
while not bed.interface.is_open():
    time.sleep(0.5)
bed.spawn_in("SpawnA")
time.sleep(12)
while True:
    try:
        run_script(Y[i % 5], G[i])
    except:
        player.suicide()
    i += 1
