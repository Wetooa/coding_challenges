from functools import reduce


def euclidean_division(a, b):
    """
    Calculate the greatest common divisor (GCD) of two numbers using the Euclidean division algorithm.

    The Euclidean division algorithm works by repeatedly dividing the larger number by the smaller number
    and replacing the larger number with the remainder until the remainder is zero. The last non-zero
    remainder is the GCD.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The GCD of the two numbers.
    """
    return (
        b
        if a % b == 0
        else euclidean_division(a % b, b) if a > b else euclidean_division(b % a, a)
    )


def euclidean_subtraction(a, b):
    """
    Calculate the greatest common divisor (GCD) of two numbers using the Euclidean subtraction algorithm.

    The Euclidean subtraction algorithm works by repeatedly subtracting the smaller number from the larger
    number until the two numbers are equal. The resulting number is the GCD.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The GCD of the two numbers.
    """
    return (
        b
        if a == b
        else (
            euclidean_subtraction(a - b, b)
            if a > b
            else euclidean_subtraction(a, b - a)
        )
    )


def get_factors(a):
    """
    Get all factors of a number up to its square root.

    This function finds all numbers that divide the given number `a` without leaving a remainder.
    It only checks numbers up to the square root of `a` for efficiency.

    Args:
        a (int): The number to find factors for.

    Returns:
        list: A list of factors of the number.
    """
    lim = int(a**0.5) + 1
    return [i for i in range(2, lim) if a % i == 0]


def prime_factorization(a, b):
    """
    Calculate the product of common prime factors of two numbers.

    This function finds the prime factors of both numbers, identifies the common factors, and calculates
    their product. It uses the `get_factors` function to find the factors of each number.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The product of common prime factors of the two numbers.
    """
    x = get_factors(a)
    y = get_factors(b)

    return reduce(lambda x, y: x * y, set(x).intersection(set(y)))


# Example usage
a = 48
b = 18

# Calculate GCD using different methods
gcd_ed = euclidean_division(a, b)  # GCD using Euclidean division
gcd_es = euclidean_subtraction(a, b)  # GCD using Euclidean subtraction
gcd_pf = prime_factorization(a, b)  # GCD using prime factorization

# Print the results
print(gcd_ed, gcd_es, gcd_pf)
