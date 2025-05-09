import time

from ..._ark import Ark
from ...exceptions import DinoNotMountedError, InventoryNotAccessibleError, WheelError
from ...interfaces import ActionWheel, Inventory

class Dinosaur(Ark):
    def __init__(self, entity_name, wheel) -> None:
        super().__init__()
        self.name = entity_name
        self.inventory = Inventory(entity_name)
        self.action_wheel = ActionWheel(entity_name, wheel)

    def access(self) -> None:
        """Wraps the inventory `open` function using the action wheel to
        validate whether we are actually in range of it on failure.

        Raises
        ------
        `InventoryNotAccessibleError`
            If the Inventory could not be accessed even though it is in
            range (determined by the action wheel)

        `WheelNotAccessibleError`
            When no wheel could be opened at all after several attempts

        `UnexpectedWheelError`
            When a wheel was opened but is of an unexpected entity
        """
        try:
            self.inventory.open()
        except InventoryNotAccessibleError as e:
            try:
                self.action_wheel.activate()
            except WheelError:
                self.action_wheel.deactivate()
                raise e
            self.action_wheel.deactivate()
            self.inventory.open(max_duration=40)

    def close(self) -> None:
        self.inventory.close()

    def is_mounted(self) -> bool:
        return (
            self.window.locate_template(
                f"{self.PKG_DIR}/assets/templates/stamina_mount.png",
                region=(1880, 53, 31, 44),
                confidence=0.6,
            )
            is not None
        )

    def can_ride(self) -> bool:
        return (
            self.window.locate_template(
                f"{self.PKG_DIR}/assets/templates/ride.png",
                region=(0, 0, 1920, 1080),
                confidence=0.7,
            )
            is not None
        )

    def can_access(self) -> bool:
        return (
            self.window.locate_template(
                f"{self.PKG_DIR}/assets/templates/access_inventory.png",
                region=(0, 0, 1920, 1080),
                confidence=0.7,
            )
            is not None
        )

    def await_mounted(self) -> bool:
        counter = 0
        while not self.is_mounted():
            self.sleep(0.1)
            if self.inventory.is_open():
                raise DinoNotMountedError(
                    f"Failed to mount {self.name}, accessed inventory instead!"
                    "Please ensure a saddle is equipped."
                )
            counter += 1
            if counter > 130:
                return False
        return True

    def await_dismounted(self) -> bool:
        counter = 0
        while self.is_mounted():
            self.sleep(0.1)
            counter += 1
            if counter > 130:
                return False
        return True

    def mount(self) -> None:
        counter = 0
        while not self.is_mounted():
            self.press(self.keybinds.use)
            if self.await_mounted():
                return
            counter += 1
            if counter >= 4:
                raise DinoNotMountedError(f"Failed to mount {self.name} after 60s!")
        self.sleep(0.5)

    def dismount(self) -> None:
        while self.is_mounted():
            self.press(self.keybinds.use)
            if self.await_dismounted():
                return

        self.sleep(0.5)

    def attack(self, button: str, duration: int = 0) -> None:
        if duration > 0:
            start_time = time.time()
            while time.time() - start_time < duration:  # Loop for duration
                self.click(button)
                time.sleep(0.1)
        else:
            self.click(button)


