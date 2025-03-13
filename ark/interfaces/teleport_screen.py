import cv2 as cv  # type:ignore[import]
import numpy as np
import pyautogui  # type:ignore[import]
from PIL import Image

from .._ark import Ark
from .._helpers import await_event, get_center
from ..exceptions import PlayerDidntTravelError, TeleporterNotFoundError, TeleporterNotAccessibleError

from .. import config, Player
from pytesseract import pytesseract as tes  # type: ignore[import]

player = Player(500, 800, 100, 100)

class TeleportScreen(Ark):
    """Represents the spawn screen in Ark.

    Provides the ability to search for beds and detect them on the map,
    to then travel to them. If the bed icon itself cannot be found, the
    center of the red X will be assumed to be the correct location.
    """

    SEARCH_BAR = (425, 960)
    TOP_TELEPORTER = (290, 220)
    TOP_TELEPORTER_NAME = (108, 215, 386, 15)
    TELEPORT_BUTTON = (1640, 960)

    def teleport(self) -> None:
        """Clicks the spawn button"""
        self.click_at(self.TELEPORT_BUTTON)

    def search(self, name: str) -> None:
        """Searches for a bed"""
        self.click_at(self.SEARCH_BAR)

        attempts = 0
        pyautogui.typewrite(name.lower(), interval=0.001)
        self.sleep(0.1)
        while attempts < 5:
            top_name = self.window.locate_all_text(region=self.TOP_TELEPORTER_NAME, recolour=False)
            if name.lower() in top_name.lower():
                self.click_at(self.TOP_TELEPORTER, delay=0.1)
                return
            self.sleep(0.2)
            attempts += 1

        raise TeleporterNotFoundError(f"Cant find tp named: '{name}'!")

    def open(self) -> None:
        """Opens the bed menu. Times out after 30 unsuccessful
        attempts raising a `BedNotAccessibleError`"""
        attempt = 0
        while not self.is_open():
            attempt += 1
            self.press(self.keybinds.use)
            self.sleep(0.3)

            if attempt > 3:
                raise TeleporterNotAccessibleError("Failed to access the teleporter!")

    def teleport_to(self, tp_name: str) -> None:
        """Travels to a tp given it's name. If the spawn screen is not
        already open, it will be opened first.

        Parameters
        ----------
        name :class:`str`:
            The name of the bed to travel to
        """
        max_attempts = 3

        for attempt in range(max_attempts):
            player.look_up_hard()
            before = self.window.get_fullscreen()
            player.look_down_hard()
            self.open()
            self.search(tp_name)

            self.teleport()
            self.sleep(0.5)
            player.look_up_hard()
            after = self.window.get_fullscreen()
            player.look_down_hard()
            if not self.window.compare_imgs(before, after, 0.9):
                return

            self.sleep(1)
        raise PlayerDidntTravelError(f"Failed to travel to tp '{tp_name}'!")

    def teleport_to_default(self) -> None:
        """Travels to the default teleporter, retrying up to 3 times if unsuccessful."""
        max_attempts = 3

        for attempt in range(max_attempts):
            before = self.window.get_fullscreen()
            self.press(self.keybinds.reload)
            self.sleep(0.5)
            after = self.window.get_fullscreen()

            if not self.window.compare_imgs(before, after, 0.8):
                return
            self.sleep(1)
        raise PlayerDidntTravelError("Failed to travel to default tp!")

    def is_open(self) -> bool:
        """Returns whether the spawn screen is currently open."""
        return (
                self.window.locate_template(
                    f"{self.PKG_DIR}/assets/interfaces//teleports.png",
                    region=(250, 133, 157, 40),
                    confidence=0.8,
                )
                is not None
        )
