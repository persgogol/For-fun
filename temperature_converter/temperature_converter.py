def celsius_to_fahrenheit(c: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return c * 9/5 + 32


def fahrenheit_to_celsius(f: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (f - 32) * 5/9


def celsius_to_kelvin(c: float) -> float:
    """Convert Celsius to Kelvin."""
    return c + 273.15


def kelvin_to_celsius(k: float) -> float:
    """Convert Kelvin to Celsius."""
    return k - 273.15


def fahrenheit_to_kelvin(f: float) -> float:
    """Convert Fahrenheit to Kelvin."""
    return (f - 32) * 5/9 + 273.15


def kelvin_to_fahrenheit(k: float) -> float:
    """Convert Kelvin to Fahrenheit."""
    return (k - 273.15) * 9/5 + 32


def main():
    print("Temperature Converter")
    print("Available conversions:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    while True:
        choice = input("Select conversion (1-6) or 'q' to quit: ").strip()
        if choice.lower() == 'q':
            print("Goodbye!")
            break
        try:
            option = int(choice)
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6 or 'q' to quit.")
            continue
        if option < 1 or option > 6:
            print("Invalid choice. Please select a number between 1 and 6.")
            continue
        try:
            temp = float(input("Enter the temperature to convert: "))
        except ValueError:
            print("Invalid temperature input. Please enter a numeric value.")
            continue
        if option == 1:
            result = celsius_to_fahrenheit(temp)
            unit_from = "°C"
            unit_to = "°F"
        elif option == 2:
            result = fahrenheit_to_celsius(temp)
            unit_from = "°F"
            unit_to = "°C"
        elif option == 3:
            result = celsius_to_kelvin(temp)
            unit_from = "°C"
            unit_to = "K"
        elif option == 4:
            result = kelvin_to_celsius(temp)
            unit_from = "K"
            unit_to = "°C"
        elif option == 5:
            result = fahrenheit_to_kelvin(temp)
            unit_from = "°F"
            unit_to = "K"
        else:
            result = kelvin_to_fahrenheit(temp)
            unit_from = "K"
            unit_to = "°F"
        print(f"{temp}{unit_from} is {result}{unit_to}")


if __name__ == "__main__":
    main()
