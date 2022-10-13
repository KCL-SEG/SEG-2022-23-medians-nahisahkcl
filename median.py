"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break



    len_numbers = len(numbers)
    if len_numbers % 2 ==0:
        tot = numbers[len_numbers/2] + numbers[(len_numbers/2)-1]
        median = tot/2
        return median
    else:
        median = numbers[(len_numbers-1)/2]
print(numbers)
