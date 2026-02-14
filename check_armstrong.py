# This program checks whether a number is an Armstrong number or not.

# Taking input from the user
num = int(input("Enter a number: "))

# Store original number
check = num
total = 0
digits = len(str(num))

# Armstrong logic
while num > 0:
    digit = num % 10
    total += digit ** digits
    num //= 10

# Check result
if check == total:
    print(f"{check} is an Armstrong number")
else:
    print(f"{check} is not an Armstrong number")