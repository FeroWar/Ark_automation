import time

from ark import Player, items, Dinosaur

player = Player(500, 800, 100, 100)
anky = Dinosaur("Anky", f"C:/Users/Tomas/Desktop/Ark_code/Ark_automation/ark/assets/wheels/gacha.png")

time.sleep(3)
while(True):
    anky.attack("left", 30)
    try:
        anky.inventory.open()
        anky.inventory.drop_all([items.STONE, items.FLINT, items.OBSIDIAN, items.WOOD, items.THATCH])
        anky.inventory.close()
    finally:
        time.sleep(0.1)

