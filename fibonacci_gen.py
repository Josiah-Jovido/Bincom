#!/usr/bin/env python3
"""
Author : Josiah-Oborekanhwo <josiahjovido@gmail.com>
Date   : 2021-03-15
Purpose: Implement a Fibonacci series generator
"""

"""
A fibonacci series is a a series of numbers in which each number ( Fibonacci number ) is the sum of the two preceding numbers. 
The simplest is the series 1, 1, 2, 3, 5, 8, etc. For this script we will be generating the first 20 fibonacci numbers.
"""

#---------------------------------------------
# Create a fibonacci function
def fib():
    x2 = 1
    x3 = 1
    while True:
        x1 = x2
        x2 = x3
        x3 = x1 + x2
        yield x1

#---------------------------------------------
# store the fibonacci function in a variable
f = fib()

# Generate the first 20 fibonacci numbers
print(', '.join(str(next(f)) for i in range(20))) # Method 1: list comprehension

#Method 2: For loop
# for i in range(20):
#     print(next(f), end=' ')

"""
Method 1 or method 2 will work fine, My preference lies with method 1 because it has less lines of codes which corresponds
to less bytes.
"""
