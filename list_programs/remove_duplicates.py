# Remove duplicates without using loop

lst = [1, 1, 1, 2, 2, 4, 4, 5, 5, 8, 9, 7, 3, 3]

new_list = list(set(lst))   # convert to set to remove duplicates
print("orginal list: ",lst)
print("List without duplicates:", new_list)