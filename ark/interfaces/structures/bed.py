import time
from typing import final

from ..spawn_screen import SpawnScreen
from .structure import Structure


@final
class Bed(Structure):

    def __init__(self, name: str) -> None:
        super().__init__(name, "assets/wheels/bed.png")
        self.interface = SpawnScreen()

    def travel_to(self, name: str) -> None:
        self.interface.travel_to(name)

    def lay_down(self) -> None:
        self.action_wheel.activate()
        self.action_wheel.select_action((1130, 510))
        self.action_wheel.deactivate()
        time.sleep(0.3)

    def get_up(self) -> None:
        self.press(self.keybinds.use)
        time.sleep(0.3)

    def spawn_in(self, name: str):
        self.interface.spawn_in(name)

    def access(self):
        self.interface.open()
