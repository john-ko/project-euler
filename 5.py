"""
Smallest multiple
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

"""
 3 = prime
 5 = prime
 7 = prime
 9 = 3 * 3
 8 = 4 * 2
"""

from collections import defaultdict

def get_multiples(number):
    numbers = []
    for i in range(1, number):
        if number % i == 0:
            numbers.append(i)
    return numbers

def smallest_multiple():
    # must have at least all primes (2,3,5,7,11,13,17,19)

    

    # figure out from there?
    d = defaultdict(int)

    for i in range(1,20):
        if i == 1:
            continue

        
        d[i].append()


    pass

#print(get_multiples(20))

def test(number):
    
    total = int(number / 10)

    ratio = 1;

    while number > 100:
        ratio = ratio * .8
        number = int(number / 10)
        total += int(ratio * number)
    return total




print(test(100000))
