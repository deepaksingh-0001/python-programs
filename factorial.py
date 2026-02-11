#Program: Factorial of a Number

# Taking input from the user
num = int(input("Enter a number: "))

# Validate input
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    fact = 1

    # Loop to calculate factorial
    for i in range(1, num + 1):
        fact *= i

    # Display result
    print(f"Factorial of {num} is {fact}")
