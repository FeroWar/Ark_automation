import string
import time

from GachaBot import run_script
from ark import Bed, Player
from ark.interfaces.structures.teleporter import Teleporter

player = Player(500, 800, 100, 100)
tp = Teleporter("Main Base")
bed = Bed("")


player.suicide()
while not bed.interface.is_open():
    time.sleep(0.5)
    bed.spawn_in("SpawnA")
    time.sleep(12)
for letter in string.ascii_uppercase[:10]:
    try:
        run_script(letter)
    except  :
        player.suicide()

        while not bed.interface.is_open():
            time.sleep(0.5)

        bed.spawn_in("SpawnA")
        time.sleep(12)
