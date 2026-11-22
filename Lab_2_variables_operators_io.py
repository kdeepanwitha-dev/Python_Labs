"""
Lab Exercise 2: Variables, Operators, and Input/Output
"""

print("=" * 60)
print("       VARIABLES, OPERATORS AND INPUT/OUTPUT")
print("=" * 60)

name = input("Enter your name: ").strip()

while True:
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            print("Age cannot be negative.")
        else:
            break
    except ValueError:
        print("Please enter age as a whole number.")

while True:
    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))
        break
    except ValueError:
        print("Please enter valid numeric values.")

print("\n" + "-" * 60)
print("RESULTS")
print("-" * 60)

print(f"Hello, {name}!")
print(f"You are {age} years old.")
print(f"Next year, you will be {age + 1} years old.")

print(f"\nFirst number: {first_number}")
print(f"Second number: {second_number}")

print("\nArithmetic operations:")
print(f"Addition:       {first_number} + {second_number} = "
      f"{first_number + second_number}")

print(f"Subtraction:    {first_number} - {second_number} = "
      f"{first_number - second_number}")

print(f"Multiplication: {first_number} * {second_number} = "
      f"{first_number * second_number}")

if second_number != 0:
    print(f"Division:        {first_number} / {second_number} = "
          f"{first_number / second_number:.2f}")

    print(f"Floor division:  {first_number} // {second_number} = "
          f"{first_number // second_number}")

    print(f"Remainder:       {first_number} % {second_number} = "
          f"{first_number % second_number}")
else:
    print("Division, floor division, and remainder are not possible by zero.")

print(f"Power:           {first_number} ** {second_number} = "
      f"{first_number ** second_number}")

print("-" * 60)