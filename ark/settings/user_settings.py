from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Optional

import dacite

from ark import config

@dataclass
class UserSettings:
    """Represents the GameUserSettings.ini"""

    path: Path = field(init=False)
    ui_scaling: float
    fov_multiplier: float
    left_right_sens: float
    up_down_sens: float
    hide_item_names: bool
    show_item_tooltips: bool
    auto_chatbox: bool
    toggle_hud: bool
    disable_menu_transitions: bool
    resolution_x: int
    resolution_y: int
    server_filter: int
    last_server: str
    reverse_logs: bool
    local_show_all_items: bool
    remote_show_all_items: bool
    sort_type: int
    remote_sort_type: int
    remote_show_engrams: bool
    remote_hide_unlearned_engrams: bool
    in_remote_inventory: bool

    @staticmethod
    def load(path: Optional[str] = None) -> UserSettings:
        """Loads the settings from GameUserSettings.ini, using the `ARK_PATH`
        provided in the configs or an alternatively passed path."""
        if path is None:
            path = f"{config.ARK_PATH}/ShooterGame/Saved/Config/Windows/GameUserSettings.ini"

        try:
            with open(path, encoding="utf-8") as f:
                contents = f.readlines()
        except UnicodeDecodeError:
            with open(path, encoding="utf-16") as f:
                contents = f.readlines()
        settings: dict[str, float | bool | str | Path] = {"path": Path(path),"remote_hide_unlearned_engrams": True}

        # keep track of the session occurrences so we can find the last joined
        # server for the selected category, which is stored as an integer from 0-7
        session_occurences = 0
        for line in contents:
            if line.startswith("[/Script/Engine.GameUserSettings]"):
                break

            if "=" not in line:
                continue

            if "LastJoinedSessionPerCategory" in line and not settings.get("last_server"):
                if session_occurences == settings.get("server_filter"):
                    settings["last_server"] = line.split("=")[1].strip().strip('"')
                    continue
                else:
                    session_occurences += 1
            try:
                option, value = line.rstrip().split("=")
            except ValueError:
                pass
            setting = _KEY_MAP.get(option)

            if setting is not None:
                settings[setting] = _set_type(value)  # type: ignore[assignment]
        return dacite.from_dict(UserSettings, settings)

    @property
    def last_modified(self) -> str:
        epoch = self.path.stat().st_mtime
        return datetime.fromtimestamp(epoch).strftime("%Y-%m-%d %H:%M:%S")

    def listen_for_change(self) -> None:
        """Listens to any changes made to the file, this is done by loading the
        data of the last modified timestamp, and then waiting for the timestamp
        to change. Once it has we compare the new data to the previous data and
        notify about any changes.
        
        Particularly useful to find the name of a setting in the .ini by just
        changing it ingame, listening to the changes and see what value gets
        changed."""
        last_change = self.last_modified
        with open(self.path) as f:
            old_data = f.readlines()

        while self.last_modified == last_change:
            pass

        print("Change detected in GameUserSettings.ini!")
        while True:
            try:
                with open(self.path) as f:
                    new_data = f.readlines()
            except PermissionError:
                continue
            else:
                break

        for old_line, new_line in zip(old_data, new_data):
            if old_line != new_line:
                print(f"Setting '{old_line.strip()}' changed to '{new_line.strip()}'!")


_KEY_MAP = {
    "UIScaling": "ui_scaling",
    "FOVMultiplier": "fov_multiplier",
    "LookLeftRightSensitivity": "left_right_sens",
    "LookUpDownSensitivity": "up_down_sens",
    "HideItemTextOverlay": "hide_item_names",
    "bEnableInventoryItemTooltips": "show_item_tooltips",
    "bShowChatBox": "auto_chatbox",
    "bToggleExtendedHUDInfo": "toggle_hud",
    "bDisableMenuTransitions": "disable_menu_transitions",
    "ResolutionSizeX": "resolution_x",
    "ResolutionSizeY": "resolution_y",
    "LastServerSearchType": "server_filter",
    "bReverseTribeLogOrder": "reverse_logs",
    "bLocalInventoryItemsShowAllItems": "local_show_all_items",
    "LocalItemSortType": "sort_type",
    "RemoteItemSortType": "remote_sort_type",
    "bRemoteInventoryShowEngrams": "remote_show_engrams",
    "bRemoteInventoryCraftingShowAllItems": "remote_show_all_items",
    "bRemoteInventoryShowCraftables": "in_remote_inventory"
}


def _set_type(val: str) -> str | bool | float | int:
    """Sets the value from the .ini to the correct type"""
    if val == "True":
        return True

    elif val == "False":
        return False
    try:
        if "." in val:
            return float(val)
        return int(val)
    except ValueError:
        return val
