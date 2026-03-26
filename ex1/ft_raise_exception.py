def input_temperature(temp_str: str) -> int:
    """
    Converts a string to an integer temperature and validates if it is
    within the acceptable range for plants (0 to 40 degrees Celsius).
    Raises a ValueError if the temperature is out of bounds.
    """
    temp: int = int(temp_str)
    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    return temp


def test_temperature() -> None:
    """
    Tests input_temperature with valid, invalid, and extreme temperature
    values to demonstrate custom exception raising and handling.
    """
    print("=== Garden Temperature Checker ===")

    inputs: list[str] = ["25", "abc", "100", "-50"]
    for val in inputs:
        print(f"\nInput data is '{val}'")
        try:
            temp: int = input_temperature(val)
            print(f"Temperature is now {temp}°C")
        except Exception as e:
            print(f"Caught input_temperature error: {e}")

    print("\nAll tests completed program didn't crash!")


if __name__ == "__main__":
    test_temperature()
