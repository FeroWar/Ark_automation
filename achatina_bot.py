import time

from ark import Player, items, Dinosaur, TekDedicatedStorage, Bed, TekSleepingPod, TribeLog
from ark.Discord_Webhook import DiscordWebhook

player = Player(500, 100, 100, 800)
achatina = Dinosaur("achatina", f"C:/Users/Tomas/Desktop/Ark_code/Ark_automation/ark/assets/wheels/gacha.png")
dedi = TekDedicatedStorage()
bed = Bed("")
logs = TribeLog()
discord = DiscordWebhook("https://discord.com/api/webhooks/1290639488388698114/NvupgLHjHQcv1Ft9Q0SWUp11EFkXVW84G4XUUZuCPmPNA913ZYaaupQKXf-MsY3NHLrB")


def achatina_chamber():
    player.look_down_hard()
    player.turn_y_by(115)
    time.sleep(1)
    #achatina.inventory.open()
    #achatina.inventory.transfer_all(items.PASTE)
    #achatina.inventory.close()
    player.look_down_hard()
    player.crouch()
    player.turn_y_by(70)
    time.sleep(1)
    #achatina.inventory.open()
    #achatina.inventory.transfer_all(items.PASTE)
    #achatina.inventory.close()
    player.crouch()
    player.look_down_hard()

def dump():
    player.crouch()
    player.turn_x_by(90)
    player.look_down_hard()
    player.turn_y_by(60)
    dedi.open()
    player.inventory.transfer_all()
    dedi.close()
    player.crouch()
    dedi.open()
    player.inventory.transfer_all()
    dedi.close()

def cicle():
    time.sleep(2)
    player.suicide()
    while not bed.interface.is_open():
        time.sleep(0.5)
    bed.spawn_in("SpawnB")
    time.sleep(12)
    player.turn_y_by(-30)
    bed.lay_down()
    bed.get_up()
    time.sleep(0.3)
    player.walk("d", 0.47)
    for _ in range(10):
        time.sleep(1)
        player.walk("w", 0.2)
        achatina_chamber()
        player.turn_x_by(180)
        player.walk("w", 0.2)
        achatina_chamber()
        player.turn_x_by(180)
        player.walk("d", 0.285)
    player.walk("d", 0.2)
    dump()
    player.turn_x_by(180)
    player.walk("w", 5)
    player.walk("d", 0.3)
    player.look_down_hard()
    player.turn_y_by(30)
    player.turn_x_by(90)
    bed.lay_down()
    start = time.time()
    while True:
        try:
            print("reading logs.")
            logs.open()
            log_events = logs.get_tribelog_events()

        # Only alert if there are logs, to avoid empty messagesz\
            if log_events:
                print("found logs to relay.")
                discord.AlertDetection(log_events)

        except Exception as e:
        # Catch the exception and assign it to 'e'
            print(f"An error occurred: {e}")

        finally:
        # Will print in all cases, whether an exception occurred or not
            if time.time() - start > 5400:
                break
            print("Finished processing.")
        time.sleep(30)

while True:
    try:
        cicle()
    except Exception as e:
        print(e)