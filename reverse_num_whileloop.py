#Program: Reverse a Number

# Taking input from the user
num = int(input("Enter a number: "))

# Store original number
temp = num
rev = 0

# Reverse logic
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

# Display result
print(f"Reverse of {temp} is: {rev}")