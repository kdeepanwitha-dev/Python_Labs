"""
Unit 2 - Lab Exercise 2
Prime Number and Factorial Program

This program:
1. Checks whether a number is prime.
2. Calculates its factorial.
3. Displays the factors of the number.
"""


def read_non_negative_integer(prompt):
    """Read a non-negative integer."""
    while True:
        try:
            number = int(input(prompt))

            if number < 0:
                print("Please enter a non-negative number.")
            else:
                return number

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def is_prime(number):
    """
    Return True if number is prime, otherwise return False.

    A prime number is greater than 1 and has only two factors:
    1 and itself.
    """
    if number < 2:
        return False

    if number == 2:
        return True

    if number % 2 == 0:
        return False

    divisor = 3

    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2

    return True


def calculate_factorial(number):
    """Calculate factorial using a loop."""
    factorial = 1

    for value in range(1, number + 1):
        factorial *= value

    return factorial


def find_factors(number):
    """Return all factors of a positive number."""
    if number == 0:
        return []

    factors = []

    for value in range(1, number + 1):
        if number % value == 0:
            factors.append(value)

    return factors


def display_result(number):
    """Display the complete analysis of the entered number."""
    print("\n" + "=" * 60)
    print("                  NUMBER ANALYSIS")
    print("=" * 60)

    print(f"Number entered: {number}")

    if is_prime(number):
        print(f"Prime status: {number} is a prime number.")
    else:
        print(f"Prime status: {number} is not a prime number.")

    print(f"Factorial: {number}! = {calculate_factorial(number)}")

    if number == 0:
        print("Factors: Zero has infinitely many factors.")
    else:
        factors = find_factors(number)
        print("Factors:", ", ".join(map(str, factors)))

    print("=" * 60)


def main():
    """Run the prime and factorial program."""
    print("=" * 60)
    print("             PRIME NUMBER AND FACTORIAL")
    print("=" * 60)

    number = read_non_negative_integer("Enter a non-negative integer: ")
    display_result(number)


if __name__ == "__main__":
    main()