from dataclasses import dataclass
from typing import Optional

from .._ark import Ark
from .._helpers import get_filepath


@dataclass
class Button:
    #location and region in 1920/1080 but the ratios allow it to be used on most aspect ratios and resolutions
    location: tuple[int, int]
    region: Optional[tuple[int, int, int, int]] = None
    template: Optional[str] = None

    def __post_init__(self) -> None:
        if self.template is None:
            return
        template = f"{Ark.PKG_DIR}/assets/interfaces/{self.template}"
        self.template = get_filepath(template)

    def get_location(self):
        return self.location_x(), self.location_y()

    def location_x(self):
        return self.location[0]

    def location_y(self):
        return self.location[1]

    def get_region(self):
        return self.region
