import cv2 as cv  # type:ignore[import]
import numpy as np
import pyautogui  # type:ignore[import]

from .._ark import Ark
from .._helpers import await_event, get_center
from ..exceptions import BedNotAccessibleError, BedNotFoundError, PlayerDidntTravelError

from .. import config


class SpawnScreen(Ark):
    """Represents the spawn screen in Ark.

    Provides the ability to search for beds and detect them on the map,
    to then travel to them. If the bed icon itself cannot be found, the
    center of the red X will be assumed to be the correct location.
    """

    SEARCH_BAR = (425, 960)
    SPAWN_BUTTON = (1640, 960)

    SPAWN_SEARCH_BAR = (200, 970)

    TOP_BED = (290, 220)
    TOP_BED_NAME = (108, 215, 386, 15)

    _BEDS_REGION = (160, 70, 1050, 880)
    _BED_NAME_AREA = (624, 967, 250, 25)

    def spawn(self) -> None:
        """Clicks the spawn button"""
        self.click_at(self.SPAWN_BUTTON)

    def search(self, name: str) -> None:
        """Searches for a bed"""
        self.click_at(self.SEARCH_BAR)
        attempts = 0

        pyautogui.typewrite(name.lower(), interval=0.001)
        self.sleep(0.1)
        while attempts < 5:
            top_name = self.window.locate_all_text(region=self.TOP_BED_NAME, recolour=False)
            print(top_name)
            if name.lower() in top_name.lower():
                self.click_at(self.TOP_BED, delay=0.1)
                self.spawn()
                return
            self.sleep(0.2)
            attempts += 1
        raise BedNotFoundError(f"Cant find bed named: '{name}'!")

    def spawn_search(self, name: str) -> None:
        """Searches for a bed"""
        self.click_at(self.SPAWN_SEARCH_BAR)
        attempts = 0

        pyautogui.typewrite(name.lower(), interval=0.001)
        self.sleep(0.1)
        while attempts < 5:
            top_name = self.window.locate_all_text(region=self.TOP_BED_NAME, recolour=False)
            print(top_name)
            if name.lower() in top_name.lower():
                self.click_at(self.TOP_BED, delay=0.1)
                self.spawn()
                return
            self.sleep(0.2)
            attempts += 1
        raise BedNotFoundError(f"Cant find bed named: '{name}'!")

    def open(self) -> None:
        """Opens the bed menu. Times out after 30 unsuccessful
        attempts raising a `BedNotAccessibleError`"""
        attempt = 0
        while not self.is_open():
            attempt += 1
            self.press(self.keybinds.use)
            self.sleep(1)

            if attempt > 3:
                raise BedNotAccessibleError("Failed to access the bed!")

    def travel_to(self, bed_name: str) -> None:
        """Travels to a bed given it's name. If the spawn screen is not
        already open, it will be opened first.

        Parameters
        ----------
        name :class:`str`:
            The name of the bed to travel to
        """
        self.open()
        self.search(bed_name)

        if await_event(self._is_travelling, max_duration=5 * config.TIMER_FACTOR):
            self.sleep(0.5)
            return
        raise PlayerDidntTravelError(f"Failed to travel to bed '{bed_name}'!")

    def spawn_in(self, bed_name: str) -> None:
        """Travels to a bed given it's name. If the spawn screen is not
        already open, it will be opened first.

        Parameters
        ----------
        name :class:`str`:
            The name of the bed to travel to
        """
        if self.is_open():
            self.spawn_search(bed_name)

        if await_event(self._is_travelling, max_duration=5 * config.TIMER_FACTOR):
            self.sleep(0.5)
            return
        raise PlayerDidntTravelError(f"Failed to travel to bed '{bed_name}'!")

    def can_be_accessed(self) -> bool:
        """Returns whether the bed can be accessed, determined by the
        'Fast trave' text that appears when facing it."""
        return (
            self.window.locate_template(
                f"{self.PKG_DIR}/assets/templates/fast_travel.png",
                region=(0, 0, 1920, 1080),
                confidence=0.7,
            )
            is not None
        )

    def is_open(self) -> bool:
        """Returns whether the spawn screen is currently open."""
        return (
            self.window.locate_template(
                f"{self.PKG_DIR}/assets/interfaces//bed_filter.png",
                region=(294, 134, 71, 36),
                confidence=0.8,
            )
            is not None
            or self.window.locate_template(
                f"{self.PKG_DIR}/assets/interfaces//bed_filter.png",
                region=(380, 134, 71, 36),
                confidence=0.8,
            )
            is not None
        )

    def _find_bed(self) -> tuple[int, int] | None:
        """Finds the icon of a bed on the map, assuming the bed has already
        been searched."""
        img_arr = np.array(self.window.grab_screen(self._BEDS_REGION))
        img = cv.cvtColor(img_arr, cv.COLOR_BGR2RGB)

        lower_bound = tuple(max(0, i - 7) for i in (0, 255, 255))
        upper_bound = tuple(min(255, i + 7) for i in (0, 255, 255))

        mask = cv.inRange(img, lower_bound, upper_bound)
        contours, _ = cv.findContours(
            mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE
        )

        if len(contours) == 0:
            return None

        contour = max(contours, key=cv.contourArea)
        if cv.contourArea(contour) < 10:
            return None

        point = get_center(cv.boundingRect(contour))
        return point[0] + 160, point[1] + 70

    def _find_x(self) -> tuple[int, int] | None:
        """Finds the red X on the map, assuming the bed has already
        been searched."""
        img_arr = np.array(self.window.grab_screen(self._BEDS_REGION))
        img = cv.cvtColor(img_arr, cv.COLOR_BGR2RGB)

        lower_bound = tuple(max(0, i - 7) for i in (255, 255, 255))
        upper_bound = tuple(min(255, i + 7) for i in (255, 255, 255))

        mask = cv.inRange(img, lower_bound, upper_bound)
        contours, _ = cv.findContours(
            mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE
        )

        if len(contours) == 0:
            return None

        contour = max(contours, key=cv.contourArea)
        if cv.contourArea(contour) < 300:
            return None

        point = get_center(cv.boundingRect(contour))
        return point[0] + 160, point[1] + 70

    def _is_travelling(self) -> bool:
        """Check if we are currently travelling (whitescreen)"""
        return pyautogui.pixelMatchesColor(
            *self.window.convert_point(959, 493), (255, 255, 255), tolerance=10
        )

    def _bed_is_selected(self) -> bool:
        return (
            self.window.locate_template(
                f"{self.PKG_DIR}/assets/interfaces/bed_button.png",
                region=(587, 955, 35, 43),
                confidence=0.7,
            )
            is not None
        )

    def _spawn_region_is_selected(self) -> bool:
        return (
            self.window.locate_template(
                f"{self.PKG_DIR}/assets/interfaces/random_location.png",
                region=self._BED_NAME_AREA,
                confidence=0.85,
            )
            is not None
        )
