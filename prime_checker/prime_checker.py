def is_prime(n: int) -> bool:
    """Return True if n is a prime number, otherwise False."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def generate_primes(limit: int) -> list:
    """Generate all prime numbers up to the given limit (inclusive)."""
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes


def main():
    print("Prime Checker and Generator")
    while True:
        choice = input("Enter a number to check prime, 'list' to generate primes, or 'quit' to exit: ")
        choice = choice.strip()
        if choice.lower() == 'quit':
            print("Goodbye!")
            break
        elif choice.lower() == 'list':
            try:
                limit = int(input("Generate primes up to: "))
                primes = generate_primes(limit)
                print(f"Primes up to {limit}:")
                print(primes)
            except ValueError:
                print("Invalid input. Please enter an integer.")
        else:
            try:
                n = int(choice)
                if is_prime(n):
                    print(f"{n} is a prime.")
                else:
                    print(f"{n} is not a prime.")
            except ValueError:
                print("Invalid input. Please enter an integer or 'list' or 'quit'.")


if __name__ == "__main__":
    main()
