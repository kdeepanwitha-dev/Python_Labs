def frequency_counter():
    # Take input from user
    text = input("Enter a string: ")

    # Create an empty dictionary
    freq = {}

    # Count frequency of each character
    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    # Display the result
    print("\nCharacter Frequency:")
    print("-" * 25)
    for key, value in freq.items():
        print(f"'{key}' : {value}")


# Run the program
frequency_counter()