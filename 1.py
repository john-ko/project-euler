"""
Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def natrual_numbers(limit):
    max = int(limit/3) + 1
    sum = 0
    for i in range(max):
        # multiple of 3
        if i*3 < limit:
            sum+= i*3

        # multiple of 5
        if i*5 < limit:
            sum += i*5

    return sum


print(natrual_numbers(1000))
