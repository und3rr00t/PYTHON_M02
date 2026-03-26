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


class WaterError(GardenError):
    """
    Exception raised for errors related to the irrigation and watering system.
    """
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def test_plant_error() -> None:
    """
    Raises a PlantError for demonstration purposes.
    """
    raise PlantError("The tomato plant is wilting!")


def test_water_error() -> None:
    """
    Raises a WaterError for demonstration purposes.
    """
    raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    """
    Demonstrates raising and catching custom exceptions, including
    how catching a base class (GardenError) catches its subclasses.
    """
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        test_plant_error()
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        test_water_error()
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors..")
    try:
        test_plant_error()
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    try:
        test_water_error()
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
