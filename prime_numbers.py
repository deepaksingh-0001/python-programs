#Program: Prime Numbers up to N

# Taking input from the user
n = int(input("Enter the value of n: "))

# Validate input
if n < 2:
    print("There are no prime numbers less than 2.")
else:
    print(f"Prime numbers up to {n} are:")

    for num in range(2, n + 1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, end=" ")
