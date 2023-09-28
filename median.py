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
print(numbers)

numbers.sort()

length = (len(numbers)+1)/2

if length%1 == 0:
    print(numbers[int(length)])
else:
    a = length +0.5
    b = length - 0.5
    sum = numbers[int(a)] + numbers[int(b)]
    print(sum/2)