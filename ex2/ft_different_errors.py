def garden_operations(operation_number: int) -> None:
    """
    Executes different faulty operations based on the provided number
    to purposefully raise specific built-in Python exceptions.
    """
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        1 / 0
    elif operation_number == 2:
        open('/non/existent/file')
    elif operation_number == 3:
        "a" + 1


def test_error_types() -> None:
    """
    Iterates through garden operations to trigger and independently
    catch different types of exceptions, demonstrating precise error handling.
    """
    print("=== Garden Error Types Demo ===")

    for i in range(5):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
            if i == 4:
                print("Operation completed successfully")
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
