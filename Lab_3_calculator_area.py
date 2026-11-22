"""
Lab Exercise 3: Scientific Calculator and Area Calculator

This program demonstrates:
+   Addition
-   Subtraction
*   Multiplication
/   Division
//  Floor division
%   Modulus/remainder
**  Exponentiation
"""

import math


def read_number(prompt):
    """Read a valid integer or decimal number from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def display_result(operation, result):
    """Display a calculator result in a consistent format."""
    print(f"\n{operation}")
    print(f"Result: {result:g}")


def calculator():
    """Perform arithmetic calculations using a menu."""
    while True:
        print("\n" + "=" * 60)
        print("                 SIMPLE CALCULATOR")
        print("=" * 60)
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Floor Division (//)")
        print("6. Modulus/Remainder (%)")
        print("7. Exponentiation (**)")
        print("8. Show all operations")
        print("9. Return to main menu")

        choice = input("Enter your choice: ").strip()

        if choice == "9":
            break

        if choice not in {"1", "2", "3", "4", "5", "6", "7", "8"}:
            print("Invalid choice. Please choose from 1 to 9.")
            continue

        first_number = read_number("Enter the first number: ")
        second_number = read_number("Enter the second number: ")

        if choice == "1":
            display_result(
                f"{first_number:g} + {second_number:g}",
                first_number + second_number
            )

        elif choice == "2":
            display_result(
                f"{first_number:g} - {second_number:g}",
                first_number - second_number
            )

        elif choice == "3":
            display_result(
                f"{first_number:g} * {second_number:g}",
                first_number * second_number
            )

        elif choice == "4":
            if second_number == 0:
                print("Error: Division by zero is not allowed.")
            else:
                display_result(
                    f"{first_number:g} / {second_number:g}",
                    first_number / second_number
                )

        elif choice == "5":
            if second_number == 0:
                print("Error: Floor division by zero is not allowed.")
            else:
                display_result(
                    f"{first_number:g} // {second_number:g}",
                    first_number // second_number
                )

        elif choice == "6":
            if second_number == 0:
                print("Error: Modulus by zero is not allowed.")
            else:
                display_result(
                    f"{first_number:g} % {second_number:g}",
                    first_number % second_number
                )

        elif choice == "7":
            try:
                display_result(
                    f"{first_number:g} ** {second_number:g}",
                    first_number ** second_number
                )
            except OverflowError:
                print("The result is too large to calculate.")

        elif choice == "8":
            print("\nAll arithmetic results:")

            print(f"Addition:       {first_number + second_number:g}")
            print(f"Subtraction:    {first_number - second_number:g}")
            print(f"Multiplication: {first_number * second_number:g}")

            if second_number != 0:
                print(f"Division:        {first_number / second_number:g}")
                print(f"Floor division:  {first_number // second_number:g}")
                print(f"Remainder:       {first_number % second_number:g}")
            else:
                print("Division:        Not possible by zero")
                print("Floor division:  Not possible by zero")
                print("Remainder:       Not possible by zero")

            try:
                print(f"Power:           {first_number ** second_number:g}")
            except OverflowError:
                print("Power:           Result too large")


def calculate_area():
    """Calculate the area of a selected geometric shape."""
    while True:
        print("\n" + "=" * 60)
        print("                 AREA CALCULATOR")
        print("=" * 60)
        print("1. Circle")
        print("2. Rectangle")
        print("3. Triangle")
        print("4. Square")
        print("5. Return to main menu")

        choice = input("Enter your choice: ").strip()

        if choice == "5":
            break

        if choice == "1":
            radius = read_number("Enter the radius: ")
            if radius < 0:
                print("Radius cannot be negative.")
            else:
                area = math.pi * radius ** 2
                print(f"Area of circle: {area:.2f} square units")

        elif choice == "2":
            length = read_number("Enter the length: ")
            width = read_number("Enter the width: ")

            if length < 0 or width < 0:
                print("Length and width cannot be negative.")
            else:
                area = length * width
                print(f"Area of rectangle: {area:.2f} square units")

        elif choice == "3":
            base = read_number("Enter the base: ")
            height = read_number("Enter the height: ")

            if base < 0 or height < 0:
                print("Base and height cannot be negative.")
            else:
                area = (1 / 2) * base * height
                print(f"Area of triangle: {area:.2f} square units")

        elif choice == "4":
            side = read_number("Enter the side: ")

            if side < 0:
                print("Side cannot be negative.")
            else:
                area = side ** 2
                print(f"Area of square: {area:.2f} square units")

        else:
            print("Invalid choice. Please try again.")


def main():
    """Display the main menu."""
    while True:
        print("\n" + "#" * 60)
        print("          PYTHON CALCULATOR AND AREA SYSTEM")
        print("#" * 60)
        print("1. Open calculator")
        print("2. Calculate area")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            calculator()
        elif choice == "2":
            calculate_area()
        elif choice == "3":
            print("Thank you for using the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()