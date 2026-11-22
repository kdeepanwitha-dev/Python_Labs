"""
Mini Project: Unit Converter
Converts length, weight, temperature, and time units.
"""


def read_positive_number(prompt):
    """Read a non-negative number."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Value cannot be negative.")
            else:
                return value
        except ValueError:
            print("Please enter a valid number.")


def length_converter():
    print("\nLength Conversion")
    print("1. Metres to kilometres")
    print("2. Kilometres to metres")
    print("3. Centimetres to metres")

    choice = input("Choose an option: ")
    value = read_positive_number("Enter the value: ")

    if choice == "1":
        print(f"{value:g} m = {value / 1000:g} km")
    elif choice == "2":
        print(f"{value:g} km = {value * 1000:g} m")
    elif choice == "3":
        print(f"{value:g} cm = {value / 100:g} m")
    else:
        print("Invalid option.")


def weight_converter():
    print("\nWeight Conversion")
    print("1. Kilograms to grams")
    print("2. Grams to kilograms")

    choice = input("Choose an option: ")
    value = read_positive_number("Enter the value: ")

    if choice == "1":
        print(f"{value:g} kg = {value * 1000:g} g")
    elif choice == "2":
        print(f"{value:g} g = {value / 1000:g} kg")
    else:
        print("Invalid option.")


def temperature_converter():
    print("\nTemperature Conversion")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Choose an option: ")
    value = read_positive_number("Enter the value: ")

    if choice == "1":
        result = (value * 9 / 5) + 32
        print(f"{value:g}°C = {result:.2f}°F")
    elif choice == "2":
        result = (value - 32) * 5 / 9
        print(f"{value:g}°F = {result:.2f}°C")
    else:
        print("Invalid option.")


def main():
    while True:
        print("\n" + "=" * 50)
        print("              UNIT CONVERTER")
        print("=" * 50)
        print("1. Length")
        print("2. Weight")
        print("3. Temperature")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            length_converter()
        elif choice == "2":
            weight_converter()
        elif choice == "3":
            temperature_converter()
        elif choice == "4":
            print("Thank you for using the unit converter.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()