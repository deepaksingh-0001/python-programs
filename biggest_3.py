#Program: Biggest of Three Numbers

# Taking input from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Finding the biggest number
if a >= b and a >= c:
    biggest = a
elif b >= a and b >= c:
    biggest = b
else:
    biggest = c

# Display result
print(f"{biggest} is the biggest number")