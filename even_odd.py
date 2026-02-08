# Program to check whether a number is even or odd

# Taking input from the user
num = int(input("Enter a number: "))

# Checking even or odd using modulus operator
if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")