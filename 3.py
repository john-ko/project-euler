"""
Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
from math import sqrt

def is_prime(number):
    for i in range(int(sqrt(number))):
        if i + 1 < 2:
            continue

        if number % (i + 1) == 0:
            return False

    return True

def largest_prime_factor(number):

    # keep a list of prime

    # smaller n
    number_range = sqrt(number) / 2

    numbers = []

    # only looping through odd numbers
    for i in range(int(number_range)):
        # using only odd numbers
        j = i * 2 + 1

        if is_prime(j) and number % (j) == 0:
            numbers.append(j)

    return numbers[-1]

assert(largest_prime_factor(13195) == 29)

# this one takes like 9s ... theres probably a better way to check
print(largest_prime_factor(600851475143))