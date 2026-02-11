# Program to find the sum of first N natural numbers

# Taking input from the user
n = int(input("Enter the value of n: "))

# Initializing sum variable
total = 0

# Loop to calculate sum of natural numbers
for i in range(1, n + 1):
    total = total + i

# Displaying the result
print("Sum of first", n, "natural numbers is:", total)
