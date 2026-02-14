#This program checks whether a number is a palindrome or not.

# Taking input from the user
num = int(input("Enter a number: "))

# Store original number
n = num
rev = 0

# Reverse the number
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

# Check palindrome
if n == rev:
    print(f"{n} is a palindrome number")
else:
    print(f"{n} is not a palindrome number")