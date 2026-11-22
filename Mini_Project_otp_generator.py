"""
Unit 2 - Mini Project
OTP Generator and Verification System

This educational program generates a six-digit OTP and allows
the user a limited number of verification attempts.
"""

import random
from datetime import datetime


def generate_otp():
    """Generate a six-digit one-time password."""
    return random.randint(100000, 999999)


def display_otp_information(otp):
    """Display OTP information for this classroom demonstration."""
    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    print("\n" + "=" * 60)
    print("                 OTP GENERATED")
    print("=" * 60)
    print(f"Generated at: {current_time}")
    print(f"Your demonstration OTP is: {otp}")
    print("=" * 60)


def verify_otp(correct_otp, maximum_attempts=3):
    """Verify the OTP using a limited number of attempts."""
    for attempt in range(1, maximum_attempts + 1):
        try:
            entered_otp = int(input("Enter the six-digit OTP: "))
        except ValueError:
            print("OTP must contain digits only.")
            continue

        if entered_otp == correct_otp:
            return True

        remaining_attempts = maximum_attempts - attempt

        if remaining_attempts > 0:
            print(f"Incorrect OTP. Attempts remaining: {remaining_attempts}")
        else:
            print("You have used all verification attempts.")

    return False


def main():
    """Run the OTP generator and verification process."""
    print("=" * 60)
    print("              OTP GENERATOR SYSTEM")
    print("=" * 60)
    print("This is a classroom demonstration program.")

    otp = generate_otp()
    display_otp_information(otp)

    is_verified = verify_otp(otp)

    print("\n" + "=" * 60)

    if is_verified:
        print("OTP verified successfully.")
        print("Access granted.")
    else:
        print("OTP verification failed.")
        print("Access denied.")

    print("=" * 60)


if __name__ == "__main__":
    main()