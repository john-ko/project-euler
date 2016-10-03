"""
Largest palindrome product
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from collections import defaultdict

def is_palindrome(number):
    string = str(number)
    for i in range(int(len(string)/2)):
        if string[i] != string[len(string) - 1 - i]:
            return False
    return True

def largest_palindrome_product():
    
    # 111 * 112
    # i dont want to check 112 * 111

    start = 111
    max = 0

    # O(n^2) which makes me sad
    for a in range(111, 999):
        for b in range(start, 999):
            if is_palindrome(a*b) and max < a * b:
                max = a * b

            
        # to skip already computed numbers
        start += 1

    return max

assert is_palindrome(90409) == True
assert is_palindrome(393934) == False
print(largest_palindrome_product())
