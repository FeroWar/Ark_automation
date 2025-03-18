import string
import time

from GachaBotIsland import run_script_Square
from ark import Bed, Player
from ark.interfaces.structures.teleporter import Teleporter

player = Player(500, 800, 100, 100)
tp = Teleporter("Main Base")
bed = Bed("")

G = ["AA", "AB","AC", "AD","AE", "AF","AG", "AH","AI", "AJ","AK", "AL"]
i = 0

time.sleep(1)
player.suicide()
while not bed.interface.is_open():
    time.sleep(0.5)
bed.spawn_in("SpawnA")
time.sleep(12)
while True:
    try:
        run_script_Square(G[i%len(G)])
    except:
        if tp.interface.is_open(): tp.interface.close()
        if bed.interface.is_open(): bed.interface.close()
        if player.inventory.is_open(): player.inventory.close()
        player.walk("d", 2)
        player.suicide()
        while not bed.interface.is_open():
            time.sleep(0.5)
        bed.spawn_in("SpawnA")
        time.sleep(12)
    i += 1

