def input_temperature(temp_str: str) -> int:
    """
    Converts a string representation of a temperature to an integer.
    """
    return int(temp_str)


def test_temperature() -> None:
    """
    Tests the input_temperature function with valid and invalid inputs,
    demonstrating basic exception handling to prevent program crashes.
    """
    print("=== Garden Temperature ===")

    print("\nInput data is '25'")
    try:
        temp: int = input_temperature("25")
        print(f"Temperature is now {temp}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    print("\nInput data is 'abc'")
    try:
        temp = input_temperature("abc")
        print(f"\nTemperature is now {temp}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    print("\nAll tests completed program didn't crash!")


if __name__ == "__main__":
    test_temperature()
