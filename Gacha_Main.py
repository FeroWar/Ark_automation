import string
import time

from GachaBotIsland import run_script_Square
from ark import Bed, Player
from ark.Discord_Webhook import DiscordWebhook
from ark.interfaces.structures.teleporter import Teleporter

player = Player(500, 800, 100, 100)
tp = Teleporter("Main Base")
bed = Bed("")
discord = DiscordWebhook("https://discord.com/api/webhooks/1354475101294166117/8DpVv8_iC7KW8gkzg2s3R7FWVZvq9DVPWz8edud5tuM2vSh1mZC29GJfQcGNU9IhVK3K")

G = ["AA", "AB","AC", "AD","AE", "AF","AG", "AH","AI", "AJ","AK", "AL"]
i = 0

time.sleep(1)
player.suicide()
while not bed.interface.is_open():
    time.sleep(0.5)
bed.spawn_in("SpawnA")
time.sleep(12)
try:
    while True:
        try:
            run_script_Square(G[i%len(G)])
        except Exception as e:
            discord.SendMsg("Gacha Bot Killed Itself, Exception: " + str(e), "<@333266368847675403>")
            player.walk("d", 1)
            for _ in range(5):
                if tp.interface.is_open(): tp.interface.close()
                if bed.interface.is_open(): bed.interface.close()
                if player.inventory.is_open(): player.inventory.close()
                time.sleep(0.5)
            player.walk("d", 1)
            player.suicide()
            while not bed.interface.is_open():
                time.sleep(0.5)
            bed.spawn_in("SpawnA")
            time.sleep(12)
        i += 1
except Exception as e:
    discord.SendMsg("Gacha Bot Full Shutdown, Exception: " + str(e),"<@333266368847675403>")


