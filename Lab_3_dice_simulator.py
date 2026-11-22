import random

def roll_dice():
    """Simulate rolling a standard 6-sided dice."""
    return random.randint(1, 6)

def main():
    print("=== Dice Rolling Simulator ===")
    print("Press Enter to roll the dice")
    print("Type 'q' and press Enter to quit\n")

    while True:
        user_input = input("Roll the dice? (Enter / q): ").strip().lower()

        if user_input == 'q':
            print("\nThanks for playing! Goodbye!")
            break

        result = roll_dice()
        print(f"🎲 You rolled a {result}\n")

if __name__ == "__main__":
    main()