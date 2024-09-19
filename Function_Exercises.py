# Function Exercises

"""
Create a function that multiplies all unnamed arguments received
Return the total to a variable and display the value of the variable.
"""
import random

def multiplication(*args):
    total = 1
    for num in args:
        total *= num
    return total

numbers = []

i = 0

while i <= random.randint(0, 9):
    numbers.append(random.randint(0, 9))
    i += 1

variable = multiplication(*numbers)
print('The result of the multiplication is', variable, f'\t(list of multiplied numbers: {numbers})')

"""
Create a function that tells whether a number is even or odd.
Return whether the number is even or odd.
"""

def test(a):
    if a % 2 == 0:
        return f'The number {a} is even!'
    return f'The number {a} is odd!'
    
print(test(random.randint(0, 1000)))