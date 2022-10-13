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

    numbers = sorted(numbers)
    len = len(numbers)
    if len ==0:
        return 0
    elif len == 1:
        return numbers[0]
    elif len % 2 == 0:
        n1 = numbers[len // 2]
        n2 = numbers[len//2 -1 ]
        return (n1 + n2)/2
    else:
        return numbers[len//2]

print(numbers)
