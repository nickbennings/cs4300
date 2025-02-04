"""
task3.py - Shows control structures in Python:
1. An if-elif-else statement to check if a number is positive, negative, or zero.
2. A while loop to generate the first n prime numbers.
3. A while loop to compute the sum of numbers from 1 to 100.
"""

def check_number(n):
    """Returns whether a number is Positive, Negative, or Zero."""
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

def first_n_primes(n):
    """
    Generates the first n prime numbers using a while loop.

    A number is prime if it is greater than 1 and has no divisors other than 1 and itself.
    """
    primes = []
    num = 2  # Start checking from 2 (first prime number)
    while len(primes) < n:
        for i in range(2, num):  # Check divisibility
            if num % i == 0:
                break  # Not a prime, move to next number
        else:
            primes.append(num)  # Prime number found
        num += 1
    return primes

def sum_numbers_upto_100():
    """Computes and returns the sum of numbers from 1 to 100 using a while loop."""
    total = 0
    num = 1
    while num <= 100:
        total += num
        num += 1
    return total

