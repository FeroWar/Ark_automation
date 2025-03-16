import pyautogui
import keyboard
import threading

clicking = False  # Houdt bij of er geklikt moet worden
paused = False  # Houdt bij of het script gepauzeerd is

def clicker():
    global clicking, paused
    while True:
        if clicking and not paused:
            pyautogui.click()
        else:
            threading.Event().wait(0.001)  # Kleinere pauze om CPU-belasting te verlagen

def toggle_clicking():
    global clicking
    if not paused:
        clicking = not clicking  # Wisselt de klikstatus
        print(f"AutoClick {'AAN' if clicking else 'UIT'}")  # Laatste status printen

def toggle_pause():
    global paused, clicking
    paused = not paused  # Wisselt pauze aan/uit
    clicking = False  # Zet klikken uit als we pauzeren
    print(f"Autoclicker {'Gepauzeerd' if paused else 'Actief'}")

# Luisteren naar hotkeys
keyboard.add_hotkey("F1", toggle_clicking)  # Start/stop bij F1
keyboard.add_hotkey("F2", toggle_pause)  # Pauzeer/hervat bij F2

# Start de clicker in een aparte thread
thread = threading.Thread(target=clicker, daemon=True)
thread.start()

print("Autoclicker gestart. Druk op F1 om te starten/stoppen en F2 om te pauzeren/hervatten.")
keyboard.wait()  # Houdt het script draaiend
