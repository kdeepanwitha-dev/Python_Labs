"""
Unit 2 - Lab Exercise 3
Fibonacci Series Using Recursion

Fibonacci sequence:
0, 1, 1, 2, 3, 5, 8, ...

Each term is the sum of the previous two terms.
"""


def read_positive_integer(prompt):
    """Read a positive integer from the user."""
    while True:
        try:
            number = int(input(prompt))

            if number <= 0:
                print("Please enter a number greater than zero.")
            else:
                return number

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def fibonacci(term):
    """
    Return the Fibonacci value at a given position using recursion.

    Base cases:
    fibonacci(0) = 0
    fibonacci(1) = 1
    """
    if term == 0:
        return 0

    if term == 1:
        return 1

    return fibonacci(term - 1) + fibonacci(term - 2)


def generate_fibonacci_series(number_of_terms):
    """Generate a Fibonacci list by calling the recursive function."""
    series = []

    for term in range(number_of_terms):
        series.append(fibonacci(term))

    return series


def display_series(series):
    """Display the Fibonacci series neatly."""
    print("\n" + "=" * 60)
    print("              FIBONACCI SERIES")
    print("=" * 60)

    print("Number of terms:", len(series))
    print("Series:")
    print(" → ".join(map(str, series)))

    print("=" * 60)


def main():
    """Run the Fibonacci program."""
    print("=" * 60)
    print("        FIBONACCI SERIES USING RECURSION")
    print("=" * 60)

    number_of_terms = read_positive_integer(
        "Enter the number of terms required: "
    )

    if number_of_terms > 30:
        print(
            "Warning: Large values may take time because this demonstration "
            "uses recursion."
        )

    series = generate_fibonacci_series(number_of_terms)
    display_series(series)


if __name__ == "__main__":
    main()