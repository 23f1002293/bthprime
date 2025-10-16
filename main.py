import sys
import math

def is_prime(n):
    """Checks if a number is prime using an optimized trial division."""
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

def get_pth_prime(p):
    """Finds the p-th prime number."""
    if p < 1:
        raise ValueError("Input must be a positive integer.")
    
    if p == 1:
        return 2

    count = 1
    num = 3
    while count < p:
        if is_prime(num):
            count += 1
        if count == p:
            return num
        num += 2 # Check only odd numbers
    return num # Should be found in the loop, but as a fallback

def main():
    """Main function to handle command-line arguments."""
    if len(sys.argv) != 2:
        print("Usage: python main.py <p>")
        print("where <p> is a positive integer indicating the prime to find.")
        sys.exit(1)

    try:
        p = int(sys.argv[1])
        if p < 1:
            raise ValueError()
    except ValueError:
        print("Error: Input must be a positive integer.")
        sys.exit(1)

    try:
        prime = get_pth_prime(p)
        print(f"The {p}th prime number is: {prime}")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
