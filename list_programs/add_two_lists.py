#program to concatenate two lists using user input

lst1 = list(map(int, input("Enter list 1 elements: ").split()))
lst2 = list(map(int, input("Enter list 2 elements: ").split()))

final_list = lst1 + lst2   # concatenate two lists

print("Combined list:", final_list)