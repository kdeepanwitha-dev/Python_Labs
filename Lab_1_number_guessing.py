"""
Unit 2 - Lab Exercise 1
Number Guessing Game

The computer selects a random number between 1 and 100.
The player receives hints until the correct number is guessed.
"""

import random


def read_integer(prompt, minimum=None, maximum=None):
    """Read and validate an integer from the user."""
    while True:
        try:
            value = int(input(prompt))

            if minimum is not None and value < minimum:
                print(f"Please enter a number greater than or equal to {minimum}.")
                continue

            if maximum is not None and value > maximum:
                print(f"Please enter a number less than or equal to {maximum}.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def play_game():
    """Run one round of the number guessing game."""
    secret_number = random.randint(1, 100)
    attempts = 0

    print("\nI have selected a number between 1 and 100.")
    print("Try to guess it!")

    while True:
        guess = read_integer("Enter your guess: ", 1, 100)
        attempts += 1

        if guess < secret_number:
            print("Hint: Your guess is too low.")
        elif guess > secret_number:
            print("Hint: Your guess is too high.")
        else:
            print("\nCongratulations! You guessed the correct number.")
            print(f"Number of attempts: {attempts}")

            if attempts == 1:
                print("Excellent! You guessed it on your first attempt.")
            elif attempts <= 5:
                print("Very good performance!")
            else:
                print("Good effort! Keep practising.")

            break


def main():
    """Display the game menu."""
    print("=" * 60)
    print("                 NUMBER GUESSING GAME")
    print("=" * 60)

    while True:
        play_game()

        again = input("\nWould you like to play again? (y/n): ").strip().lower()

        if again != "y":
            print("\nThank you for playing!")
            break


if __name__ == "__main__":
    main()