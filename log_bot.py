import time

from ark import TribeLog, TribeLogMessage
from ark.Discord_Webhook import DiscordWebhook

logs = TribeLog()
discord = DiscordWebhook("https://discord.com/api/webhooks/1290639488388698114/NvupgLHjHQcv1Ft9Q0SWUp11EFkXVW84G4XUUZuCPmPNA913ZYaaupQKXf-MsY3NHLrB")

time.sleep(1)
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
        print("Finished processing.")
    time.sleep(10)
