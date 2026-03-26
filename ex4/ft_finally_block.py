class GardenError(Exception):
    """
    Base exception class for all garden-related errors.
    """
    def __init__(self, message: str = "Unknown garden error") -> None:
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    """
    Exception raised for errors specific to individual plants.
    """
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    """
    Attempts to water a plant. Raises a PlantError if the
    plant name is not properly capitalized.
    """
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    """
    Tests the watering system with valid and invalid plants, demonstrating
    how the 'finally' block ensures resource cleanup regardless of errors.
    """
    print("=== Garden Watering System ===")

    print("\nTesting valid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print("ending tests and returning to main")
        return
    finally:
        print("Closing watering system")

    print("\nTesting invalid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("lettuce")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print("ending tests and returning to main")
        return
    finally:
        print("Closing watering system")
        print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
