from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import dacite

from .. import config


@dataclass
class InputSettings:
    """Represents the Input.ini"""

    console: str
    crouch: str
    drop: str
    inventory: str
    prone: str
    target_inventory: str
    toggle_hud: str
    hud_info: str
    use: str
    logs: str
    transfer: str
    reload: str
    hotbar_0: str
    hotbar_1: str
    hotbar_2: str
    hotbar_3: str
    hotbar_4: str
    hotbar_5: str
    hotbar_6: str
    hotbar_7: str
    hotbar_8: str
    hotbar_9: str

    @staticmethod
    def load(path: Optional[str] = None) -> InputSettings:
        """Loads the settings from input.ini, using the `ARK_PATH` provided
        in the configs or an alternatively passed path."""
        if path is None:
            path = f"{config.ARK_PATH}/ShooterGame/Saved/Config/Windows/Input.ini"

        try:
            with open(path, encoding="utf-8") as f:
                contents = f.readlines()
        except UnicodeDecodeError:
            with open(path, encoding="utf-16") as f:
                contents = f.readlines()
           
        settings: dict[str, float | bool | str | Path] = {"console": "tab", "crouch": "c", "drop": "o",
                                                          "inventory": "i", "prone": "x", "target_inventory": "f",
                                                          "toggle_hud": "backspace", "hud_info": "h", "use": "e",
                                                          "logs": "l", "transfer": "t", "reload": "r", "hotbar_0": "0",
                                                          "hotbar_1": "1", "hotbar_2": "2", "hotbar_3": "3",
                                                          "hotbar_4": "4", "hotbar_5": "5", "hotbar_6": "6",
                                                          "hotbar_7": "7", "hotbar_8": "8", "hotbar_9": "9",
                                                          "path": Path(path)}

        pattern = r'ActionName="([^"]+)",.*?Key=([^,)]+)'
        for line in contents:
            if not "=" in line:
                continue

            if "ConsoleKeys" in line:
                action_name = "ConsoleKeys"
                key = line.split("=")[1].strip()
            else:
                matches = re.search(pattern, line)

                if matches is None:
                    continue

                action_name = matches.group(1)
                key = matches.group(2)

            #print("Parsing Action: {action_name}, Key: {key}")  # Debug print

            action = _KEY_MAP.get(action_name)
            if key.lower() in _REPLACE and action is not None:
                settings[action] = str(_REPLACE.index(key.lower()))
            elif action is not None:
                settings[action] = validate_key(key.lower())

            #print("Updated Setting: {action} = {settings.get(action)}")  # Debug print

        return dacite.from_dict(InputSettings, settings)


def validate_key(key: str) -> str:
    """
    Validates and corrects a key so it matches the valid set.

    - If the key is already valid, return it.
    - If the key has a known mapping, return the mapped value.
    - Otherwise, return None (or raise an error if strict mode is needed).
    """
    key = key.lower()

    if key in VALID_KEYS:
        return key  # Already valid

    if key in KEY_MAPPINGS:
        return KEY_MAPPINGS[key]  # Fix known issues

    return ""  # Or return a default key if needed

_KEY_MAP = {
    "ConsoleKeys": "console",
    "Crouch": "crouch",
    "Prone": "prone",
    "DropItem": "drop",
    "ShowMyInventory": "inventory",
    "AccessInventory": "target_inventory",
    "ToggleHUDHidden": "toggle_hud",
    "ShowExtendedInfo": "hud_info",
    "TransferItem": "transfer",
    "Use": "use",
    "ShowTribeManager": "logs",
    "Reload": "reload",
    "UseItem1": "hotbar_1",
    "UseItem2": "hotbar_2",
    "UseItem3": "hotbar_3",
    "UseItem4": "hotbar_4",
    "UseItem5": "hotbar_5",
    "UseItem6": "hotbar_6",
    "UseItem7": "hotbar_7",
    "UseItem8": "hotbar_8",
    "UseItem9": "hotbar_9",
    "UseItem10": "hotbar_0",
}

_REPLACE = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

VALID_KEYS = {
    '\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
    ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
    '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
    'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
    'browserback', 'browserfavorites', 'browserforward', 'browserhome',
    'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
    'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
    'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
    'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
    'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
    'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
    'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
    'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
    'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
    'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
    'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
    'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
    'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
    'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
    'command', 'option', 'optionleft', 'optionright'
}

KEY_MAPPINGS = {
    "leftcontrol": "ctrlleft",
    "rightcontrol": "ctrlright",
    "leftshift": "shiftleft",
    "rightshift": "shiftright",
    "Leftalt": "altleft",
    "rightalt": "altright",
    "return": "enter",
    "prtsc": "printscreen",
    "prntscrn": "printscreen",
    "prtscr": "printscreen",
}