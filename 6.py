"""
Sum square difference
Problem 6
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first
ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first
one hundred natural numbers and the square of the sum.
"""

def sum_square_difference(n):
    summation = n * (n + 1) / 2
    square_summation = n * (n+1) * (2*n + 1) / 6
    return summation * summation - square_summation


assert sum_square_difference(10) == 2640.0

print(sum_square_difference(1000))


