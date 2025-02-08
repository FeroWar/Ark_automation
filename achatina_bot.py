import time

from ark import Player, items, Dinosaur

player = Player(500, 100, 100, 800)
achatina = Dinosaur("achatina", f"C:/Users/Tomas/Desktop/Ark_code/Ark_automation/ark/assets/wheels/gacha.png")

time.sleep(2)
player.press("e")
player.walk("d", 0.7)
player.walk("w", 2)
player.turn_y_by(15)
for _ in range(8):
    achatina.inventory.open()
    achatina.inventory.transfer_all(items.PASTE)
    achatina.inventory.close()
    player.prone()
    player.turn_y_by(-15)
    achatina.inventory.open()
    achatina.inventory.transfer_all(items.PASTE)
    achatina.inventory.close()
    player.prone()
    time.sleep(0.3)
    player.walk("a", 0.28)
    player.turn_y_by(15)
player.turn_x_by(180)
for _ in range(7):
    achatina.inventory.open()
    achatina.inventory.transfer_all(items.PASTE)
    achatina.inventory.close()
    player.prone()
    player.turn_y_by(-15)
    achatina.inventory.open()
    achatina.inventory.transfer_all(items.PASTE)
    achatina.inventory.close()
    player.prone()
    time.sleep(0.3)
    player.walk("a", 0.28)
    player.turn_y_by(15)