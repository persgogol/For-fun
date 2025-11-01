"""
Fibonacci Sequence Generator

This script allows users to generate Fibonacci numbers in two ways:
1. Generate a specific number of terms.
2. Generate all Fibonacci numbers up to a maximum value.

The Fibonacci sequence starts with 0 and 1. Each subsequent number is the sum of the previous two numbers.

Usage:
Run the script and follow the on-screen prompts to choose the generation method and enter your input.

Functions:
- generate_n_terms(n): Returns a list of the first n Fibonacci numbers.
- generate_up_to(limit): Returns a list of Fibonacci numbers up to 'limit'.

Author: Anonymous
Date: 2025-10-18
"""

def generate_n_terms(n):
    """Generate the first n Fibonacci numbers."""
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def generate_up_to(limit):
    """Generate Fibonacci numbers up to a maximum value."""
    sequence = []
    a, b = 0, 1
    while a <= limit:
        sequence.append(a)
        a, b = b, a + b
    return sequence

def main():
    print("Fibonacci Sequence Generator")
    print("----------------------------")
    print("Choose an option:")
    print("1. Generate a specific number of terms")
    print("2. Generate all Fibonacci numbers up to a maximum value")
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == "1":
        while True:
            try:
                n = int(input("Enter the number of terms to generate: ").strip())
                if n <= 0:
                    print("Please enter a positive integer.")
                    continue
                fib_sequence = generate_n_terms(n)
                print(f"The first {n} Fibonacci numbers are:")
                print(fib_sequence)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")
    elif choice == "2":
        while True:
            try:
                limit = int(input("Generate Fibonacci numbers up to: ").strip())
                if limit < 0:
                    print("Please enter a non-negative integer.")
                    continue
                fib_sequence = generate_up_to(limit)
                print(f"Fibonacci numbers up to {limit} are:")
                print(fib_sequence)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")
    else:
        print("Invalid choice. Please run the program again and select option 1 or 2.")

if __name__ == "__main__":
    main()
