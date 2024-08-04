import time

from ark import Player, TekDedicatedStorage, IndustrialForge, items

player = Player(500, 800, 100, 100)
dedi = TekDedicatedStorage()
forge = IndustrialForge()

time.sleep(1)
print("run it t")
dedi.open()
dedi.inventory.transfer_all()
dedi.close()

player.turn_x_by(180, delay=0.1)
forge.open()
player.inventory.transfer_all(items.METAL)
forge.turn_on()
forge.close()

