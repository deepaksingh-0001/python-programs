# Program to replace a substring inside a string

main_str = input("Enter the main string: ")
old_str = input("Enter the substring to replace: ")
new_str = input("Enter the new substring: ")

result = main_str.replace(old_str, new_str)

print("String after replacement:", result)