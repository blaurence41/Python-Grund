"""
# Read three numbers.
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# Check which one of the numbers is the greatest
# and pass it to the largest_number variable.

largest_number = max(number1, number2, number3)
smallest_number = min(number1, number2, number3)
# Print the result.
print("The largest number is:", largest_number)
print("The smallest number is:", smallest_number)
"""
"""
# Store the current largest number here.
largest_number = -999999999

# Input the first value.
number = int(input("Enter a number or type -1 to stop: "))

# If the number is not equal to -1, continue.
while number != -1:
    # Is number larger than largest_number?
    if number > largest_number:
        # Yes, update largest_number.
        largest_number = number
    # Input the next number.
    number = int(input("Enter a number or type -1 to stop: "))

# Print the largest number.
print("The largest number is:", largest_number)
"""

secret_number = 51

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

# Input the first value.
number = int(input("Secret number: "))

# If the number is not equal to sec_number, continue.
while number != secret_number:
    print("Ha ha! You're stuck in my loop!")
    if number < secret_number:
        print("Higher!")
    if number > secret_number:
        print("Lower!")
    number = int(input("Guess again: "))

print("Well done, muggle! You are free now.")