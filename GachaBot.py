import time

from ark import Player, items, Dinosaur, Bed, TekCropPlot, TekDedicatedStorage
from ark.interfaces.structures.teleporter import Teleporter

player = Player(500, 800, 100, 100)
tp = Teleporter("Main Base")
bed = Bed("")
crop_plot = TekCropPlot("")
gacha = Dinosaur("Gacha", f"C:/Users/Tomas/Desktop/Ark_code/Ark_automation/ark/assets/wheels/gacha.png")
dedi = TekDedicatedStorage()

time.sleep(1)


def y_vaccum(first: bool):
    if first:
        access_cropplots()
        player.walk("d", 0.6)
        access_cropplots()
        player.walk("a", 0.6)
    else:
        player.walk("d", 0.6)
        player.walk("d", 0.6)
        access_cropplots()
        player.walk("d", 0.6)
        access_cropplots()
        player.walk("a", 1.9)
    player.look_down_hard()


def gacha_vaccum(first: bool, out: str):
    if first:
        player.look_down_hard()
        player.turn_y_by(110)
        gacha.inventory.open()
        gacha.inventory.transfer_all(items.OWL_PELLET)
        player.inventory.transfer_all(items.Y_TRAP)
        player.inventory.transfer_all(items.OWL_PELLET)
        gacha.inventory.close()
        player.look_down_hard()
        time.sleep(0.1)
        tp.teleport(out)
        time.sleep(0.1)
    else:
        player.look_down_hard()
        player.turn_y_by(110)
        player.turn_x_by(-100)
        gacha.inventory.open()
        gacha.inventory.transfer_all(items.OWL_PELLET)
        player.inventory.transfer_all(items.Y_TRAP, items.YTRAP_SEED)
        player.inventory.transfer_all(items.OWL_PELLET)
        gacha.inventory.close()
        pegomastaks()
        player.turn_x_by(100)
        player.look_down_hard()
        time.sleep(0.1)
        tp.teleport(out)
        time.sleep(0.1)
    player.look_down_hard()


def access_cropplots():
    angles = [30, 10, 15, 15, 15, 15, 15, 15, 20]
    player.look_down_hard()
    for angle in angles:
        player.turn_y_by(angle)
        take_y()


def take_y():
    crop_plot.open()
    crop_plot.inventory.search(items.Y_TRAP)
    crop_plot.inventory.transfer_all()
    crop_plot.close()


def pegomastaks():
    player.look_down_hard()
    player.turn_y_by(45)
    player.turn_x_by(-80)
    player.walk("w", 0.1)
    player.turn_y_by(-20)
    gacha.inventory.open()
    gacha.inventory.transfer_all()
    gacha.inventory.close()
    player.turn_x_by(80)
    player.look_down_hard()

def tek_pause():
    bed.lay_down()
    #while (player.stats.health < player.stats.health_max):
    #player.get_hp()
    #check_logs()
    #time.sleep(10)
    bed.get_up()
    time.sleep(0.3)
    player.turn_y_by(-40)
    player.turn_x_by(-70)
    bed.access()
    bed.travel_to("spawnA")


def dump_dust():
    player.look_down_hard()
    player.turn_y_by(25)
    player.press(player.keybinds.use)
    player.turn_y_by(25)
    player.press(player.keybinds.use)
    player.turn_y_by(60)
    player.press(player.keybinds.use)
    player.turn_y_by(40)
    player.press(player.keybinds.use)


def dump_vault():
    player.look_down_hard()
    player.turn_y_by(90)
    dedi.open()
    player.inventory.transfer_all()
    dedi.close()
    player.turn_y_by(33)
    dedi.open()
    player.inventory.transfer_all()
    dedi.close()


def drop_vaults():
    player.walk("d", 0.3)
    dump_vault()
    player.walk("d", 0.25)
    dump_vault()
    player.walk("d", 0.4)
    dump_vault()
    player.walk("d", 0.35)
    dump_vault()
def open_crystals():
    player.look_down_hard()
    player.turn_y_by(50)
    bed.lay_down()
    bed.get_up()
    player.walk("w", 3)
    player.inventory.open()
    player.inventory.drop_all(items.OWL_PELLET)
    player.inventory.close()
    for _ in range(75):
        player.spam_hotbar()
    dump_dust()
    player.turn_x_by(40)
    dump_dust()
    player.turn_x_by(50)
    drop_vaults()
    player.turn_x_by(90)

def run_script(letter :str):
    #player.suicide()
    #while not bed.interface.is_open():
        #time.sleep(0.5)
    #bed.spawn_in("SpawnA")
    #wtime.sleep(12)
    player.turn_y_by(-30)
    bed.lay_down()
    bed.get_up()
    time.sleep(0.3)
    player.walk("s", 1)
    player.look_down_hard()
    tp.teleport("yy"+letter)
    y_vaccum(True)
    tp.teleport("Gacha+letter")
    gacha_vaccum(True, "yy"+letter)
    y_vaccum(False)
    tp.teleport("Gacha+letter")
    gacha_vaccum(False, "bed out")
    open_crystals()
    player.look_down_hard()
    player.turn_y_by(50)
    tek_pause()

#run_script()