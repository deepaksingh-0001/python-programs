# Take space-separated numbers from user and convert to list

user_input = input("Enter the elements: ")
l = list(map(int, user_input.split()))

print("List is:", l)