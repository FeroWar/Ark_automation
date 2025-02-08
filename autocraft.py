import time
from ark import Player, ChemistryBench , items

player = Player(500, 800, 100, 100)
chem_bench = ChemistryBench()

time.sleep(5)
player.press("e")
player.look_down_hard()
player.walk("w", 0.18)
player.walk("d", 0.48)
for i in range(4):
    for _ in range(10):
        chem_bench.open()
        #chem_bench.turn_on()
        chem_bench.inventory.open_tab("crafting")
        #chem_bench.inventory.search(items.SPARKPOWDER)
        #player.click_at((1244, 281))
        #for _ in range(10):
            #player.press("a")
        #player.click_at((969, 540))
        chem_bench.inventory.search(items.GUNPOWDER)
        player.click_at((1244, 281))
        for _ in range(10):
            player.press("a")
        player.click_at((969, 540))
        chem_bench.close()
        time.sleep(0.5)
        if i == 0 or i == 2:
            player.walk("d", 0.2)
        else:
            player.walk("a", 0.2)
    if i == 0 or i == 2:
        player.walk("s", 2)
        player.walk("a", 0.2)
    if i == 1 :
        player.walk("s", 5.4)
        player.walk("d", 0.2)
