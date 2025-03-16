import string
import time

from ark import Player, items, Dinosaur, Bed, TekCropPlot, TekDedicatedStorage
from ark.interfaces.structures.teleporter import Teleporter

player = Player(500, 800, 100, 100)
tp = Teleporter("Main Base")
bed = Bed("")
crop_plot = TekCropPlot("")
gacha = Dinosaur("Gacha", f"C:/Users/Tomas/Desktop/Ark_code/Ark_automation/ark/assets/wheels/gacha.png")
dedi = TekDedicatedStorage()

def run_script_Square(letter_G: str):
    player.turn_y_by(-30)
    bed.lay_down()
    bed.get_up()
    time.sleep(0.3)
    player.walk("s", 1)
    player.look_down_hard()
    tp.teleport("YYA")
    y_module()
    tp.teleport("Gacha" + letter_G)
    time.sleep(0.3)
    gacha_square(True, "YYB")
    y_module()
    tp.teleport("Gacha" + letter_G)
    gacha_square(False, "bed out")
    open_crystals()
    player.look_down_hard()
    player.turn_y_by(55)
    tek_pause()

def tek_pause():
    bed.lay_down()
    #while (player.stats.health < player.stats.health_max):
    #player.get_hp()
    #check_logs()
    time.sleep(10)
    bed.get_up()
    time.sleep(0.3)
    player.turn_y_by(-40)
    player.turn_x_by(-70)
    bed.access()
    bed.travel_to("spawnA")

def open_crystals():
    player.look_down_hard()
    player.turn_y_by(70)
    bed.lay_down()
    bed.get_up()
    player.walk("w", 3)
    player.inventory.open()
    player.inventory.drop_all(items.OWL_PELLET)
    player.inventory.drop_all(items.Y_TRAP)
    player.inventory.close()
    for _ in range(75):
        player.spam_hotbar()
    dump_dust()
    player.turn_x_by(40)
    dump_dust()
    player.turn_x_by(50)
    drop_vaults()
    player.turn_x_by(90)

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

def drop_vaults():
    player.walk("d", 0.3)
    dump_vault()
    player.walk("d", 0.25)
    dump_vault()
    player.walk("d", 0.4)
    dump_vault()
    player.walk("d", 0.4)
    dump_vault()

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

def gacha_square(first: bool, out: str):
    #time.sleep(5)
    player.look_down_hard()
    player.turn_y_by(90)
    if first:
        player.turn_x_by(50)
        gacha_take()
        player.turn_x_by(-50)
    else:
        player.turn_x_by(-50)
        gacha_take()
        player.turn_x_by(50)
        player.look_down_hard()
        player.turn_x_by(180)
        player.turn_y_by(90)
        gacha.inventory.open()
        gacha.inventory.transfer_all()
        gacha.inventory.close()
        player.turn_x_by(-180)
    player.look_down_hard()
    time.sleep(0.1)
    tp.teleport(out)
    time.sleep(0.1)
    player.look_down_hard()

def gacha_take():
    time.sleep(0.5)
    gacha.inventory.open()
    gacha.inventory.transfer_all(items.OWL_PELLET)
    player.inventory.transfer_all(items.Y_TRAP)
    player.inventory.transfer_all(items.OWL_PELLET)
    gacha.inventory.close()

def y_module():
    player.turn_x_by(-180)
    player.look_down_hard()
    player.turn_y_by(70)
    bed.lay_down()
    bed.get_up()
    player.walk("s", 0.3)
    player.inventory.open()
    player.inventory.drop_all(items.Y_TRAP)
    player.inventory.close()
    player.walk("a", 0.6)
    access_cropplots(False)
    player.walk("a", 0.6)
    access_cropplots(False)
    player.walk("a", 1)
    access_cropplots(True)
    player.look_down_hard()

def access_cropplots(on_tp: bool):
    player.look_down_hard()
    angles = [30, 10, 15, 15, 15, 15, 15, 15, 15]
    if on_tp: angles = [35, 10, 15, 15, 15, 15, 15, 15, 10]
    for angle in angles:
        try:
            player.turn_y_by(angle)
            take_y()
        except Exception as e:
            continue
    player.look_down_hard()

def take_y():
    crop_plot.open()
    crop_plot.inventory.search(items.Y_TRAP)
    crop_plot.inventory.transfer_all()
    crop_plot.close()