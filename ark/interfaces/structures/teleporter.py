from typing import final

from .structure import Structure
from ..teleport_screen import TeleportScreen


@final
class Teleporter(Structure):

    def __init__(self, name: str) -> None:
        super().__init__(name, "assets/wheels/bed.png")
        self.interface = TeleportScreen()

    def teleport(self, name: str) -> None:
        self.interface.teleport_to(name)

    def open(self) -> None:
        self.interface.open()

    def teleport_default(self) -> None:
        self.interface.teleport_to_default()


