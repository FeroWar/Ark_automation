import time

from GachaBot import y_vaccum, gacha_vaccum, open_crystals, access_cropplots, preload_croplots
from ark import Player, items, Dinosaur, Bed, TekCropPlot, TekDedicatedStorage, Structure
from ark.interfaces.structures.teleporter import Teleporter

player = Player(500, 800, 100, 100)
tp = Teleporter("Main Base")
bed = Bed("")
crop_plot = TekCropPlot("")
gacha = Dinosaur("Gacha", f"C:/Users/Tomas/Desktop/Ark_code/Ark_automation/ark/assets/wheels/gacha.png")
dedi = TekDedicatedStorage()

time.sleep(2)
bed.lay_down()
bed.get_up()