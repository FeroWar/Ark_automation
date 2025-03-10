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

time.sleep(1)


def y_vaccum(first: bool, full_back: bool):
    if full_back: player.walk("w",0.15)
    if first:
        access_cropplots(full_back)
        player.walk("d", 0.6)
        access_cropplots(full_back)
        player.walk("a", 0.6)
    else:
        player.walk("d", 0.6)
        player.walk("d", 0.6)
        access_cropplots(full_back)
        player.walk("d", 0.6)
        access_cropplots(full_back)
        player.walk("a", 1.9)
    player.look_down_hard()
    if full_back: player.walk("s", 0.3)

def gacha_take():
    gacha.inventory.open()
    gacha.inventory.transfer_all(items.OWL_PELLET)
    player.inventory.transfer_all(items.Y_TRAP)
    player.inventory.transfer_all(items.OWL_PELLET)
    gacha.inventory.close()

def gacha_front(first: bool, out: str):
    if first:
        player.look_down_hard()
        player.turn_y_by(110)
        gacha_take()
        player.look_down_hard()
        time.sleep(0.1)
        tp.teleport(out)
        time.sleep(0.1)
    else:
        player.look_down_hard()
        player.turn_y_by(110)
        gacha_take()
        player.look_down_hard()
        pegomastaks_side()
        player.look_down_hard()
        time.sleep(0.1)
        tp.teleport(out)
        time.sleep(0.1)
    player.look_down_hard()

def pegomastaks_side():
    player.look_down_hard()
    player.turn_y_by(25)
    player.turn_x_by(90)
    gacha.inventory.open()
    gacha.inventory.transfer_all()
    gacha.inventory.close()
    player.turn_x_by(-90)
    player.look_down_hard()


def gacha_vaccum(first: bool, out: str):
    if first:
        player.look_down_hard()
        player.turn_y_by(110)
        gacha_take()
        player.look_down_hard()
        time.sleep(0.1)
        tp.teleport(out)
        time.sleep(0.1)
    else:
        player.look_down_hard()
        player.turn_y_by(110)
        player.turn_x_by(-100)
        gacha_take()
        pegomastaks()
        player.turn_x_by(100)
        player.look_down_hard()
        time.sleep(0.1)
        tp.teleport(out)
        time.sleep(0.1)
    player.look_down_hard()


def access_cropplots(preload: bool):
    angles = [30, 10, 15, 15, 15, 15, 15, 15, 15]
    player.look_down_hard()
    if preload: angles = [35, 10, 15, 15, 15, 15, 15, 15, 10]
    for angle in angles:
        player.turn_y_by(angle)
        take_y(preload)

def take_y(preload: bool):
    crop_plot.open()
    if not preload:
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

def gacha_hex(int: int, out_tp: str, first: bool):
    if int==0:
        gacha_front()
    elif int==1:
        player.turn_x_by(-90)
        time.sleep(0.1)
        player.turn_x_by(90)
    elif int == 2:
        player.turn_x_by(90)
        time.sleep(0.1)
        player.turn_x_by(-90)
    elif int == 3:
        time.sleep(0.1)
    elif int == 4:
        player.turn_x_by(-90)
        time.sleep(0.1)
        player.turn_x_by(90)
    elif int == 5:
        player.turn_x_by(90)
        time.sleep(0.1)
        player.turn_x_by(-90)

def gacha_square(first: bool, out: str):
    if first:
        player.look_down_hard()
        player.turn_y_by(110)

        player.walk("a", 0.5)
        gacha_take()
        player.walk("d", 0.5)
    else:
        player.look_down_hard()
        player.turn_y_by(110)
        player.walk("a", 1.5)
        gacha_take()
        player.walk("d", 1.5)
        player.look_down_hard()
        player.turn_y_by(45)
        gacha.inventory.open()
        gacha.inventory.transfer_all()
        gacha.inventory.close()
    player.look_down_hard()
    time.sleep(0.1)
    tp.teleport(out)
    time.sleep(0.1)
    player.look_down_hard()

def run_script(letter_Y: str, letter_G: str):
    player.turn_y_by(-30)
    bed.lay_down()
    bed.get_up()
    time.sleep(0.3)
    player.walk("s", 1)
    player.look_down_hard()
    tp.teleport("yy" + letter_Y)
    y_vaccum(True, False)
    tp.teleport("Gacha" + letter_G)
    gacha_vaccum(True, "yy" + letter_Y)
    y_vaccum(False, False)
    tp.teleport("yyw")
    player.walk("d", 0.6)
    player.inventory.open()
    player.inventory.search(items.OWL_PELLET)
    player.inventory.close()
    player.walk("a", 0.6)
    tp.teleport("Gacha" + letter_G)
    gacha_vaccum(False, "bed out")
    open_crystals()
    player.look_down_hard()
    player.turn_y_by(55)
    tek_pause()

def run_script_Perci(num: int, out_tp:str):
    player.turn_y_by(-30)
    bed.lay_down()
    bed.get_up()
    time.sleep(0.3)
    player.walk("s", 1)
    player.look_down_hard()
    tp.teleport("yy" + Y[num % 5])
    y_vaccum(True, False)
    tp.teleport("Gacha" + G[num])
    gacha_hex(num%6, "yy" + Y[num % 5])
    y_vaccum(False, False)
    tp.teleport(out_tp)
    player.walk("d", 0.6)
    player.inventory.open()
    player.inventory.search(items.OWL_PELLET)
    player.inventory.close()
    player.walk("a", 0.6)
    tp.teleport("Gacha" + G[num])
    gacha_vaccum(False, "bed out")
    open_crystals()
    player.look_down_hard()
    player.turn_y_by(55)
    tek_pause()

def run_script_Square(letter_Y: str, letter_G: str):
    player.turn_y_by(-30)
    bed.lay_down()
    bed.get_up()
    time.sleep(0.3)
    player.walk("s", 1)
    player.look_down_hard()
    tp.teleport("yy" + letter_Y)
    y_vaccum(True, True)
    tp.teleport("Gacha" + letter_G)
    gacha_square(True, "yy" + letter_Y)
    y_vaccum(False, True)
    #tp.teleport("yyw")
    #player.walk("d", 0.6)
    #player.inventory.open()
    #player.inventory.search(items.OWL_PELLET)
    #player.inventory.close()
    #player.walk("a", 0.6)
    tp.teleport("Gacha" + letter_G)
    gacha_square(False, "bed out")
    open_crystals()
    player.look_down_hard()
    player.turn_y_by(55)
    tek_pause()