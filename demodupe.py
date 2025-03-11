import time
import win32gui
import win32con
import win32api

APP_TITLE = "ArkAscended"


def get_window_handle():
    """Zoekt het venster van Ark Ascended en retourneert de handle."""
    hwnd = win32gui.FindWindow(None, APP_TITLE)
    return hwnd if hwnd else None


def hold_key(hwnd, key, hold_time=30):
    """Houdt een toets ingedrukt voor een bepaalde tijd."""
    if hwnd:
        win32gui.SetForegroundWindow(hwnd)  # Zet focus op game
        time.sleep(0.1)  # Korte vertraging

        vk_code = ord(key.upper())  # Converteer letter naar Virtual Key Code
        win32api.keybd_event(vk_code, 0, 0, 0)  # Druk toets in
        print(f"Toets '{key}' ingedrukt in {APP_TITLE}")

        time.sleep(hold_time)  # Houd toets ingedrukt

        win32api.keybd_event(vk_code, 0, win32con.KEYEVENTF_KEYUP, 0)  # Laat toets los
        print(f"Toets '{key}' losgelaten.")


def click_right_mouse(hwnd):
    """Klikt 1 keer met de rechtermuisknop."""
    if hwnd:
        win32gui.SetForegroundWindow(hwnd)  # Zet focus op game
        time.sleep(0.1)  # Korte vertraging

        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)  # Rechtermuisknop indrukken
        time.sleep(0.05)  # Korte pauze zodat het een echte klik is
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)  # Rechtermuisknop loslaten

        print("Rechtermuisknop 1 keer ingedrukt.")


while True:
    hwnd = get_window_handle()
    if hwnd:
        hold_key(hwnd, '1', hold_time=20)  # Houd '1' 20 seconden ingedrukt
        click_right_mouse(hwnd)  # Klik 1 keer met de rechtermuisknop
    else:
        print(f"Venster '{APP_TITLE}' niet gevonden. Zorg dat het open is!")

    print("Wachten 5 seconden en '9' indrukken...")
    time.sleep(5)  # 5 seconden pauze voordat de cyclus opnieuw start

    hwnd = get_window_handle()
    if hwnd:
        hold_key(hwnd, '9', hold_time=0.5)  # Druk '9' kort in
