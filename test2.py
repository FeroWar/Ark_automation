import string
import time

from GachaBotIsland import run_script_Square, gacha_square, open_crystals, tek_pause
from ark import Bed, Player, Dinosaur
from ark.Discord_Webhook import DiscordWebhook
from ark.interfaces.structures.teleporter import Teleporter

player = Player(500, 800, 100, 100)
tp = Teleporter("Main Base")
bed = Bed("")
discord = DiscordWebhook("https://discord.com/api/webhooks/1354475101294166117/8DpVv8_iC7KW8gkzg2s3R7FWVZvq9DVPWz8edud5tuM2vSh1mZC29GJfQcGNU9IhVK3K")

G = ["AA"]
i = 0



time.sleep(1)
discord.SendMsg("Maxx like willy", "<@333266368847675403>")

