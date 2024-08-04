import time

from ark import Player, items, Dinosaur

player = Player(500, 800, 100, 100)
anky = Dinosaur("Anky", f"C:/Users/Tomas/Desktop/Ark code/Ark-automation/ark/assets/wheels/gacha.png")

time.sleep(1)
anky.attack("left", 10)
anky.inventory.open()
anky.inventory.drop_all([items.STONE, items.FLINT, items.CRYSTAL, items.OBSIDIAN, items.WOOD, items.THATCH])
anky.inventory.close()
