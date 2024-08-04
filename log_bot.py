import time

from ark import TribeLog, ArkWindow

logs = TribeLog()

time.sleep(1)

logs.open()
print("members")
logs.get_online_members()
print(logs.online_members)
