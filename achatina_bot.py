import time

from ark import Player, items, Dinosaur

player = Player(500, 800, 100, 100)
achatina = Dinosaur("achatina", f"C:/Users/Tomas/Desktop/Ark_code/Ark_automation/ark/assets/wheels/gacha.png")

time.sleep(1)

achatina.inventory.open()
achatina.inventory.transfer_all(items.PASTE)
achatina.inventory.close()
player.turn_y_by(-45)
achatina.inventory.open()
achatina.inventory.transfer_all(items.PASTE)
achatina.inventory.close()
player.walk("d", 0.3)
player.turn_y_by(45)
#player.turn_x_by(180)